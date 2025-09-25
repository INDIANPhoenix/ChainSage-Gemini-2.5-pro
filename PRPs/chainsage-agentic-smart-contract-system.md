name: "ChainSage: Agentic AI Smart Contract Generator & Auditor"
description: |

## Purpose
Production-ready agentic AI system that transforms natural language specifications into secure Solidity smart contracts with integrated AI-powered security auditing. Features both Web UI and CLI interfaces with comprehensive static analysis integration.

## Core Principles
1. **Context is King**: Include ALL necessary documentation, examples, and caveats
2. **Validation Loops**: Provide executable tests/lints the AI can run and fix
3. **Information Dense**: Use keywords and patterns from the codebase
4. **Progressive Success**: Start simple, validate, then enhance
5. **Global rules**: Be sure to follow all rules in CLAUDE.md

---

## Goal
Build a comprehensive agentic AI system called "ChainSage" that accepts natural language specifications and produces production-ready Solidity smart contracts with integrated security analysis. The system includes Web UI (Next.js + Tailwind), CLI interface, FastAPI backend, and integrates Slither/Surya static analysis tools.

## Why
- **Business value**: Democratizes smart contract development by removing technical barriers
- **Integration**: Bridges the gap between business requirements and secure smart contract implementation
- **Problems solved**: Reduces smart contract vulnerabilities, accelerates development cycles, provides comprehensive audit trails

## What
Multi-modal application featuring:
- **Generation Agent**: Transforms natural language specs into Solidity using OpenZeppelin patterns
- **Audit Agent**: LLM-based security review with Slither/Surya integration and patch proposals
- **Web UI**: Next.js application for spec input, code preview, audit management, patch application
- **CLI**: Power user interface for generation, auditing, patching, and test scaffolding
- **Backend API**: FastAPI service exposing agent capabilities via RESTful endpoints

### Success Criteria
- [ ] Generate secure Solidity contracts from natural language specifications
- [ ] Integrate OpenZeppelin security patterns automatically
- [ ] Perform comprehensive AI-powered security audits
- [ ] Generate actionable patch proposals for vulnerabilities
- [ ] Support both Web UI and CLI workflows
- [ ] Output organized artifacts to /out/ directory
- [ ] Pass comprehensive test suites and validation gates

## All Needed Context

### Documentation & References (MUST READ)
```yaml
# Solidity & OpenZeppelin Research
- docfile: research/solidity/page1_intro_smart_contracts.md
  why: Foundation patterns, SimpleStorage and Subcurrency examples (36KB)

- docfile: research/solidity/page2_solidity_by_example.md
  why: Complex voting contract with delegation, structs, access control (81KB)

- docfile: research/solidity/page3_contracts.md
  why: Complete contract structure, functions, modifiers, events, errors, inheritance (152KB)

- docfile: research/solidity/page4_security.md
  why: Critical security considerations, reentrancy, overflow, gas limits (27KB)

- docfile: research/solidity/page5_types.md
  why: All Solidity data types, mappings, arrays, structs (132KB)

- docfile: research/openzeppelin/page2_access_control.md
  why: Comprehensive access control patterns (31KB)

- docfile: research/openzeppelin/page22_utils_api.md
  why: Massive utilities documentation with security patterns (336KB)

- docfile: research/openzeppelin/page23_governance.md
  why: Comprehensive governance system patterns (26KB)

# FastAPI Backend Research
- docfile: research/fastapi/page20_bigger_applications.md
  why: Production-ready app structure using APIRouter, modular organization

- docfile: research/fastapi/page23_databases.md
  why: Comprehensive database patterns with SQLAlchemy, async handling (281KB)

- docfile: research/fastapi/page8_dependencies.md
  why: Dependency injection patterns, shared logic, database connections

- docfile: research/fastapi/page9_security.md
  why: Security fundamentals, OAuth2, JWT tokens

# Next.js Frontend Research
- docfile: research/nextjs/page2_app_router.md
  why: App Router system, file-based routing (87KB)

- docfile: research/nextjs/page3_server_components.md
  why: Server components architecture and patterns (90KB)

- docfile: research/nextjs/page7_server_actions.md
  why: Modern form handling with Server Actions (87KB)

- docfile: research/nextjs/page12_project_structure.md
  why: App Router directory structure and organization (99KB)

# OpenAI Integration Research
- docfile: research/openai/page1_overview.md
  why: Latest API patterns and model selection

- docfile: research/openai/page3_chat.md
  why: Chat completions API with function calling (584KB)

- docfile: research/openai/page8_function_calling.md
  why: Tool integration patterns for agents (34KB)

# Static Analysis Tools Research
- docfile: research/static-analysis/page3_slither_detectors.md
  why: Complete detector documentation with 99 built-in detectors (115KB)

- docfile: research/static-analysis/page4_slither_usage.md
  why: Usage patterns and CLI commands (95KB)

- docfile: research/static-analysis/page2_surya_main.md
  why: Visual analysis tools, graph generation (47KB)

# Agent Pattern Reference
- file: PRPs/EXAMPLE_multi_agent_prp.md
  why: Multi-agent system patterns, agent-as-tool, dependency injection
```

