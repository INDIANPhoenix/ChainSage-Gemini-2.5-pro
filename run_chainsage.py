#!/usr/bin/env python3
"""
ChainSage Runner - Simple interface to run the ChainSage system

Usage:
    python run_chainsage.py --spec "Create an ERC20 token called MyToken"
    python run_chainsage.py --help
"""

import asyncio
import argparse
import os
import sys
from pathlib import Path

# Add the current directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

def setup_mock_environment():
    """Set up mock environment for testing without external dependencies"""

    # Mock pydantic for basic functionality
    class MockBaseModel:
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)

    class MockField:
        def __init__(self, *args, **kwargs):
            pass

    def mock_validator(field):
        def decorator(func):
            return func
        return decorator

    # Create mock modules
    import types

    # Mock pydantic
    pydantic = types.ModuleType('pydantic')
    pydantic.BaseModel = MockBaseModel
    pydantic.Field = MockField
    pydantic.validator = mock_validator
    sys.modules['pydantic'] = pydantic

    # Mock pydantic_settings
    pydantic_settings = types.ModuleType('pydantic_settings')
    pydantic_settings.BaseSettings = MockBaseModel
    sys.modules['pydantic_settings'] = pydantic_settings

    # Mock openai
    openai = types.ModuleType('openai')
    sys.modules['openai'] = openai

    # Set environment variables for testing
    os.environ.setdefault('OPENAI_API_KEY', 'mock-key-for-testing')
    os.environ.setdefault('OPENAI_MODEL', 'gpt-4o-2024-11-20')

def print_banner():
    """Print ChainSage banner"""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║                          ChainSage                           ║
║          Agentic AI Smart Contract Generator & Auditor       ║
║                                                              ║
║  Transform natural language into secure Solidity contracts  ║
╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

async def run_contract_generation(specification: str, contract_type: str = "custom"):
    """Run contract generation with mock environment"""

    from enum import Enum
    import re

    print(f"🤖 Processing specification: '{specification}'")
    print(f"📋 Contract type: {contract_type}")
    print("-" * 60)

    # Mock contract types
    class ContractType(str, Enum):
        ERC20 = "erc20"
        ERC721 = "erc721"
        ERC1155 = "erc1155"
        GOVERNANCE = "governance"
        CUSTOM = "custom"

    # Extract contract name from specification
    def extract_contract_name(spec):
        patterns = [
            r'(?:contract|token|coin)\s+(?:called|named)\s+(\w+)',
            r'(\w+)\s+(?:token|coin|contract)',
            r'create\s+(?:a|an)\s+(\w+)'
        ]

        for pattern in patterns:
            match = re.search(pattern, spec, re.IGNORECASE)
            if match:
                name = match.group(1)
                return ''.join(word.capitalize() for word in re.findall(r'\w+', name))
        return "GeneratedContract"

    contract_name = extract_contract_name(specification)

    # Determine security features from specification
    security_features = []
    if any(word in specification.lower() for word in ['mint', 'minting']):
        security_features.append('mintable')
    if any(word in specification.lower() for word in ['pause', 'emergency', 'stop']):
        security_features.append('pausable')
    if any(word in specification.lower() for word in ['burn', 'burning']):
        security_features.append('burnable')
    if any(word in specification.lower() for word in ['vote', 'voting', 'governance']):
        security_features.append('votes')
    if any(word in specification.lower() for word in ['access', 'role', 'permission']):
        security_features.append('access_control')

    # Generate contract based on type
    print(f"🏗️  Generating {contract_type.upper()} contract...")
    print(f"🏷️  Contract name: {contract_name}")
    print(f"🔒 Security features: {security_features}")
    print()

    # Build the contract
    if contract_type == "erc20" or any(word in specification.lower() for word in ['token', 'erc20', 'fungible']):
        contract_code = generate_erc20_contract(contract_name, security_features, specification)
    elif contract_type == "erc721" or any(word in specification.lower() for word in ['nft', 'erc721', 'non-fungible']):
        contract_code = generate_erc721_contract(contract_name, security_features, specification)
    else:
        contract_code = generate_custom_contract(contract_name, security_features, specification)

    # Display results
    print("✅ Contract Generation Complete!")
    print("=" * 60)
    print("📄 Generated Solidity Contract:")
    print("=" * 60)
    print(contract_code)
    print("=" * 60)

    # Analysis
    lines = contract_code.split('\n')
    imports = [line for line in lines if line.strip().startswith('import')]
    functions = [line for line in lines if 'function ' in line]

    print("\n📊 Contract Analysis:")
    print(f"   📏 Lines of code: {len(lines)}")
    print(f"   📦 OpenZeppelin imports: {len(imports)}")
    print(f"   🔧 Functions: {len(functions)}")
    print(f"   🛡️  Security features: {len(security_features)}")
    print(f"   ⛽ Estimated gas: ~1,200,000 (typical ERC20 deployment)")

    # Save to file
    output_dir = Path("out/contracts")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"{contract_name}.sol"
    with open(output_file, 'w') as f:
        f.write(contract_code)

    print(f"\n💾 Contract saved to: {output_file}")

    # Security recommendations
    print("\n🔒 Security Recommendations:")
    print("   • Test thoroughly on testnets before mainnet deployment")
    print("   • Consider professional security audit for production use")
    print("   • Follow principle of least privilege for access controls")
    if 'mintable' in security_features:
        print("   • Implement proper tokenomics and supply management")
    if 'pausable' in security_features:
        print("   • Document emergency pause procedures clearly")

    return contract_code, contract_name

