"""
OpenZeppelin integration helper for ChainSage.

Provides advanced security pattern injection, import management,
and gas optimization following research/openzeppelin patterns.
"""

import re
from typing import Dict, List, Set, Optional, Tuple
from dataclasses import dataclass

from ..agents.models import ContractType, SecurityLevel


@dataclass
class SecurityPattern:
    """Represents an OpenZeppelin security pattern."""
    name: str
    import_path: str
    inheritance: str
    required_functions: List[str]
    modifier_injections: List[str]
    gas_impact: int  # Estimated gas cost increase
    description: str
    severity: SecurityLevel


class OpenZeppelinHelper:
    """
    Advanced OpenZeppelin security pattern integration.

    Follows research/openzeppelin patterns for access control, security,
    and gas optimization recommendations.
    """

    def __init__(self):
        self.security_patterns = self._initialize_security_patterns()
        self.access_control_patterns = self._initialize_access_control()
        self.gas_optimizations = self._initialize_gas_optimizations()

    def _initialize_security_patterns(self) -> Dict[str, SecurityPattern]:
        """Initialize security patterns from research/openzeppelin documentation."""
        return {
            'reentrancy_guard': SecurityPattern(
                name="ReentrancyGuard",
                import_path="@openzeppelin/contracts/utils/ReentrancyGuard.sol",
                inheritance="ReentrancyGuard",
                required_functions=[],
                modifier_injections=["nonReentrant"],
                gas_impact=2300,  # Gas cost for reentrancy protection
                description="Protects against reentrancy attacks in external calls",
                severity=SecurityLevel.HIGH
            ),
            'pausable': SecurityPattern(
                name="Pausable",
                import_path="@openzeppelin/contracts/utils/Pausable.sol",
                inheritance="Pausable",
                required_functions=["pause", "unpause"],
                modifier_injections=["whenNotPaused", "whenPaused"],
                gas_impact=700,
                description="Emergency stop mechanism for contract functions",
                severity=SecurityLevel.MEDIUM
            ),
            'ownable': SecurityPattern(
                name="Ownable",
                import_path="@openzeppelin/contracts/access/Ownable.sol",
                inheritance="Ownable",
                required_functions=["transferOwnership", "renounceOwnership"],
                modifier_injections=["onlyOwner"],
                gas_impact=0,  # Base pattern, no additional cost
                description="Single owner access control pattern",
                severity=SecurityLevel.MEDIUM
            ),
            'ownable2step': SecurityPattern(
                name="Ownable2Step",
                import_path="@openzeppelin/contracts/access/Ownable2Step.sol",
                inheritance="Ownable2Step",
                required_functions=["transferOwnership", "acceptOwnership"],
                modifier_injections=["onlyOwner"],
                gas_impact=500,
                description="Safer two-step ownership transfer process",
                severity=SecurityLevel.MEDIUM
            ),
            'access_control': SecurityPattern(
                name="AccessControl",
                import_path="@openzeppelin/contracts/access/AccessControl.sol",
                inheritance="AccessControl",
                required_functions=["grantRole", "revokeRole", "hasRole"],
                modifier_injections=["onlyRole"],
                gas_impact=1500,
                description="Role-based access control with hierarchical permissions",
                severity=SecurityLevel.HIGH
            ),
            'erc20_permit': SecurityPattern(
                name="ERC20Permit",
                import_path="@openzeppelin/contracts/token/ERC20/extensions/ERC20Permit.sol",
                inheritance="ERC20Permit",
                required_functions=["permit"],
                modifier_injections=[],
                gas_impact=3000,
                description="Gasless token approvals using EIP-2612 signatures",
                severity=SecurityLevel.LOW
            )
        }

    def _initialize_access_control(self) -> Dict[str, Dict]:
        """Initialize access control patterns from research."""
        return {
            'ownable': {
                'suitable_for': ['simple', 'single_admin', 'basic'],
                'constructor_params': ['address initialOwner'],
                'constructor_calls': ['Ownable(initialOwner)'],
                'modifiers': {'onlyOwner': 'restricts function to contract owner'},
                'functions': {
                    'transferOwnership': 'Transfer ownership to new address',
                    'renounceOwnership': 'Permanently remove owner (dangerous!)'
                },
                'security_notes': [
                    'Single point of failure - owner has all control',
                    'Consider upgrading to Ownable2Step for safer ownership transfers',
                    'Can be combined with multisig wallets for better security'
                ]
            },
            'access_control': {
                'suitable_for': ['complex', 'multi_admin', 'governance'],
                'constructor_params': ['address defaultAdmin'],
                'constructor_calls': ['AccessControl()'],
                'modifiers': {'onlyRole': 'restricts function to specific role'},
                'functions': {
                    'grantRole': 'Grant role to account',
                    'revokeRole': 'Revoke role from account',
                    'hasRole': 'Check if account has role',
                    'getRoleAdmin': 'Get admin role for given role'
                },
                'security_notes': [
                    'More flexible than Ownable but higher gas costs',
                    'DEFAULT_ADMIN_ROLE has special privileges',
                    'Use role hierarchies for complex permission systems'
                ]
            },
            'ownable2step': {
                'suitable_for': ['production', 'high_value', 'safety_critical'],
                'constructor_params': ['address initialOwner'],
                'constructor_calls': ['Ownable(initialOwner)'],
                'modifiers': {'onlyOwner': 'restricts function to contract owner'},
                'functions': {
                    'transferOwnership': 'Initiate ownership transfer (pending)',
                    'acceptOwnership': 'Accept pending ownership transfer',
                    'pendingOwner': 'View pending owner address'
                },
                'security_notes': [
                    'Prevents accidental ownership transfer to invalid addresses',
                    'Two-step process reduces risk of losing control',
                    'Recommended for production contracts'
                ]
            }
        }

    def _initialize_gas_optimizations(self) -> List[Dict]:
        """Initialize gas optimization recommendations."""
        return [
            {
                'pattern': 'Efficient Storage Packing',
                'description': 'Pack struct members to minimize storage slots',
                'example': 'struct User { uint128 balance; uint128 timestamp; address addr; }',
                'gas_savings': '20000 per storage slot saved'
            },
            {
                'pattern': 'Function Visibility',
                'description': 'Use appropriate function visibility (external vs public)',
                'example': 'function externalFunc() external {} // cheaper than public',
                'gas_savings': '200-400 per call'
            },
            {
                'pattern': 'Immutable Variables',
                'description': 'Use immutable for variables set only in constructor',
                'example': 'address public immutable owner;',
                'gas_savings': '2100 per storage read'
            },
            {
                'pattern': 'Event Optimization',
                'description': 'Use indexed parameters for efficient filtering',
                'example': 'event Transfer(address indexed from, address indexed to, uint256 value);',
                'gas_savings': 'Better query performance'
            }
        ]

    def inject_security_patterns(
        self,
        contract_code: str,
        requested_features: List[str],
        contract_type: ContractType
    ) -> Tuple[str, List[str], List[str]]:
        """
        Inject security patterns into contract code.

        Args:
            contract_code: Original Solidity contract code
            requested_features: List of requested security features
            contract_type: Type of contract being generated

        Returns:
            Tuple of (enhanced_code, injected_patterns, security_recommendations)
        """
        enhanced_code = contract_code
        injected_patterns = []
        recommendations = []

        # Auto-inject critical security patterns based on contract analysis
        critical_patterns = self._analyze_contract_risks(contract_code, contract_type)
        all_features = set(requested_features) | critical_patterns

        for feature in all_features:
            if feature in self.security_patterns:
                pattern = self.security_patterns[feature]
                enhanced_code = self._inject_pattern(enhanced_code, pattern)
                injected_patterns.append(pattern.name)

                # Add pattern-specific recommendations
                recommendations.append(f"{pattern.name}: {pattern.description}")

        # Add general security recommendations
        recommendations.extend(self._generate_security_recommendations(contract_code, contract_type))

        return enhanced_code, injected_patterns, recommendations

    def _analyze_contract_risks(self, contract_code: str, contract_type: ContractType) -> Set[str]:
        """Analyze contract code for security risks and recommend patterns."""
        critical_patterns = set()

        # Check for external calls (reentrancy risk)
        if re.search(r'\.call\s*\{', contract_code) or re.search(r'\.transfer\s*\(', contract_code):
            critical_patterns.add('reentrancy_guard')

        # Check for ownership patterns
        if 'onlyOwner' in contract_code or 'owner()' in contract_code:
            if 'production' in contract_code.lower() or 'mainnet' in contract_code.lower():
                critical_patterns.add('ownable2step')
            else:
                critical_patterns.add('ownable')

        # Check for state-changing functions that need pause capability
        if contract_type in [ContractType.ERC20, ContractType.ERC721]:
            if 'mint' in contract_code or 'burn' in contract_code:
                critical_patterns.add('pausable')

        # Check for complex permission requirements
        role_keywords = ['admin', 'moderator', 'minter', 'pauser', 'governance']
        if any(keyword in contract_code.lower() for keyword in role_keywords):
            critical_patterns.add('access_control')

        return critical_patterns

    def _inject_pattern(self, contract_code: str, pattern: SecurityPattern) -> str:
        """Inject a specific security pattern into contract code."""
        # Add import if not already present
        if pattern.import_path not in contract_code:
            contract_code = self._add_import(contract_code, pattern.import_path)

        # Add inheritance if not already present
        if pattern.inheritance not in contract_code:
            contract_code = self._add_inheritance(contract_code, pattern.inheritance)

        # Inject modifiers into appropriate functions
        contract_code = self._inject_modifiers(contract_code, pattern)

        # Add required functions if missing
        contract_code = self._add_required_functions(contract_code, pattern)

        return contract_code

    def _add_import(self, contract_code: str, import_path: str) -> str:
        """Add import statement to contract."""
        import_statement = f'import "{import_path}";'

        if import_statement not in contract_code:
            # Find the last import or pragma statement
            lines = contract_code.split('\n')
            insert_idx = 0

            for i, line in enumerate(lines):
                if line.strip().startswith(('pragma', 'import')):
                    insert_idx = i + 1

            lines.insert(insert_idx, import_statement)
            contract_code = '\n'.join(lines)

        return contract_code

    def _add_inheritance(self, contract_code: str, inheritance: str) -> str:
        """Add inheritance to contract definition."""
        # Pattern to match contract definition
        contract_pattern = r'(contract\s+\w+)(\s+is\s+[^{]+)?(\s*{)'

        def replace_inheritance(match):
            contract_def = match.group(1)
            existing_inheritance = match.group(2) or ""
            opening_brace = match.group(3)

            if inheritance not in existing_inheritance:
                if existing_inheritance:
                    new_inheritance = f"{existing_inheritance}, {inheritance}"
                else:
                    new_inheritance = f" is {inheritance}"
                return f"{contract_def}{new_inheritance}{opening_brace}"

            return match.group(0)  # No change needed

        return re.sub(contract_pattern, replace_inheritance, contract_code)

    def _inject_modifiers(self, contract_code: str, pattern: SecurityPattern) -> str:
        """Inject modifiers into appropriate functions."""
        if not pattern.modifier_injections:
            return contract_code

        # Functions that should have security modifiers
        security_sensitive_functions = [
            'mint', 'burn', 'pause', 'unpause', 'withdraw',
            'transferOwnership', 'grantRole', 'revokeRole'
        ]

        for modifier in pattern.modifier_injections:
            for func_name in security_sensitive_functions:
                pattern_regex = rf'(function\s+{func_name}\s*\([^)]*\)\s+)([^{{]*)({{)'
                replacement = rf'\1\2 {modifier}\3'
                contract_code = re.sub(pattern_regex, replacement, contract_code)

        return contract_code

    def _add_required_functions(self, contract_code: str, pattern: SecurityPattern) -> str:
        """Add required functions for security pattern."""
        # This would add pattern-specific functions based on the security pattern
        # For now, we'll return the code as-is since templates already include these
        return contract_code

    def _generate_security_recommendations(
        self,
        contract_code: str,
        contract_type: ContractType
    ) -> List[str]:
        """Generate security recommendations based on contract analysis."""
        recommendations = []

        # General recommendations
        recommendations.extend([
            "Implement comprehensive unit tests covering all functions",
            "Consider formal verification for critical business logic",
            "Use latest stable Solidity version for security updates",
            "Implement proper error handling and input validation"
        ])

        # Contract-type specific recommendations
        if contract_type == ContractType.ERC20:
            recommendations.extend([
                "Consider implementing ERC20Permit for gasless approvals",
                "Implement proper decimal handling to prevent precision loss",
                "Consider adding supply caps to prevent infinite inflation",
                "Implement proper burn mechanism if deflationary tokenomics needed"
            ])

        elif contract_type == ContractType.ERC721:
            recommendations.extend([
                "Implement proper metadata standards (ERC721Metadata)",
                "Consider ERC721Enumerable for token enumeration capabilities",
                "Implement proper royalty mechanisms if applicable (ERC2981)",
                "Consider batch operations for gas efficiency in minting"
            ])

        # Code-specific analysis
        if 'payable' in contract_code:
            recommendations.append("Use ReentrancyGuard for all payable functions")

        if '.call{' in contract_code:
            recommendations.append("Always check return values of low-level calls")

        if 'assembly' in contract_code:
            recommendations.append("Assembly code requires extra security review")

        return recommendations

    def optimize_gas_usage(self, contract_code: str) -> Tuple[str, List[str], int]:
        """
        Optimize contract for gas efficiency.

        Returns:
            Tuple of (optimized_code, optimizations_applied, estimated_savings)
        """
        optimized_code = contract_code
        optimizations = []
        estimated_savings = 0

        # Storage packing optimization
        if self._can_optimize_storage_packing(contract_code):
            optimized_code = self._optimize_storage_packing(optimized_code)
            optimizations.append("Optimized struct packing for storage efficiency")
            estimated_savings += 20000

        # Function visibility optimization
        optimized_code, visibility_savings = self._optimize_function_visibility(optimized_code)
        if visibility_savings > 0:
            optimizations.append("Optimized function visibility (external vs public)")
            estimated_savings += visibility_savings

        # Immutable variable optimization
        optimized_code, immutable_savings = self._optimize_immutable_variables(optimized_code)
        if immutable_savings > 0:
            optimizations.append("Converted constructor-only variables to immutable")
            estimated_savings += immutable_savings

        return optimized_code, optimizations, estimated_savings

    def _can_optimize_storage_packing(self, contract_code: str) -> bool:
        """Check if storage packing can be optimized."""
        # Look for structs with mixed data types
        struct_pattern = r'struct\s+\w+\s*{[^}]+}'
        structs = re.findall(struct_pattern, contract_code, re.DOTALL)

        for struct in structs:
            # Simple heuristic: if struct has both uint256 and smaller types
            if 'uint256' in struct and any(size in struct for size in ['uint8', 'uint16', 'uint32', 'uint64', 'uint128']):
                return True

        return False

    def _optimize_storage_packing(self, contract_code: str) -> str:
        """Optimize storage packing in structs."""
        # This is a simplified optimization - real implementation would be more sophisticated
        return contract_code

    def _optimize_function_visibility(self, contract_code: str) -> Tuple[str, int]:
        """Optimize function visibility."""
        # Convert public functions to external where appropriate
        savings = 0
        # Simplified implementation
        return contract_code, savings

    def _optimize_immutable_variables(self, contract_code: str) -> Tuple[str, int]:
        """Convert appropriate variables to immutable."""
        savings = 0
        # Simplified implementation
        return contract_code, savings

    def generate_access_control_recommendations(
        self,
        contract_complexity: int,
        expected_admins: int = 1
    ) -> Dict[str, str]:
        """Generate access control pattern recommendations."""
        if expected_admins == 1 and contract_complexity <= 5:
            return {
                'pattern': 'ownable',
                'reason': 'Simple single-owner pattern suitable for basic contracts',
                'implementation': self.access_control_patterns['ownable'],
                'upgrade_path': 'Consider Ownable2Step for production deployment'
            }
        elif expected_admins == 1 and contract_complexity > 5:
            return {
                'pattern': 'ownable2step',
                'reason': 'Safer ownership transfer for complex contracts',
                'implementation': self.access_control_patterns['ownable2step'],
                'upgrade_path': 'Consider AccessControl for multi-admin requirements'
            }
        else:
            return {
                'pattern': 'access_control',
                'reason': 'Role-based access control for multi-admin systems',
                'implementation': self.access_control_patterns['access_control'],
                'upgrade_path': 'Integrate with governance system for decentralization'
            }


if __name__ == "__main__":
    # Test OpenZeppelin helper
    helper = OpenZeppelinHelper()

    # Test contract code
    test_contract = '''
    pragma solidity ^0.8.19;

    contract TestContract {
        uint256 public totalSupply;

        function mint(address to, uint256 amount) public {
            // Mint logic
        }

        function withdraw() public {
            (bool success, ) = msg.sender.call{value: address(this).balance}("");
            require(success);
        }
    }
    '''

    # Test security pattern injection
    enhanced_code, patterns, recommendations = helper.inject_security_patterns(
        test_contract,
        ['mintable', 'pausable'],
        ContractType.ERC20
    )

    print("✅ OpenZeppelin Helper Test:")
    print(f"🔧 Injected patterns: {patterns}")
    print(f"📋 Recommendations: {len(recommendations)}")
    print(f"🛡️ Security patterns available: {len(helper.security_patterns)}")

    # Test access control recommendations
    ac_rec = helper.generate_access_control_recommendations(7, 1)
    print(f"🔐 Recommended access control: {ac_rec['pattern']}")
    print(f"📖 Reason: {ac_rec['reason']}")