### Current Codebase Tree
```bash
.
├── research/                    # Exhaustive documentation (110+ pages)
│   ├── solidity/               # 25 pages of Solidity documentation
│   ├── openzeppelin/           # 25 pages of OpenZeppelin patterns
│   ├── fastapi/                # 26 pages of FastAPI documentation
│   ├── nextjs/                 # 20 pages of Next.js documentation
│   ├── openai/                 # 22 pages of OpenAI SDK documentation
│   └── static-analysis/        # 21 pages of Slither/Surya documentation
├── PRPs/
│   ├── templates/
│   │   └── prp_base.md
│   └── EXAMPLE_multi_agent_prp.md
├── CLAUDE.md                   # Project instructions and constraints
├── initial.md                  # Feature specification
└── README.md
```

### Desired Codebase Tree with Files to be Added
```bash
.
├── chainsage/                  # Main application package
│   ├── __init__.py            # Package initialization
│   ├── agents/                # Agent system core
│   │   ├── __init__.py
│   │   ├── generation_agent.py    # NL → Solidity generation agent
│   │   ├── audit_agent.py         # Security audit and patch agent
│   │   ├── orchestrator.py       # Primary agent orchestrator
│   │   └── models.py              # Pydantic models for agents
│   ├── tools/                 # Agent tools and integrations
│   │   ├── __init__.py
│   │   ├── solidity_generator.py  # Solidity code generation utilities
│   │   ├── static_analyzer.py     # Slither/Surya integration
│   │   ├── openzeppelin_helper.py # OpenZeppelin pattern integration
│   │   └── patch_generator.py     # Vulnerability patch generation
│   ├── core/                  # Core system components
│   │   ├── __init__.py
│   │   ├── config.py          # Configuration and environment management
│   │   ├── providers.py       # LLM provider abstraction
│   │   └── utils.py           # Shared utilities
│   └── cli/                   # CLI interface
│       ├── __init__.py
│       ├── main.py            # CLI entry point
│       ├── commands.py        # CLI command implementations
│       └── display.py         # CLI output formatting
├── api/                       # FastAPI backend
│   ├── __init__.py
│   ├── main.py               # FastAPI application entry
│   ├── routers/              # API route modules
│   │   ├── __init__.py
│   │   ├── generation.py     # Contract generation endpoints
│   │   ├── audit.py          # Audit endpoints
│   │   └── artifacts.py      # File management endpoints
│   ├── middleware/           # API middleware
│   │   ├── __init__.py
│   │   ├── cors.py          # CORS configuration
│   │   └── auth.py          # Authentication middleware
│   └── models/              # API models
│       ├── __init__.py
│       ├── requests.py      # Request schemas
│       └── responses.py     # Response schemas
├── frontend/                # Next.js Web UI
│   ├── app/                # App Router structure
│   │   ├── layout.tsx      # Root layout
│   │   ├── page.tsx        # Home page
│   │   ├── generate/       # Contract generation flow
│   │   │   ├── page.tsx
│   │   │   └── components/ # Generation-specific components
│   │   ├── audit/          # Audit management flow
│   │   │   ├── page.tsx
│   │   │   └── components/ # Audit-specific components
│   │   └── api/           # Next.js API routes
│   │       ├── generate.ts # Generation proxy endpoint
│   │       └── audit.ts   # Audit proxy endpoint
│   ├── components/        # Shared React components
│   │   ├── ui/           # Base UI components
│   │   ├── forms/        # Form components
│   │   ├── editor/       # Code editor components
│   │   └── layout/       # Layout components
│   ├── lib/              # Frontend utilities
│   │   ├── api.ts        # API client
│   │   ├── utils.ts      # Shared utilities
│   │   └── types.ts      # TypeScript definitions
│   ├── styles/           # Styling
│   │   └── globals.css   # Global styles with Tailwind
│   ├── package.json      # Frontend dependencies
│   ├── tailwind.config.js # Tailwind configuration
│   └── tsconfig.json     # TypeScript configuration
├── out/                  # Output directory for generated artifacts
│   ├── contracts/        # Generated .sol files
│   ├── audits/          # Audit reports (.md)
│   ├── patches/         # Patch files (.diff)
│   └── tests/           # Generated test files
├── tests/               # Comprehensive test suite
│   ├── __init__.py
│   ├── unit/           # Unit tests
│   │   ├── test_agents.py
│   │   ├── test_tools.py
│   │   └── test_api.py
│   ├── integration/    # Integration tests
│   │   ├── test_generation_flow.py
│   │   ├── test_audit_flow.py
│   │   └── test_cli.py
│   └── fixtures/       # Test fixtures and mock data
├── docker/             # Docker configuration
│   ├── Dockerfile.api  # API container
│   ├── Dockerfile.frontend # Frontend container
│   └── docker-compose.yml  # Full stack orchestration
├── .env.example        # Environment variables template
├── requirements.txt    # Python dependencies
├── pytest.ini         # Test configuration
├── mypy.ini           # Type checking configuration
├── README.md          # Comprehensive setup and usage guide
└── setup.py           # Package installation configuration
```

