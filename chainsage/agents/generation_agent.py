"""
Generation Agent for ChainSage - Natural Language to Solidity Contract Generation.

Uses OpenAI function calling to integrate with Solidity generation tools,
following research/openai patterns for tool integration and iterative refinement.
"""

import json
import logging
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime

from ..agents.models import (
    GenerationRequest, GeneratedContract, ContractType,
    AgentMessage, AgentContext, ToolResult
)
from ..core.providers import get_llm_provider_manager
from ..tools.solidity_generator import SolidityGenerator
from ..tools.openzeppelin_helper import OpenZeppelinHelper

logger = logging.getLogger(__name__)


class GenerationAgent:
    """
    Primary agent for natural language to Solidity contract generation.

    Follows research/openai function calling patterns and multi-agent
    architecture from PRPs/EXAMPLE_multi_agent_prp.md.
    """

    def __init__(self):
        self.llm_manager = get_llm_provider_manager()
        self.solidity_generator = SolidityGenerator()
        self.openzeppelin_helper = OpenZeppelinHelper()

        # Tool definitions for OpenAI function calling
        self.tools = self._initialize_tools()

        # System prompt with comprehensive context from research
        self.system_prompt = self._build_system_prompt()

    def _initialize_tools(self) -> List[Dict[str, Any]]:
        """
        Initialize tool definitions for OpenAI function calling.

        Follows research/openai/page6_function_calling.md patterns.
        """
        return [
            {
                "type": "function",
                "function": {
                    "name": "generate_solidity_contract",
                    "description": "Generate a Solidity smart contract from natural language specification",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "contract_name": {
                                "type": "string",
                                "description": "Name of the contract to generate"
                            },
                            "contract_type": {
                                "type": "string",
                                "enum": ["erc20", "erc721", "erc1155", "governance", "custom"],
                                "description": "Type of contract to generate"
                            },
                            "security_features": {
                                "type": "array",
                                "items": {"type": "string"},
                                "description": "Security features to include (pausable, burnable, etc.)"
                            },
                            "specification": {
                                "type": "string",
                                "description": "Detailed natural language specification"
                            },
                            "complexity_level": {
                                "type": "integer",
                                "minimum": 1,
                                "maximum": 10,
                                "description": "Complexity level (1-10)"
                            }
                        },
                        "required": ["contract_name", "contract_type", "specification"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "enhance_with_security_patterns",
                    "description": "Enhance generated contract with OpenZeppelin security patterns",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "contract_code": {
                                "type": "string",
                                "description": "Solidity contract code to enhance"
                            },
                            "contract_type": {
                                "type": "string",
                                "enum": ["erc20", "erc721", "erc1155", "governance", "custom"],
                                "description": "Type of contract"
                            },
                            "requested_features": {
                                "type": "array",
                                "items": {"type": "string"},
                                "description": "Specific security features to inject"
                            },
                            "complexity_level": {
                                "type": "integer",
                                "minimum": 1,
                                "maximum": 10,
                                "description": "Contract complexity for security recommendations"
                            }
                        },
                        "required": ["contract_code", "contract_type"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "get_access_control_recommendation",
                    "description": "Get recommended access control pattern for the contract",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "complexity_level": {
                                "type": "integer",
                                "minimum": 1,
                                "maximum": 10,
                                "description": "Contract complexity level"
                            },
                            "expected_admins": {
                                "type": "integer",
                                "minimum": 1,
                                "description": "Expected number of administrators"
                            },
                            "use_case": {
                                "type": "string",
                                "description": "Brief description of the contract's use case"
                            }
                        },
                        "required": ["complexity_level", "expected_admins"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "validate_solidity_syntax",
                    "description": "Validate Solidity contract syntax and structure",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "contract_code": {
                                "type": "string",
                                "description": "Solidity code to validate"
                            }
                        },
                        "required": ["contract_code"]
                    }
                }
            }
        ]

    def _build_system_prompt(self) -> str:
        """Build comprehensive system prompt with research context."""
        return f"""You are ChainSage, an expert Solidity smart contract generation agent. Your mission is to transform natural language specifications into secure, production-ready smart contracts following the highest security standards.

## Core Capabilities

You have access to advanced tools for:
1. **Contract Generation**: Creating Solidity contracts from natural language
2. **Security Enhancement**: Integrating OpenZeppelin security patterns
3. **Access Control**: Recommending appropriate permission systems
4. **Validation**: Ensuring contract syntax and structure correctness

## Security-First Approach

ALWAYS prioritize security:
- Use OpenZeppelin contracts and patterns as the foundation
- Implement proper access controls (Ownable, AccessControl, or custom)
- Add reentrancy guards for functions handling ETH transfers
- Validate all address parameters for zero address
- Emit events for all state changes
- Follow checks-effects-interactions pattern
- Use appropriate Solidity version (^0.8.19 or later)

## Best Practices from Research

1. **Contract Structure**: Follow research/solidity patterns
   - Start with SPDX license identifier
   - Use semantic versioning for pragma
   - Import OpenZeppelin contracts first
   - Organize functions: constructor, external, public, internal, private

2. **OpenZeppelin Integration**: Follow research/openzeppelin patterns
   - Prefer composition over inheritance
   - Use established security patterns (ReentrancyGuard, Pausable, etc.)
   - Implement proper role-based access control when needed
   - Consider upgradeability patterns for complex contracts

3. **Gas Optimization**: Consider efficiency
   - Use appropriate data types
   - Pack structs efficiently
   - Use external for functions called externally
   - Implement batch operations where beneficial

## Contract Types Expertise

- **ERC20**: Fungible tokens with optional extensions (mintable, burnable, pausable, etc.)
- **ERC721**: Non-fungible tokens with metadata and enumeration
- **ERC1155**: Multi-token standard for both fungible and NFTs
- **Governance**: DAO governance with voting, proposals, and timelock
- **Custom**: Application-specific logic with security patterns

## Response Approach

1. **Understand**: Analyze the natural language specification thoroughly
2. **Plan**: Determine contract type, required features, and security needs
3. **Generate**: Use tools to create the initial contract
4. **Enhance**: Apply security patterns and optimizations
5. **Validate**: Ensure syntax correctness and completeness
6. **Explain**: Provide clear explanation of the generated contract

## Tool Usage Guidelines

- Use `generate_solidity_contract` for initial contract creation
- Use `enhance_with_security_patterns` to add security features
- Use `get_access_control_recommendation` for permission systems
- Use `validate_solidity_syntax` to ensure correctness

Always be thorough, security-conscious, and educational in your responses.

Current timestamp: {datetime.now().isoformat()}"""

    async def generate_contract(
        self,
        request: GenerationRequest,
        context: Optional[AgentContext] = None
    ) -> Tuple[GeneratedContract, List[AgentMessage]]:
        """
        Generate a Solidity contract from natural language specification.

        Args:
            request: Generation request with specification and requirements
            context: Optional agent context for conversation history

        Returns:
            Tuple of (generated_contract, conversation_messages)
        """
        conversation = []

        try:
            # Build initial conversation with user request
            messages = [
                {"role": "system", "content": self.system_prompt},
                {
                    "role": "user",
                    "content": self._build_user_prompt(request)
                }
            ]

            # Track conversation
            conversation.append(AgentMessage(
                role="user",
                content=self._build_user_prompt(request)
            ))

            # Start iterative generation process
            max_iterations = 3
            iteration = 0
            generated_contract = None

            while iteration < max_iterations:
                logger.info(f"Generation iteration {iteration + 1}/{max_iterations}")

                # Get model response with tools
                response = await self.llm_manager.chat_completion(
                    messages=messages,
                    tools=self.tools,
                    tool_choice="auto"
                )

                # Process response
                assistant_message = response.choices[0].message

                # Track assistant message
                conversation.append(AgentMessage(
                    role="assistant",
                    content=assistant_message.content or "",
                    tool_calls=self._format_tool_calls(assistant_message.tool_calls)
                ))

                # Add assistant message to conversation
                messages.append({
                    "role": "assistant",
                    "content": assistant_message.content,
                    "tool_calls": [
                        {
                            "id": tc.id,
                            "type": tc.type,
                            "function": {
                                "name": tc.function.name,
                                "arguments": tc.function.arguments
                            }
                        } for tc in (assistant_message.tool_calls or [])
                    ]
                })

                # Execute tool calls if present
                if assistant_message.tool_calls:
                    tool_results = []

                    for tool_call in assistant_message.tool_calls:
                        result = await self._execute_tool_call(tool_call, request)
                        tool_results.append(result)

                        # Add tool result to conversation
                        messages.append({
                            "role": "tool",
                            "tool_call_id": tool_call.id,
                            "content": json.dumps(result.result) if result.success else result.error_message
                        })

                        # Track tool message
                        conversation.append(AgentMessage(
                            role="tool",
                            content=json.dumps(result.result) if result.success else result.error_message,
                            tool_call_id=tool_call.id
                        ))

                        # Check if we got a contract
                        if result.tool_name == "generate_solidity_contract" and result.success:
                            generated_contract = result.result

                else:
                    # No tool calls, check if we have a final response
                    if generated_contract:
                        break

                iteration += 1

            # Ensure we have a generated contract
            if not generated_contract:
                # Fallback: generate contract directly
                logger.warning("No contract generated through function calling, using fallback")
                generated_contract = self.solidity_generator.generate_contract(request)

            return generated_contract, conversation

        except Exception as e:
            logger.error(f"Contract generation failed: {str(e)}")

            # Return error contract
            error_contract = GeneratedContract(
                contract_name="ErrorContract",
                solidity_code=f"// Error generating contract: {str(e)}",
                explanation=f"Failed to generate contract: {str(e)}",
                security_notes=["Manual review required due to generation error"],
                dependencies=[]
            )

            conversation.append(AgentMessage(
                role="assistant",
                content=f"Error generating contract: {str(e)}"
            ))

            return error_contract, conversation

    def _build_user_prompt(self, request: GenerationRequest) -> str:
        """Build comprehensive user prompt from generation request."""
        prompt = f"""Please generate a Solidity smart contract based on this specification:

**Specification**: {request.specification}

**Requirements**:
- Contract Type: {request.contract_type.value}
- Security Features: {', '.join(request.security_features) if request.security_features else 'Standard security patterns'}
- OpenZeppelin Integration: {'Enabled' if request.openzeppelin_integration else 'Disabled'}
- Complexity Level: {request.max_complexity}/10
- Include Tests: {'Yes' if request.include_tests else 'No'}
- Solidity Version: {request.solidity_version}

**Expected Output**:
1. Complete Solidity contract with all required functionality
2. Proper security patterns and OpenZeppelin integration
3. Comprehensive documentation and comments
4. Gas-efficient implementation
5. Production-ready code structure

Please use your available tools to generate the contract step by step."""

        return prompt

    async def _execute_tool_call(
        self,
        tool_call,
        request: GenerationRequest
    ) -> ToolResult:
        """Execute a tool call and return the result."""
        start_time = datetime.now()

        try:
            function_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            logger.info(f"Executing tool: {function_name} with args: {arguments}")

            if function_name == "generate_solidity_contract":
                return await self._tool_generate_contract(arguments, request)

            elif function_name == "enhance_with_security_patterns":
                return await self._tool_enhance_security(arguments)

            elif function_name == "get_access_control_recommendation":
                return await self._tool_get_access_control(arguments)

            elif function_name == "validate_solidity_syntax":
                return await self._tool_validate_syntax(arguments)

            else:
                return ToolResult(
                    tool_name=function_name,
                    success=False,
                    result=None,
                    error_message=f"Unknown tool: {function_name}",
                    execution_time=(datetime.now() - start_time).total_seconds()
                )

        except Exception as e:
            logger.error(f"Tool execution failed: {str(e)}")
            return ToolResult(
                tool_name=function_name,
                success=False,
                result=None,
                error_message=str(e),
                execution_time=(datetime.now() - start_time).total_seconds()
            )

    async def _tool_generate_contract(
        self,
        arguments: Dict[str, Any],
        original_request: GenerationRequest
    ) -> ToolResult:
        """Execute generate_solidity_contract tool."""
        start_time = datetime.now()

        try:
            # Create updated request from tool arguments
            updated_request = GenerationRequest(
                specification=arguments.get("specification", original_request.specification),
                contract_type=ContractType(arguments.get("contract_type", original_request.contract_type.value)),
                security_features=arguments.get("security_features", original_request.security_features),
                openzeppelin_integration=original_request.openzeppelin_integration,
                max_complexity=arguments.get("complexity_level", original_request.max_complexity),
                include_tests=original_request.include_tests,
                solidity_version=original_request.solidity_version
            )

            # Generate contract using tool
            generated_contract = self.solidity_generator.generate_contract(updated_request)

            return ToolResult(
                tool_name="generate_solidity_contract",
                success=True,
                result=generated_contract,
                error_message=None,
                execution_time=(datetime.now() - start_time).total_seconds()
            )

        except Exception as e:
            return ToolResult(
                tool_name="generate_solidity_contract",
                success=False,
                result=None,
                error_message=str(e),
                execution_time=(datetime.now() - start_time).total_seconds()
            )

    async def _tool_enhance_security(self, arguments: Dict[str, Any]) -> ToolResult:
        """Execute enhance_with_security_patterns tool."""
        start_time = datetime.now()

        try:
            contract_code = arguments["contract_code"]
            contract_type = ContractType(arguments["contract_type"])
            requested_features = arguments.get("requested_features", [])

            # Enhance with security patterns
            enhanced_code, injected_patterns, recommendations = self.openzeppelin_helper.inject_security_patterns(
                contract_code, requested_features, contract_type
            )

            result = {
                "enhanced_code": enhanced_code,
                "injected_patterns": injected_patterns,
                "security_recommendations": recommendations
            }

            return ToolResult(
                tool_name="enhance_with_security_patterns",
                success=True,
                result=result,
                error_message=None,
                execution_time=(datetime.now() - start_time).total_seconds()
            )

        except Exception as e:
            return ToolResult(
                tool_name="enhance_with_security_patterns",
                success=False,
                result=None,
                error_message=str(e),
                execution_time=(datetime.now() - start_time).total_seconds()
            )

    async def _tool_get_access_control(self, arguments: Dict[str, Any]) -> ToolResult:
        """Execute get_access_control_recommendation tool."""
        start_time = datetime.now()

        try:
            complexity = arguments["complexity_level"]
            expected_admins = arguments["expected_admins"]

            recommendation = self.openzeppelin_helper.generate_access_control_recommendations(
                complexity, expected_admins
            )

            return ToolResult(
                tool_name="get_access_control_recommendation",
                success=True,
                result=recommendation,
                error_message=None,
                execution_time=(datetime.now() - start_time).total_seconds()
            )

        except Exception as e:
            return ToolResult(
                tool_name="get_access_control_recommendation",
                success=False,
                result=None,
                error_message=str(e),
                execution_time=(datetime.now() - start_time).total_seconds()
            )

    async def _tool_validate_syntax(self, arguments: Dict[str, Any]) -> ToolResult:
        """Execute validate_solidity_syntax tool."""
        start_time = datetime.now()

        try:
            contract_code = arguments["contract_code"]

            is_valid, errors = self.solidity_generator.validate_solidity_syntax(contract_code)

            result = {
                "is_valid": is_valid,
                "errors": errors,
                "recommendations": [] if is_valid else [
                    "Fix syntax errors before deployment",
                    "Consider using a Solidity linter for additional validation"
                ]
            }

            return ToolResult(
                tool_name="validate_solidity_syntax",
                success=True,
                result=result,
                error_message=None,
                execution_time=(datetime.now() - start_time).total_seconds()
            )

        except Exception as e:
            return ToolResult(
                tool_name="validate_solidity_syntax",
                success=False,
                result=None,
                error_message=str(e),
                execution_time=(datetime.now() - start_time).total_seconds()
            )

    def _format_tool_calls(self, tool_calls) -> Optional[List[Dict[str, Any]]]:
        """Format tool calls for message logging."""
        if not tool_calls:
            return None

        return [
            {
                "id": tc.id,
                "type": tc.type,
                "function": {
                    "name": tc.function.name,
                    "arguments": tc.function.arguments
                }
            }
            for tc in tool_calls
        ]


if __name__ == "__main__":
    # Test generation agent
    import asyncio

    async def test_generation():
        agent = GenerationAgent()

        # Test ERC20 generation
        request = GenerationRequest(
            specification="Create a governance token called DAOToken with voting capabilities, minting restricted to owner, and pausable functionality for emergencies",
            contract_type=ContractType.ERC20,
            security_features=["mintable", "pausable", "votes"],
            openzeppelin_integration=True,
            max_complexity=7
        )

        try:
            contract, conversation = await agent.generate_contract(request)
            print("✅ Generation Agent test completed")
            print(f"📄 Generated contract: {contract.contract_name}")
            print(f"💬 Conversation steps: {len(conversation)}")
            print(f"🔧 Functions: {len(contract.functions)}")
            print(f"🛡️ Security notes: {len(contract.security_notes)}")
            print(f"⛽ Estimated gas: {contract.estimated_gas}")
        except Exception as e:
            print(f"❌ Generation failed: {e}")

    asyncio.run(test_generation())