def generate_erc20_contract(name: str, features: list, spec: str) -> str:
    """Generate ERC20 token contract"""
    from datetime import datetime

    symbol = name[:4].upper()
    timestamp = datetime.now().isoformat()

    # Base imports
    imports = [
        '@openzeppelin/contracts/token/ERC20/ERC20.sol',
        '@openzeppelin/contracts/access/Ownable.sol'
    ]

    # Add feature-specific imports
    base_classes = ['ERC20', 'Ownable']

    if 'pausable' in features:
        imports.append('@openzeppelin/contracts/utils/Pausable.sol')
        base_classes.append('Pausable')

    if 'burnable' in features:
        imports.append('@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol')
        base_classes.append('ERC20Burnable')

    if 'votes' in features:
        imports.append('@openzeppelin/contracts/token/ERC20/extensions/ERC20Votes.sol')
        base_classes.append('ERC20Votes')

    if 'access_control' in features:
        imports.append('@openzeppelin/contracts/access/AccessControl.sol')
        base_classes.append('AccessControl')

    # Build contract
    contract_lines = [
        '// SPDX-License-Identifier: MIT',
        'pragma solidity ^0.8.19;',
        '',
    ]

    # Add imports
    for imp in imports:
        contract_lines.append(f'import "{imp}";')

    contract_lines.extend([
        '',
        '/**',
        f' * @title {name}',
        f' * @dev {spec[:100]}...',
        ' *',
        f' * Generated by ChainSage at {timestamp}',
        f' * Security features: {", ".join(features) if features else "Standard"}',
        ' */',
        f'contract {name} is {", ".join(base_classes)} {{',
        ''
    ])

    # Constructor
    constructor_calls = [
        f'ERC20("{name}", "{symbol}")',
        'Ownable(initialOwner)'
    ]

    if 'votes' in features:
        constructor_calls.append('ERC20Permit(name())')

    contract_lines.extend([
        '    constructor(address initialOwner)',
        f'        {constructor_calls[0]}',
        f'        {constructor_calls[1]}',
    ])

    if len(constructor_calls) > 2:
        contract_lines.append(f'        {constructor_calls[2]}')

    contract_lines.extend([
        '    {',
        '        // Initial supply can be minted here if needed',
        '        // _mint(initialOwner, initialSupply);',
        '    }',
        ''
    ])

    # Add feature-specific functions
    if 'mintable' in features:
        contract_lines.extend([
            '    /**',
            '     * @dev Mint new tokens. Only callable by owner.',
            '     * @param to The address to mint tokens to',
            '     * @param amount The amount of tokens to mint',
            '     */',
            '    function mint(address to, uint256 amount) public onlyOwner {',
            '        _mint(to, amount);',
            '    }',
            ''
        ])

    if 'pausable' in features:
        contract_lines.extend([
            '    /**',
            '     * @dev Pause all token transfers. Only callable by owner.',
            '     */',
            '    function pause() public onlyOwner {',
            '        _pause();',
            '    }',
            '',
            '    /**',
            '     * @dev Unpause all token transfers. Only callable by owner.',
            '     */',
            '    function unpause() public onlyOwner {',
            '        _unpause();',
            '    }',
            '',
            '    /**',
            '     * @dev Override required by Pausable extension.',
            '     */',
            '    function _update(address from, address to, uint256 value)',
            '        internal',
            '        override',
            '        whenNotPaused',
            '    {',
            '        super._update(from, to, value);',
            '    }',
            ''
        ])

    contract_lines.append('}')

    return '\n'.join(contract_lines)