### Known Gotchas & Library Quirks
```python
# CRITICAL: OpenAI GPT models - Use latest recommended models from research
# GPT-5 is optimized for "coding and agentic tasks across domains" per OpenAI docs
MODEL_NAME = "gpt-4o-2024-11-20"  # From research/openai/page1_overview.md

# CRITICAL: Solidity security patterns from OpenZeppelin research
# Always use ReentrancyGuard for functions that transfer funds
# Always emit events for state changes
# Use AccessControl over Ownable for complex permissions

# CRITICAL: FastAPI async patterns from research
# All agent functions must be async - no sync functions in async context
# Use dependency injection for database connections and LLM clients
# Always validate inputs with Pydantic models

# CRITICAL: Next.js App Router patterns from research
# Use Server Components by default, opt into Client Components with 'use client'
# Server Actions for form handling without API routes
# File-based routing with special files (layout.tsx, loading.tsx, error.tsx)

# CRITICAL: Slither integration patterns from research
# 99 built-in detectors available, JSON output for programmatic processing
# Docker integration for consistent environments
# Rate limiting considerations for automated analysis

# CRITICAL: Agent system patterns from multi-agent example
# Use RunContext for dependency injection
# Pass ctx.usage for token tracking in multi-agent calls
# Agent-as-tool pattern for composition
```

## Implementation Blueprint

### Data Models and Structure

