"""
Automated patch generation system for ChainSage.

Generates targeted fixes for common vulnerabilities using git diff format
following security best practices and OpenZeppelin patterns.
"""

import re
import logging
from typing import Dict, List, Optional, Tuple, Set
from dataclasses import dataclass
from datetime import datetime

from ..agents.models import AuditFinding, PatchProposal, SecurityLevel

logger = logging.getLogger(__name__)


@dataclass
class PatchTemplate:
    """Template for generating security patches."""
    vulnerability_type: str
    pattern: str  # Regex pattern to match vulnerable code
    replacement: str  # Replacement code template
    description: str
    imports_needed: List[str]
    breaking_changes: bool
    gas_impact: int
    test_cases: List[str]


class PatchGenerator:
    """
    Automated patch generation for common security vulnerabilities.

    Follows research/openzeppelin patterns and security best practices
    to generate safe, tested patches for audit findings.
    """

    def __init__(self):
        self.patch_templates = self._initialize_patch_templates()
        self.safe_patterns = self._initialize_safe_patterns()

    def _initialize_patch_templates(self) -> Dict[str, PatchTemplate]:
        """Initialize patch templates for common vulnerabilities."""
        return {
            'reentrancy-eth': PatchTemplate(
                vulnerability_type='reentrancy-eth',
                pattern=r'(function\s+\w+[^{]*\{[^}]*)([\s\S]*?)(msg\.sender\.call\{value:\s*[^}]*\}[^;]*;)',
                replacement=r'\1\2nonReentrant\3',
                description='Add ReentrancyGuard modifier to prevent reentrancy attacks',
                imports_needed=['@openzeppelin/contracts/utils/ReentrancyGuard.sol'],
                breaking_changes=False,
                gas_impact=2300,
                test_cases=[
                    'Test normal function execution',
                    'Test reentrancy attack prevention',
                    'Test gas usage increase'
                ]
            ),
            'missing-zero-check': PatchTemplate(
                vulnerability_type='missing-zero-check',
                pattern=r'(\w+\s*=\s*)([^;]+)(;[^}]*address\s*\([^)]*\))',
                replacement=r'\1\2\3\n        require(\2 != address(0), "Invalid address");',
                description='Add zero address validation',
                imports_needed=[],
                breaking_changes=False,
                gas_impact=500,
                test_cases=[
                    'Test valid address acceptance',
                    'Test zero address rejection',
                    'Test error message'
                ]
            ),
            'arbitrary-send-eth': PatchTemplate(
                vulnerability_type='arbitrary-send-eth',
                pattern=r'(\w+\.call\{value:\s*[^}]*\}\([^)]*\))',
                replacement=r'// WARNING: Validate recipient before this call\n        require(isValidRecipient(\2), "Invalid recipient");\n        \1',
                description='Add recipient validation before ETH transfers',
                imports_needed=[],
                breaking_changes=True,
                gas_impact=1000,
                test_cases=[
                    'Test valid recipient',
                    'Test invalid recipient rejection',
                    'Test validation logic'
                ]
            ),
            'weak-prng': PatchTemplate(
                vulnerability_type='weak-prng',
                pattern=r'(uint\w*\s+\w+\s*=\s*)(uint\w*\([^)]*block\.(timestamp|number|difficulty)[^)]*\))',
                replacement=r'\1_getSecureRandom() // TODO: Implement secure randomness source',
                description='Replace weak PRNG with secure randomness placeholder',
                imports_needed=[],
                breaking_changes=True,
                gas_impact=5000,
                test_cases=[
                    'Test randomness quality',
                    'Test gas efficiency',
                    'Test integration with Chainlink VRF'
                ]
            ),
            'tx-origin': PatchTemplate(
                vulnerability_type='tx-origin',
                pattern=r'\btx\.origin\b',
                replacement='msg.sender',
                description='Replace tx.origin with msg.sender for authentication',
                imports_needed=[],
                breaking_changes=False,
                gas_impact=0,
                test_cases=[
                    'Test direct calls',
                    'Test contract-to-contract calls',
                    'Test access control behavior'
                ]
            ),
            'unprotected-upgrade': PatchTemplate(
                vulnerability_type='unprotected-upgrade',
                pattern=r'(function\s+_authorizeUpgrade\([^{]*\{)',
                replacement=r'\1\n        require(hasRole(UPGRADER_ROLE, msg.sender), "Unauthorized upgrade");',
                description='Add access control to upgrade functions',
                imports_needed=['@openzeppelin/contracts/access/AccessControl.sol'],
                breaking_changes=False,
                gas_impact=1500,
                test_cases=[
                    'Test authorized upgrade',
                    'Test unauthorized upgrade rejection',
                    'Test role management'
                ]
            )
        }

    def _initialize_safe_patterns(self) -> Set[str]:
        """Initialize patterns that are considered safe and shouldn't be modified."""
        return {
            'require(',
            'assert(',
            'revert(',
            'nonReentrant',
            'onlyOwner',
            'onlyRole',
            'whenNotPaused',
            'ReentrancyGuard',
            '_setupRole',
            'hasRole'
        }

    def generate_patches(
        self,
        contract_code: str,
        findings: List[AuditFinding],
        contract_name: str
    ) -> List[PatchProposal]:
        """
        Generate patch proposals for audit findings.

        Args:
            contract_code: Original contract source code
            findings: List of security findings to fix
            contract_name: Name of the contract being patched

        Returns:
            List of PatchProposal objects with fixes
        """
        patches = []

        for finding in findings:
            # Skip low severity findings unless they're easy fixes
            if finding.severity == SecurityLevel.LOW and finding.detector_type != 'slither':
                continue

            # Generate patches based on finding type
            patch = self._generate_patch_for_finding(contract_code, finding, contract_name)
            if patch:
                patches.append(patch)

        # Remove duplicate patches (same code changes)
        patches = self._deduplicate_patches(patches)

        # Validate patches don't conflict
        patches = self._validate_patch_compatibility(patches)

        return patches

    def _generate_patch_for_finding(
        self,
        contract_code: str,
        finding: AuditFinding,
        contract_name: str
    ) -> Optional[PatchProposal]:
        """Generate a single patch for a specific finding."""

        # Extract vulnerability type from finding ID
        vuln_type = self._extract_vulnerability_type(finding.id)
        if not vuln_type or vuln_type not in self.patch_templates:
            return self._generate_generic_patch(contract_code, finding, contract_name)

        template = self.patch_templates[vuln_type]

        # Apply template to generate patch
        patched_code = self._apply_patch_template(contract_code, template, finding)
        if not patched_code or patched_code == contract_code:
            return None

        # Generate git diff
        diff_content = self._generate_git_diff(contract_code, patched_code, contract_name)

        # Create patch proposal
        return PatchProposal(
            finding_id=finding.id,
            description=template.description,
            diff_content=diff_content,
            explanation=self._generate_patch_explanation(template, finding),
            risk_assessment=self._assess_patch_risk(template, finding),
            estimated_gas_impact=template.gas_impact,
            test_cases=template.test_cases,
            breaking_changes=template.breaking_changes
        )

    def _extract_vulnerability_type(self, finding_id: str) -> Optional[str]:
        """Extract vulnerability type from finding ID."""
        # Expected format: "slither-{vuln_type}-{index}" or "{tool}-{vuln_type}"
        parts = finding_id.split('-')
        if len(parts) >= 2:
            # Return the main vulnerability type (skip tool prefix and index suffix)
            if len(parts) >= 3:
                return '-'.join(parts[1:-1])  # Join middle parts for complex types
            else:
                return parts[1]
        return None

    def _apply_patch_template(
        self,
        contract_code: str,
        template: PatchTemplate,
        finding: AuditFinding
    ) -> Optional[str]:
        """Apply patch template to contract code."""
        try:
            # Check if code needs the suggested imports
            patched_code = contract_code

            # Add required imports
            for import_path in template.imports_needed:
                if f'import "{import_path}";' not in patched_code:
                    patched_code = self._add_import(patched_code, import_path)

            # Add required inheritance for ReentrancyGuard
            if 'ReentrancyGuard' in template.imports_needed[0] if template.imports_needed else False:
                if 'ReentrancyGuard' not in patched_code:
                    patched_code = self._add_inheritance(patched_code, 'ReentrancyGuard')

            # Apply pattern-based fixes
            if template.vulnerability_type == 'reentrancy-eth':
                patched_code = self._fix_reentrancy(patched_code, finding)
            elif template.vulnerability_type == 'missing-zero-check':
                patched_code = self._fix_zero_address_check(patched_code, finding)
            elif template.vulnerability_type == 'tx-origin':
                patched_code = self._fix_tx_origin(patched_code)
            elif template.vulnerability_type == 'weak-prng':
                patched_code = self._fix_weak_prng(patched_code, finding)
            else:
                # Generic pattern replacement
                patched_code = re.sub(template.pattern, template.replacement, patched_code)

            return patched_code if patched_code != contract_code else None

        except Exception as e:
            logger.error(f"Failed to apply patch template: {e}")
            return None

    def _fix_reentrancy(self, contract_code: str, finding: AuditFinding) -> str:
        """Fix reentrancy vulnerabilities by adding nonReentrant modifier."""

        # Find functions with external calls
        function_pattern = r'function\s+(\w+)\s*\([^)]*\)\s*([^{]*?)\s*\{'
        functions = re.finditer(function_pattern, contract_code)

        patched_code = contract_code

        for match in functions:
            func_name = match.group(1)
            modifiers = match.group(2)
            full_func_def = match.group(0)

            # Check if this function contains external calls and might be vulnerable
            func_start = match.end()
            func_body = self._extract_function_body(contract_code, func_start)

            if ('call{value:' in func_body or '.transfer(' in func_body or '.send(' in func_body):
                # Add nonReentrant modifier if not already present
                if 'nonReentrant' not in modifiers:
                    new_modifiers = modifiers.strip() + ' nonReentrant'
                    new_func_def = full_func_def.replace(modifiers, new_modifiers)
                    patched_code = patched_code.replace(full_func_def, new_func_def)

        return patched_code

    def _fix_zero_address_check(self, contract_code: str, finding: AuditFinding) -> str:
        """Add zero address checks to address assignments."""

        # Pattern to find address assignments
        assignment_pattern = r'(\w+\s*=\s*)([^;]+address\s*\([^)]+\))'
        matches = re.finditer(assignment_pattern, contract_code)

        patched_code = contract_code

        for match in matches:
            full_assignment = match.group(0)
            var_name = match.group(1).strip().rstrip('=').strip()
            address_expr = match.group(2).strip()

            # Add zero check after assignment
            zero_check = f'\n        require({address_expr} != address(0), "Invalid address: {var_name}");'
            new_assignment = full_assignment + zero_check

            patched_code = patched_code.replace(full_assignment, new_assignment)

        return patched_code

    def _fix_tx_origin(self, contract_code: str) -> str:
        """Replace tx.origin with msg.sender."""
        return re.sub(r'\btx\.origin\b', 'msg.sender', contract_code)

    def _fix_weak_prng(self, contract_code: str, finding: AuditFinding) -> str:
        """Replace weak PRNG with secure randomness placeholder."""

        # Pattern for block-based randomness
        weak_patterns = [
            r'uint\w*\s*\([^)]*block\.(timestamp|number|difficulty)[^)]*\)',
            r'keccak256\s*\([^)]*block\.(timestamp|number|difficulty)[^)]*\)',
            r'blockhash\s*\([^)]*\)'
        ]

        patched_code = contract_code

        for pattern in weak_patterns:
            # Replace with secure randomness placeholder
            replacement = '/* TODO: Implement secure randomness (e.g., Chainlink VRF) */ _getSecureRandom()'
            patched_code = re.sub(pattern, replacement, patched_code)

        # Add placeholder function if not exists
        if '_getSecureRandom()' in patched_code and 'function _getSecureRandom()' not in patched_code:
            secure_random_func = '''
    /**
     * @dev Placeholder for secure randomness implementation
     * TODO: Implement using Chainlink VRF or similar secure source
     */
    function _getSecureRandom() internal view returns (uint256) {
        revert("Secure randomness not implemented");
    }'''

            # Add before the last closing brace
            last_brace = patched_code.rfind('}')
            if last_brace != -1:
                patched_code = patched_code[:last_brace] + secure_random_func + '\n' + patched_code[last_brace:]

        return patched_code

    def _generate_generic_patch(
        self,
        contract_code: str,
        finding: AuditFinding,
        contract_name: str
    ) -> Optional[PatchProposal]:
        """Generate a generic patch proposal for findings without specific templates."""

        # Create a comment-based patch for manual review
        comment_patch = f'''
        // SECURITY REVIEW REQUIRED: {finding.title}
        // Severity: {finding.severity.value}
        // Description: {finding.description}
        // Recommendation: {finding.recommendation}
        // Location: {finding.location}
        '''

        diff_content = f'''--- a/{contract_name}.sol
+++ b/{contract_name}.sol
@@ -1,3 +1,8 @@
+{comment_patch}
 // Original code continues here...'''

        return PatchProposal(
            finding_id=finding.id,
            description=f"Manual review required for: {finding.title}",
            diff_content=diff_content,
            explanation=f"This finding requires manual review and custom implementation. {finding.recommendation}",
            risk_assessment="Low risk - adds documentation comments for manual review",
            estimated_gas_impact=0,
            test_cases=[
                "Review finding details",
                "Implement appropriate fix",
                "Test fix thoroughly"
            ],
            breaking_changes=False
        )

    def _add_import(self, contract_code: str, import_path: str) -> str:
        """Add import statement to contract."""
        import_statement = f'import "{import_path}";'

        if import_statement in contract_code:
            return contract_code

        # Find insertion point after other imports or pragma
        lines = contract_code.split('\n')
        insert_idx = 0

        for i, line in enumerate(lines):
            if line.strip().startswith(('pragma', 'import')):
                insert_idx = i + 1

        lines.insert(insert_idx, import_statement)
        return '\n'.join(lines)

    def _add_inheritance(self, contract_code: str, inheritance: str) -> str:
        """Add inheritance to contract definition."""
        pattern = r'(contract\s+\w+)(\s+is\s+[^{]+)?(\s*{)'

        def add_inheritance(match):
            contract_def = match.group(1)
            existing = match.group(2) or ""
            brace = match.group(3)

            if inheritance not in existing:
                if existing:
                    new_inheritance = f"{existing}, {inheritance}"
                else:
                    new_inheritance = f" is {inheritance}"
                return f"{contract_def}{new_inheritance}{brace}"
            return match.group(0)

        return re.sub(pattern, add_inheritance, contract_code)

    def _extract_function_body(self, contract_code: str, start_pos: int) -> str:
        """Extract function body from contract code starting at position."""
        brace_count = 0
        i = start_pos

        while i < len(contract_code):
            if contract_code[i] == '{':
                brace_count += 1
            elif contract_code[i] == '}':
                brace_count -= 1
                if brace_count == 0:
                    return contract_code[start_pos:i]
            i += 1

        return contract_code[start_pos:]

    def _generate_git_diff(self, original: str, patched: str, filename: str) -> str:
        """Generate git diff format for patch."""
        original_lines = original.split('\n')
        patched_lines = patched.split('\n')

        # Simple diff implementation
        diff_lines = [
            f'--- a/{filename}.sol',
            f'+++ b/{filename}.sol',
            '@@ -1,' + str(len(original_lines)) + ' +1,' + str(len(patched_lines)) + ' @@'
        ]

        # Add changed lines (simplified)
        for i, (orig, patch) in enumerate(zip(original_lines, patched_lines)):
            if orig != patch:
                diff_lines.append(f'-{orig}')
                diff_lines.append(f'+{patch}')
            else:
                diff_lines.append(f' {orig}')

        # Add new lines if patched is longer
        if len(patched_lines) > len(original_lines):
            for line in patched_lines[len(original_lines):]:
                diff_lines.append(f'+{line}')

        return '\n'.join(diff_lines)

    def _generate_patch_explanation(
        self,
        template: PatchTemplate,
        finding: AuditFinding
    ) -> str:
        """Generate detailed explanation of the patch."""
        explanation = f"**Fix for {finding.title}**\n\n"
        explanation += f"**Vulnerability**: {template.vulnerability_type}\n"
        explanation += f"**Description**: {template.description}\n\n"
        explanation += f"**Changes Made**:\n"

        if template.imports_needed:
            explanation += f"- Added imports: {', '.join(template.imports_needed)}\n"

        explanation += f"- Applied security pattern to fix {template.vulnerability_type}\n"

        if template.gas_impact > 0:
            explanation += f"- Estimated gas increase: {template.gas_impact} gas\n"

        explanation += f"\n**Original Finding**: {finding.description}\n"
        explanation += f"**Recommendation**: {finding.recommendation}\n"

        return explanation

    def _assess_patch_risk(self, template: PatchTemplate, finding: AuditFinding) -> str:
        """Assess the risk of applying the patch."""
        if template.breaking_changes:
            risk = "MEDIUM RISK: This patch may introduce breaking changes. "
            risk += "Thorough testing required before deployment."
        elif template.gas_impact > 5000:
            risk = "LOW-MEDIUM RISK: Significant gas cost increase. "
            risk += "Review gas optimization opportunities."
        else:
            risk = "LOW RISK: Safe security improvement with minimal side effects."

        risk += f"\n\nConfidence: {finding.confidence * 100:.0f}%"
        risk += f"\nOriginal Severity: {finding.severity.value}"

        return risk

    def _deduplicate_patches(self, patches: List[PatchProposal]) -> List[PatchProposal]:
        """Remove duplicate patches with same changes."""
        unique_patches = []
        seen_diffs = set()

        for patch in patches:
            if patch.diff_content not in seen_diffs:
                unique_patches.append(patch)
                seen_diffs.add(patch.diff_content)

        return unique_patches

    def _validate_patch_compatibility(self, patches: List[PatchProposal]) -> List[PatchProposal]:
        """Validate that patches don't conflict with each other."""
        # For now, return all patches - more sophisticated conflict detection could be added
        return patches