def generate_erc721_contract(name: str, features: list, spec: str) -> str:
    """Generate ERC721 NFT contract"""
    symbol = name[:4].upper()

    return f'''// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title {name}
 * @dev NFT contract generated from: {spec[:80]}...
 * Generated by ChainSage
 */
contract {name} is ERC721, Ownable {{
    uint256 private _tokenIdCounter;
    uint256 public maxSupply = 10000;

    constructor(address initialOwner)
        ERC721("{name}", "{symbol}")
        Ownable(initialOwner)
    {{}}

    /**
     * @dev Mint NFT to specified address
     */
    function safeMint(address to) public onlyOwner {{
        require(_tokenIdCounter < maxSupply, "Max supply reached");
        _safeMint(to, _tokenIdCounter);
        _tokenIdCounter++;
    }}

    /**
     * @dev Get current token supply
     */
    function totalSupply() public view returns (uint256) {{
        return _tokenIdCounter;
    }}
}}'''

def generate_custom_contract(name: str, features: list, spec: str) -> str:
    """Generate custom contract"""

    return f'''// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

/**
 * @title {name}
 * @dev Custom contract generated from: {spec[:80]}...
 * Generated by ChainSage
 */
contract {name} is Ownable, ReentrancyGuard {{

    // State variables
    mapping(address => uint256) public userBalances;
    uint256 public totalBalance;

    // Events
    event Deposit(address indexed user, uint256 amount);
    event Withdrawal(address indexed user, uint256 amount);

    constructor(address initialOwner) Ownable(initialOwner) {{}}

    /**
     * @dev Deposit funds to the contract
     */
    function deposit() public payable nonReentrant {{
        require(msg.value > 0, "Must send some ether");

        userBalances[msg.sender] += msg.value;
        totalBalance += msg.value;

        emit Deposit(msg.sender, msg.value);
    }}

    /**
     * @dev Withdraw funds from the contract
     */
    function withdraw(uint256 amount) public nonReentrant {{
        require(userBalances[msg.sender] >= amount, "Insufficient balance");

        userBalances[msg.sender] -= amount;
        totalBalance -= amount;

        (bool success, ) = payable(msg.sender).call{{value: amount}}("");
        require(success, "Transfer failed");

        emit Withdrawal(msg.sender, amount);
    }}

    /**
     * @dev Get user balance
     */
    function getUserBalance(address user) public view returns (uint256) {{
        return userBalances[user];
    }}
}}'''

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="ChainSage - Agentic AI Smart Contract Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_chainsage.py --spec "Create an ERC20 token called MyToken with minting"
  python run_chainsage.py --spec "Create an NFT collection called CoolNFTs" --type erc721
  python run_chainsage.py --spec "Create a governance token with voting and pause" --type erc20
  python run_chainsage.py --spec "Create a custom contract for managing deposits"
        """
    )

    parser.add_argument(
        '--spec',
        type=str,
        required=True,
        help='Natural language specification for the smart contract'
    )

    parser.add_argument(
        '--type',
        choices=['erc20', 'erc721', 'erc1155', 'governance', 'custom'],
        default='custom',
        help='Type of contract to generate (default: auto-detect from spec)'
    )

    parser.add_argument(
        '--output',
        type=str,
        default='out/contracts',
        help='Output directory for generated contracts (default: out/contracts)'
    )

    args = parser.parse_args()

    print_banner()

    # Set up mock environment for demo
    setup_mock_environment()

    try:
        # Run the contract generation
        result = asyncio.run(run_contract_generation(args.spec, args.type))

        print("\n🎉 ChainSage execution completed successfully!")
        print("\nNext steps:")
        print("1. Review the generated contract carefully")
        print("2. Test on a testnet before mainnet deployment")
        print("3. Consider a professional security audit")
        print("4. Set up proper deployment scripts")

    except KeyboardInterrupt:
        print("\n\n⚠️  Operation cancelled by user")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("\nFor support, check the documentation or create an issue.")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())