```python
# chainsage/agents/models.py - Core data structures
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

class ContractType(str, Enum):
    ERC20 = "erc20"
    ERC721 = "erc721"
    ERC1155 = "erc1155"
    GOVERNANCE = "governance"
    CUSTOM = "custom"

class SecurityLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class GenerationRequest(BaseModel):
    specification: str = Field(..., description="Natural language contract specification")
    contract_type: ContractType = Field(ContractType.CUSTOM, description="Type of contract to generate")
    security_features: List[str] = Field(default_factory=list, description="Required security features")
    openzeppelin_integration: bool = Field(True, description="Use OpenZeppelin patterns")
    max_complexity: int = Field(5, ge=1, le=10, description="Complexity level 1-10")

class GeneratedContract(BaseModel):
    contract_name: str
    solidity_code: str
    explanation: str
    security_notes: List[str]
    dependencies: List[str]
    estimated_gas: Optional[int] = None

class AuditFinding(BaseModel):
    id: str
    severity: SecurityLevel
    title: str
    description: str
    location: str  # File:line or function name
    recommendation: str
    cve_references: List[str] = Field(default_factory=list)

class AuditReport(BaseModel):
    contract_name: str
    findings: List[AuditFinding]
    overall_score: int = Field(..., ge=0, le=100)
    summary: str
    timestamp: datetime = Field(default_factory=datetime.now)

class PatchProposal(BaseModel):
    finding_id: str
    description: str
    diff_content: str  # Git diff format
    explanation: str
    risk_assessment: str
```

### List of Tasks to be Completed in Order

```yaml
Task 1: Core System Setup
CREATE chainsage/core/config.py:
  - PATTERN: Use pydantic-settings with environment variable validation
  - Load OpenAI API keys, Slither/Surya paths, output directories
  - Validate required dependencies and tools availability

CREATE chainsage/core/providers.py:
  - PATTERN: Follow research/openai patterns for client initialization
  - Support multiple LLM providers (OpenAI, Anthropic fallback)
  - Handle authentication, rate limiting, error handling

Task 2: Solidity Generation Tools
CREATE chainsage/tools/solidity_generator.py:
  - PATTERN: Use research/solidity patterns for contract structure
  - Template system for common patterns (ERC20, ERC721, Governance)
  - OpenZeppelin integration for security patterns
  - Code validation and syntax checking

CREATE chainsage/tools/openzeppelin_helper.py:
  - PATTERN: Use research/openzeppelin for access control and security
  - Auto-inject security patterns (ReentrancyGuard, AccessControl)
  - Import management for OpenZeppelin dependencies
  - Gas optimization recommendations

Task 3: Static Analysis Integration
CREATE chainsage/tools/static_analyzer.py:
  - PATTERN: Use research/static-analysis CLI patterns
  - Slither integration with JSON output parsing
  - Surya integration for contract visualization
  - Docker wrapper for consistent execution environment
  - Result aggregation and severity classification

Task 4: Generation Agent Implementation
CREATE chainsage/agents/generation_agent.py:
  - PATTERN: Follow multi-agent example structure from PRPs/
  - Use OpenAI function calling for tool integration
  - Register solidity_generator and openzeppelin_helper as tools
  - Iterative refinement based on specification feedback
  - Contract validation and compilation checking

Task 5: Audit Agent Implementation
CREATE chainsage/agents/audit_agent.py:
  - PATTERN: Follow multi-agent example with tool registration
  - Register static_analyzer as primary tool
  - LLM-based security pattern analysis
  - Vulnerability detection beyond static analysis
  - Generate actionable security recommendations

Task 6: Patch Generation System
CREATE chainsage/tools/patch_generator.py:
  - PATTERN: Use git diff format for patch representation
  - Automated fix generation for common vulnerabilities
  - Integration with audit findings for targeted patches
  - Validation of proposed changes

Task 7: Primary Orchestrator Agent
CREATE chainsage/agents/orchestrator.py:
  - PATTERN: Multi-agent orchestration from research examples
  - Coordinate between generation and audit agents
  - Manage workflow state and artifact organization
  - Handle user feedback and iterative improvement

Task 8: FastAPI Backend Implementation
CREATE api/main.py:
  - PATTERN: Use research/fastapi production application structure
  - APIRouter organization for scalability
  - Async/await throughout for non-blocking operations
  - Comprehensive error handling and logging

CREATE api/routers/:
  - PATTERN: Follow research/fastapi dependency injection patterns
  - Generation endpoints with streaming support
  - Audit endpoints with progress tracking
  - File management for artifact downloads

Task 9: Next.js Frontend Implementation
CREATE frontend/app/:
  - PATTERN: Use research/nextjs App Router architecture
  - Server Components for initial page loads
  - Client Components for interactive elements
  - Server Actions for form submissions

CREATE frontend/components/:
  - PATTERN: Modern React patterns with TypeScript
  - Code editor integration (Monaco Editor)
  - Real-time audit result display
  - File upload/download components

Task 10: CLI Interface Development
CREATE chainsage/cli/main.py:
  - PATTERN: Follow examples/cli.py streaming pattern from research
  - Color-coded output with progress indicators
  - Command organization (gen, audit, patch, scaffold)
  - Session management for conversation context

Task 11: Docker Integration
CREATE docker/:
  - PATTERN: Multi-stage builds for production optimization
  - Slither/Surya tool integration in containers
  - Development and production compose configurations
  - Volume management for persistent artifacts

Task 12: Comprehensive Testing
CREATE tests/:
  - PATTERN: Mirror production code structure
  - Mock external API calls (OpenAI, static analysis tools)
  - Test happy path, edge cases, error conditions
  - Integration tests for full workflow validation
```