if __name__ == "__main__":
    # Test patch generation
    generator = PatchGenerator()

    test_contract = '''
    pragma solidity ^0.8.19;

    contract TestContract {
        mapping(address => uint256) public balances;
        address public owner;

        function withdraw() public {
            uint amount = balances[msg.sender];
            (bool success, ) = msg.sender.call{value: amount}("");
            require(success);
            balances[msg.sender] = 0;
        }

        function setOwner(address newOwner) public {
            owner = newOwner;
        }

        function randomize() public view returns (uint256) {
            return uint256(keccak256(abi.encode(block.timestamp, block.difficulty)));
        }
    }
    '''

    from ..agents.models import AuditFinding, SecurityLevel

    # Create test findings
    findings = [
        AuditFinding(
            id="slither-reentrancy-eth-0",
            severity=SecurityLevel.HIGH,
            title="Reentrancy vulnerability",
            description="Function vulnerable to reentrancy attack",
            location="withdraw function",
            recommendation="Use ReentrancyGuard modifier",
            detector_type="slither"
        ),
        AuditFinding(
            id="slither-missing-zero-check-1",
            severity=SecurityLevel.MEDIUM,
            title="Missing zero address validation",
            description="Address parameter not validated",
            location="setOwner function",
            recommendation="Add zero address check",
            detector_type="slither"
        )
    ]

    patches = generator.generate_patches(test_contract, findings, "TestContract")

    print("✅ Patch generation test completed")
    print(f"📋 Generated patches: {len(patches)}")
    for patch in patches:
        print(f"🔧 Patch for {patch.finding_id}: {patch.description}")
        print(f"   Breaking changes: {patch.breaking_changes}")
        print(f"   Gas impact: {patch.estimated_gas_impact}")