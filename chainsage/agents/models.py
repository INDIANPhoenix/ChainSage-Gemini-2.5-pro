"""
Pydantic models for ChainSage agent system.

Defines all data structures used throughout the application including
contract generation, audit reports, and agent communication.
"""

from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import List, Optional, Dict, Any, Union
from pydantic import BaseModel, Field, validator, root_validator


class ContractType(str, Enum):
    """Types of smart contracts that can be generated."""
    ERC20 = "erc20"
    ERC721 = "erc721"
    ERC1155 = "erc1155"
    GOVERNANCE = "governance"
    CUSTOM = "custom"


class SecurityLevel(str, Enum):
    """Security finding severity levels."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class AgentStatus(str, Enum):
    """Agent execution status."""
    IDLE = "idle"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class GenerationRequest(BaseModel):
    """Request model for contract generation."""
    specification: str = Field(
        ...,
        description="Natural language contract specification",
        min_length=10,
        max_length=5000
    )
    contract_type: ContractType = Field(
        ContractType.CUSTOM,
        description="Type of contract to generate"
    )
    security_features: List[str] = Field(
        default_factory=list,
        description="Required security features (e.g., 'pausable', 'burnable')"
    )
    openzeppelin_integration: bool = Field(
        True,
        description="Use OpenZeppelin patterns and imports"
    )
    max_complexity: int = Field(
        5,
        ge=1,
        le=10,
        description="Complexity level 1-10 (affects contract sophistication)"
    )
    include_tests: bool = Field(
        True,
        description="Generate accompanying test files"
    )
    solidity_version: str = Field(
        "^0.8.19",
        description="Solidity version pragma"
    )

    @validator('security_features')
    def validate_security_features(cls, v):
        """Validate security feature requests."""
        valid_features = {
            'pausable', 'burnable', 'mintable', 'ownable', 'access_control',
            'reentrancy_guard', 'cap', 'snapshot', 'votes', 'timelock'
        }
        invalid = set(v) - valid_features
        if invalid:
            raise ValueError(f"Invalid security features: {invalid}")
        return v


class GeneratedContract(BaseModel):
    """Generated smart contract result."""
    contract_name: str = Field(..., description="Name of the generated contract")
    solidity_code: str = Field(..., description="Complete Solidity source code")
    explanation: str = Field(..., description="Human-readable explanation of the contract")
    security_notes: List[str] = Field(
        default_factory=list,
        description="Important security considerations"
    )
    dependencies: List[str] = Field(
        default_factory=list,
        description="OpenZeppelin and other dependencies"
    )
    estimated_gas: Optional[int] = Field(
        None,
        description="Estimated gas cost for deployment"
    )
    functions: List[Dict[str, Any]] = Field(
        default_factory=list,
        description="List of contract functions with descriptions"
    )
    events: List[Dict[str, Any]] = Field(
        default_factory=list,
        description="List of contract events"
    )
    generated_at: datetime = Field(
        default_factory=datetime.now,
        description="Generation timestamp"
    )

    @validator('solidity_code')
    def validate_solidity_syntax(cls, v):
        """Basic Solidity syntax validation."""
        if not v.strip().startswith('pragma solidity'):
            raise ValueError("Contract must start with pragma statement")
        if 'contract ' not in v:
            raise ValueError("Must contain at least one contract definition")
        return v


class AuditFinding(BaseModel):
    """Individual audit finding/vulnerability."""
    id: str = Field(..., description="Unique finding identifier")
    severity: SecurityLevel = Field(..., description="Severity level")
    title: str = Field(..., description="Brief finding title")
    description: str = Field(..., description="Detailed description")
    location: str = Field(..., description="File:line or function name")
    recommendation: str = Field(..., description="Fix recommendation")
    cve_references: List[str] = Field(
        default_factory=list,
        description="Related CVE identifiers"
    )
    detector_type: str = Field(
        "llm",
        description="Detection method (slither, surya, llm)"
    )
    confidence: float = Field(
        1.0,
        ge=0.0,
        le=1.0,
        description="Finding confidence (0.0-1.0)"
    )
    code_snippet: Optional[str] = Field(
        None,
        description="Relevant code snippet"
    )


class AuditReport(BaseModel):
    """Complete audit report for a contract."""
    contract_name: str = Field(..., description="Name of audited contract")
    findings: List[AuditFinding] = Field(
        default_factory=list,
        description="List of audit findings"
    )
    overall_score: int = Field(
        ...,
        ge=0,
        le=100,
        description="Overall security score (0-100)"
    )
    summary: str = Field(..., description="Executive summary")
    timestamp: datetime = Field(
        default_factory=datetime.now,
        description="Audit timestamp"
    )
    tools_used: List[str] = Field(
        default_factory=list,
        description="Analysis tools used (slither, surya, llm)"
    )
    gas_analysis: Optional[Dict[str, Any]] = Field(
        None,
        description="Gas usage analysis"
    )
    recommendations: List[str] = Field(
        default_factory=list,
        description="High-level recommendations"
    )

    @validator('findings')
    def sort_findings_by_severity(cls, v):
        """Sort findings by severity (critical first)."""
        severity_order = {
            SecurityLevel.CRITICAL: 0,
            SecurityLevel.HIGH: 1,
            SecurityLevel.MEDIUM: 2,
            SecurityLevel.LOW: 3
        }
        return sorted(v, key=lambda x: severity_order.get(x.severity, 4))

    @root_validator
    def calculate_score_from_findings(cls, values):
        """Calculate overall score based on findings."""
        findings = values.get('findings', [])
        if not findings:
            values['overall_score'] = 100
            return values

        # Scoring algorithm based on severity
        score = 100
        for finding in findings:
            if finding.severity == SecurityLevel.CRITICAL:
                score -= 25
            elif finding.severity == SecurityLevel.HIGH:
                score -= 15
            elif finding.severity == SecurityLevel.MEDIUM:
                score -= 8
            elif finding.severity == SecurityLevel.LOW:
                score -= 3

        values['overall_score'] = max(0, score)
        return values


class PatchProposal(BaseModel):
    """Proposed fix for a security finding."""
    finding_id: str = Field(..., description="Related finding ID")
    description: str = Field(..., description="Patch description")
    diff_content: str = Field(..., description="Git diff format patch")
    explanation: str = Field(..., description="Detailed explanation of changes")
    risk_assessment: str = Field(..., description="Risk analysis of applying patch")
    estimated_gas_impact: Optional[int] = Field(
        None,
        description="Estimated gas cost change"
    )
    test_cases: List[str] = Field(
        default_factory=list,
        description="Suggested test cases for the fix"
    )
    breaking_changes: bool = Field(
        False,
        description="Whether patch introduces breaking changes"
    )


class WorkflowState(BaseModel):
    """State of a contract generation and audit workflow."""
    session_id: str = Field(..., description="Unique session identifier")
    status: AgentStatus = Field(AgentStatus.IDLE, description="Current status")
    request: Optional[GenerationRequest] = Field(None, description="Original request")
    generated_contract: Optional[GeneratedContract] = Field(None, description="Generated contract")
    audit_report: Optional[AuditReport] = Field(None, description="Audit report")
    patches: List[PatchProposal] = Field(default_factory=list, description="Patch proposals")
    error_message: Optional[str] = Field(None, description="Error message if failed")
    started_at: datetime = Field(default_factory=datetime.now, description="Start timestamp")
    completed_at: Optional[datetime] = Field(None, description="Completion timestamp")
    agent_interactions: List[Dict[str, Any]] = Field(
        default_factory=list,
        description="Log of agent interactions"
    )


class AgentMessage(BaseModel):
    """Message structure for agent communication."""
    role: str = Field(..., description="Message role (system, user, assistant, tool)")
    content: str = Field(..., description="Message content")
    tool_calls: Optional[List[Dict[str, Any]]] = Field(
        None,
        description="Tool calls made by the agent"
    )
    tool_call_id: Optional[str] = Field(
        None,
        description="ID of tool call being responded to"
    )
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Additional metadata"
    )
    timestamp: datetime = Field(
        default_factory=datetime.now,
        description="Message timestamp"
    )


class AgentContext(BaseModel):
    """Context passed between agents."""
    session_id: str = Field(..., description="Session identifier")
    workflow_state: WorkflowState = Field(..., description="Current workflow state")
    conversation_history: List[AgentMessage] = Field(
        default_factory=list,
        description="Conversation history"
    )
    shared_data: Dict[str, Any] = Field(
        default_factory=dict,
        description="Shared data between agents"
    )
    output_paths: Dict[str, Path] = Field(
        default_factory=dict,
        description="Output file paths"
    )


class ToolResult(BaseModel):
    """Result from tool execution."""
    tool_name: str = Field(..., description="Name of executed tool")
    success: bool = Field(..., description="Whether execution was successful")
    result: Any = Field(..., description="Tool execution result")
    error_message: Optional[str] = Field(None, description="Error message if failed")
    execution_time: float = Field(..., description="Execution time in seconds")
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Additional metadata"
    )


class StaticAnalysisResult(BaseModel):
    """Result from static analysis tools."""
    tool_name: str = Field(..., description="Analysis tool used")
    contract_name: str = Field(..., description="Analyzed contract name")
    findings: List[AuditFinding] = Field(
        default_factory=list,
        description="Static analysis findings"
    )
    raw_output: str = Field("", description="Raw tool output")
    execution_successful: bool = Field(True, description="Whether analysis completed")
    error_message: Optional[str] = Field(None, description="Error message if failed")
    analysis_duration: float = Field(0.0, description="Analysis duration in seconds")


# Export commonly used models
__all__ = [
    'ContractType',
    'SecurityLevel',
    'AgentStatus',
    'GenerationRequest',
    'GeneratedContract',
    'AuditFinding',
    'AuditReport',
    'PatchProposal',
    'WorkflowState',
    'AgentMessage',
    'AgentContext',
    'ToolResult',
    'StaticAnalysisResult'
]