### Per Task Pseudocode

```python
# Task 4: Generation Agent Implementation
class GenerationAgent:
    """Primary agent for natural language to Solidity conversion."""

    def __init__(self, llm_client: OpenAI, tools: List[Tool]):
        # PATTERN: Use OpenAI function calling from research/openai/page8_function_calling.md
        self.client = llm_client
        self.tools = {tool.name: tool for tool in tools}

    async def generate_contract(self, request: GenerationRequest) -> GeneratedContract:
        # PATTERN: Multi-step generation with validation loops
        system_prompt = self._build_system_prompt(request)

        # Step 1: Initial generation with OpenZeppelin patterns
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": request.specification}
        ]

        # CRITICAL: Use function calling for tool integration
        tools = [
            {
                "type": "function",
                "function": {
                    "name": "generate_solidity_code",
                    "description": "Generate Solidity contract code",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "contract_name": {"type": "string"},
                            "contract_code": {"type": "string"},
                            "security_features": {"type": "array", "items": {"type": "string"}}
                        }
                    }
                }
            }
        ]

        response = await self.client.chat.completions.create(
            model="gpt-4o-2024-11-20",  # From research
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )

        # PATTERN: Handle tool calls and validate results
        if response.choices[0].message.tool_calls:
            for tool_call in response.choices[0].message.tool_calls:
                result = await self._execute_tool(tool_call)
                # Validate generated contract compiles
                # Apply OpenZeppelin security patterns
                # Generate comprehensive explanation

        return GeneratedContract(...)

# Task 5: Audit Agent with Slither Integration
@audit_agent.tool
async def analyze_contract_security(
    ctx: RunContext[AgentDependencies],
    contract_code: str,
    contract_path: str
) -> AuditReport:
    """Comprehensive security analysis using Slither + LLM review."""

    # PATTERN: Use research/static-analysis/page4_slither_usage.md
    slither_cmd = [
        "slither", contract_path,
        "--json", "/tmp/slither_output.json",
        "--disable-color"
    ]

    # GOTCHA: Use Docker for consistent environment
    docker_cmd = [
        "docker", "run", "--rm",
        "-v", f"{os.getcwd()}:/contracts",
        "-v", "/tmp:/tmp",
        "trailofbits/eth-security-toolbox",
        *slither_cmd
    ]

    proc = await asyncio.create_subprocess_exec(
        *docker_cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await proc.communicate()

    # PATTERN: Parse Slither JSON output from research
    with open("/tmp/slither_output.json") as f:
        slither_results = json.load(f)

    # Convert Slither detections to AuditFinding objects
    findings = []
    for detector in slither_results.get("results", {}).get("detectors", []):
        finding = AuditFinding(
            id=f"slither-{detector['check']}",
            severity=_map_slither_severity(detector['impact']),
            title=detector['description'],
            description=detector['markdown'],
            location=_extract_location(detector['elements']),
            recommendation=_generate_recommendation(detector)
        )
        findings.append(finding)

    # PATTERN: LLM-based additional analysis
    llm_analysis = await self._perform_llm_security_review(contract_code)
    findings.extend(llm_analysis.findings)

    return AuditReport(
        contract_name=contract_name,
        findings=findings,
        overall_score=_calculate_security_score(findings),
        summary=_generate_audit_summary(findings),
        timestamp=datetime.now()
    )

# Task 8: FastAPI Backend with Agent Integration
@router.post("/api/v1/generate", response_model=GeneratedContract)
async def generate_contract(
    request: GenerationRequest,
    agent_service: GenerationService = Depends(get_generation_service)
) -> GeneratedContract:
    """Generate smart contract from natural language specification."""

    # PATTERN: Use research/fastapi/page8_dependencies.md for DI
    try:
        # Stream generation progress to client if needed
        result = await agent_service.generate_contract(request)

        # PATTERN: Save artifacts to /out/ directory
        output_path = f"/out/contracts/{result.contract_name}.sol"
        with open(output_path, "w") as f:
            f.write(result.solidity_code)

        return result

    except ValidationError as e:
        # PATTERN: Use research/fastapi/page21_error_handling.md
        raise HTTPException(
            status_code=422,
            detail=f"Validation error: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Generation failed: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Internal server error during contract generation"
        )

# Task 9: Next.js Frontend with Server Actions
// frontend/app/generate/page.tsx
'use client';

import { useState } from 'react';
import { generateContract } from '@/lib/api';
import CodeEditor from '@/components/editor/CodeEditor';
import { GenerationRequest, GeneratedContract } from '@/lib/types';

export default function GeneratePage() {
  const [request, setRequest] = useState<GenerationRequest>({
    specification: '',
    contract_type: 'custom',
    security_features: [],
    openzeppelin_integration: true,
    max_complexity: 5
  });

  const [result, setResult] = useState<GeneratedContract | null>(null);
  const [loading, setLoading] = useState(false);

  // PATTERN: Use Server Actions from research/nextjs/page7_server_actions.md
  async function handleGeneration() {
    setLoading(true);
    try {
      const generated = await generateContract(request);
      setResult(generated);

      // Auto-trigger audit analysis
      const auditResponse = await fetch('/api/audit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          contract_code: generated.solidity_code,
          contract_name: generated.contract_name
        })
      });

      // Handle audit results...

    } catch (error) {
      console.error('Generation failed:', error);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="container mx-auto p-6">
      {/* PATTERN: Tailwind CSS from research/nextjs/page9_tailwind.md */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="space-y-4">
          <h2 className="text-2xl font-bold">Contract Specification</h2>
          <textarea
            value={request.specification}
            onChange={(e) => setRequest({...request, specification: e.target.value})}
            placeholder="Describe your smart contract in natural language..."
            className="w-full h-40 p-4 border rounded-lg"
          />
          <button
            onClick={handleGeneration}
            disabled={loading}
            className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:opacity-50"
          >
            {loading ? 'Generating...' : 'Generate Contract'}
          </button>
        </div>

        <div className="space-y-4">
          <h2 className="text-2xl font-bold">Generated Contract</h2>
          {result && (
            <CodeEditor
              value={result.solidity_code}
              language="solidity"
              readOnly
              height="500px"
            />
          )}
        </div>
      </div>
    </div>
  );
}
```

### Integration Points
```yaml
ENVIRONMENT:
  - add to: .env
  - vars: |
      # OpenAI Configuration
      OPENAI_API_KEY=sk-...
      OPENAI_MODEL=gpt-4o-2024-11-20

      # Static Analysis Tools
      SLITHER_PATH=/usr/local/bin/slither
      SURYA_PATH=/usr/local/bin/surya

      # Output Configuration
      OUTPUT_DIR=./out
      CONTRACTS_DIR=./out/contracts
      AUDITS_DIR=./out/audits
      PATCHES_DIR=./out/patches

      # API Configuration
      API_HOST=0.0.0.0
      API_PORT=8000
      FRONTEND_URL=http://localhost:3000

      # Docker Configuration (optional)
      USE_DOCKER_TOOLS=true
      ETH_SECURITY_TOOLBOX_IMAGE=trailofbits/eth-security-toolbox

DATABASE:
  - Optional: SQLite for session management
  - Pattern: FastAPI + SQLAlchemy async from research/fastapi/page23_databases.md

STATIC_ANALYSIS:
  - Slither: JSON output format for programmatic parsing
  - Surya: PNG/SVG output for contract visualization
  - Docker integration for consistent tool environments

API_INTEGRATION:
  - OpenAI: Function calling for tool integration
  - Rate limiting: Exponential backoff for API calls
  - Error handling: Comprehensive exception management across all endpoints
```

## Validation Loop

### Level 1: Syntax & Style
```bash
# Run these FIRST - fix any errors before proceeding
ruff check chainsage/ api/ --fix     # Auto-fix Python style issues
mypy chainsage/ api/                 # Type checking
cd frontend && npm run lint          # Next.js linting
cd frontend && npm run type-check    # TypeScript checking

# Expected: No errors. If errors, READ the error and fix.
```

### Level 2: Unit Tests
```python
# tests/unit/test_generation_agent.py
async def test_contract_generation_from_specification():
    """Test generation agent creates valid Solidity from NL spec"""
    agent = GenerationAgent(mock_llm, tools)
    request = GenerationRequest(
        specification="Create an ERC20 token with minting and burning capabilities",
        contract_type=ContractType.ERC20,
        openzeppelin_integration=True
    )

    result = await agent.generate_contract(request)

    assert result.contract_name
    assert "pragma solidity" in result.solidity_code
    assert "import \"@openzeppelin/contracts" in result.solidity_code
    assert len(result.security_notes) > 0

async def test_audit_agent_detects_vulnerabilities():
    """Test audit agent identifies security issues"""
    vulnerable_contract = """
    contract Vulnerable {
        mapping(address => uint) balances;

        function withdraw() public {
            uint amount = balances[msg.sender];
            (bool success, ) = msg.sender.call{value: amount}("");
            require(success);
            balances[msg.sender] = 0; // Reentrancy vulnerability
        }
    }
    """

    agent = AuditAgent(mock_llm, static_analyzer)
    result = await agent.audit_contract(vulnerable_contract, "Vulnerable")

    assert len(result.findings) > 0
    assert any(f.severity == SecurityLevel.HIGH for f in result.findings)
    assert any("reentrancy" in f.description.lower() for f in result.findings)

# tests/integration/test_full_workflow.py
async def test_complete_generation_and_audit_workflow():
    """Test end-to-end workflow from specification to audited contract"""
    orchestrator = OrchestratorAgent(generation_agent, audit_agent)

    spec = "Create a governance token with voting delegation and timelock"
    result = await orchestrator.process_specification(spec)

    assert result.contract
    assert result.audit_report
    assert result.contract.contract_name
    assert len(result.audit_report.findings) >= 0  # May have no issues
    assert result.audit_report.overall_score > 0
```

```bash
# Run and iterate until passing:
pytest tests/ -v --cov=chainsage --cov=api --cov-report=term-missing

# If failing: Read error, understand root cause, fix code, re-run
```

### Level 3: Integration Test with Docker
```bash
# Start the full stack with Docker
docker-compose up --build

# Test contract generation via API
curl -X POST http://localhost:8000/api/v1/generate \
  -H "Content-Type: application/json" \
  -d '{
    "specification": "Create an ERC721 NFT contract with minting restrictions",
    "contract_type": "erc721",
    "openzeppelin_integration": true,
    "max_complexity": 7
  }'

# Expected: JSON response with generated contract
# Check: /out/contracts/ directory contains .sol file

# Test audit functionality
curl -X POST http://localhost:8000/api/v1/audit \
  -H "Content-Type: application/json" \
  -d '{
    "contract_code": "...",
    "contract_name": "TestContract"
  }'

# Expected: JSON response with audit findings
# Check: /out/audits/ directory contains .md report

# Test CLI interface
docker exec -it chainsage-api python -m chainsage.cli.main gen \
  --spec "Simple ERC20 token with 1000000 total supply" \
  --output /out/contracts/

# Expected: Contract generated and saved to output directory
```

### Level 4: Frontend Integration Test
```bash
# Start frontend development server
cd frontend && npm run dev

# Manual testing checklist:
# 1. Navigate to http://localhost:3000
# 2. Enter contract specification in text area
# 3. Click "Generate Contract" - should show loading state
# 4. Generated contract appears in code editor
# 5. Audit results display in audit panel
# 6. Download buttons work for contract and audit files
# 7. Error handling works for invalid specifications

# Expected: Full UI workflow completes without errors
```

## Final Validation Checklist
- [ ] All tests pass: `pytest tests/ -v`
- [ ] No linting errors: `ruff check . && cd frontend && npm run lint`
- [ ] No type errors: `mypy . && cd frontend && npm run type-check`
- [ ] Docker stack starts successfully: `docker-compose up`
- [ ] API endpoints return expected responses
- [ ] Generated contracts compile with Solidity compiler
- [ ] Slither analysis runs without crashes
- [ ] Static analysis detects known vulnerability patterns
- [ ] Frontend UI handles all user workflows
- [ ] CLI commands execute correctly
- [ ] Artifacts saved to /out/ directory with proper organization
- [ ] Error cases handled gracefully across all interfaces
- [ ] Environment variables properly configured
- [ ] Documentation complete with setup instructions

---

## Anti-Patterns to Avoid
- ❌ Don't hardcode OpenAI API keys or sensitive data
- ❌ Don't use sync functions in async agent/API context
- ❌ Don't skip OpenZeppelin security patterns in generated contracts
- ❌ Don't ignore Slither warnings without LLM review
- ❌ Don't generate contracts without proper license headers
- ❌ Don't skip input validation for user specifications
- ❌ Don't commit generated artifacts to version control
- ❌ Don't use outdated Solidity pragma versions
- ❌ Don't skip comprehensive error handling in production code
- ❌ Don't ignore gas optimization opportunities in generated contracts

## Confidence Score: 10/10

Maximum confidence due to:
- **Exhaustive research**: 110+ pages of official documentation across all technology stacks
- **Clear architectural patterns**: Multi-agent system with proven examples to follow
- **Comprehensive validation gates**: 4-level testing strategy from syntax to full integration
- **Production-ready foundations**: FastAPI, Next.js, OpenZeppelin, and OpenAI best practices
- **Security-first approach**: Integrated static analysis with LLM-powered security review
- **Complete workflow coverage**: From natural language input to audited contract output
- **Docker integration**: Consistent development and deployment environments
- **Modular architecture**: Clear separation of concerns enabling iterative development

The extensive research provides concrete implementation patterns, while the existing multi-agent PRP example offers proven architectural guidance. All critical technologies are thoroughly documented with production-ready patterns and security considerations.