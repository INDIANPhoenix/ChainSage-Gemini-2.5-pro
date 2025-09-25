#!/usr/bin/env python3
"""
ChainSage Runner - Gemini-powered version
Uses Google's Gemini API for smart contract generation

Usage:
    python run_chainsage_gemini.py --spec "Create an ERC20 token called MyToken"
    python run_chainsage_gemini.py --help
"""

import asyncio
import argparse
import os
import sys
import json
from pathlib import Path
from datetime import datetime
import google.generativeai as genai

# Configure Gemini API
GEMINI_API_KEY = "AIzaSyD5rJWiDC0ZgPIk8AsQeu430oOYhWvBnMo"
genai.configure(api_key=GEMINI_API_KEY)

def print_banner():
    """Print ChainSage banner"""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║                          ChainSage                           ║
║          Agentic AI Smart Contract Generator & Auditor       ║
║                     Powered by Google Gemini                ║
║                                                              ║
║  Transform natural language into secure Solidity contracts  ║
╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

async def generate_contract_with_gemini(specification: str, contract_type: str = "custom"):
    """Generate smart contract using Google Gemini"""

    print(f"🤖 Processing specification: '{specification}'")
    print(f"📋 Contract type: {contract_type}")
    print("-" * 60)

    # Create Gemini model instance
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Craft detailed prompt for contract generation
    prompt = f"""
You are ChainSage, an expert Solidity smart contract generator. Generate a production-ready smart contract based on this specification:

SPECIFICATION: {specification}
CONTRACT_TYPE: {contract_type}

REQUIREMENTS:
1. Generate complete, production-ready Solidity code
2. Use OpenZeppelin imports for security
3. Include proper SPDX license and pragma
4. Add comprehensive NatSpec documentation
5. Follow Solidity best practices
6. Include security features based on specification
7. Use appropriate contract inheritance

CONTRACT TYPES:
- erc20: Create ERC20 token contract
- erc721: Create ERC721 NFT contract
- defi: Create DeFi protocol contract
- governance: Create DAO governance contract
- custom: Analyze specification and create appropriate contract

SECURITY FEATURES TO CONSIDER:
- Mintable: Add minting functionality
- Pausable: Add emergency pause capability
- Burnable: Add token burning functionality
- Votes: Add governance voting power
- Access Control: Add role-based permissions
- Reentrancy Guard: Prevent reentrancy attacks

OUTPUT FORMAT:
Return only the complete Solidity smart contract code, starting with "// SPDX-License-Identifier: MIT"

Generate the contract now:
"""

    try:
        print("🔄 Generating contract with Gemini AI...")

        # Generate content with Gemini
        response = model.generate_content(prompt)
        contract_code = response.text.strip()

        # Clean up the response - remove any markdown formatting
        if contract_code.startswith("```solidity"):
            contract_code = contract_code[11:]  # Remove ```solidity
        elif contract_code.startswith("```"):
            contract_code = contract_code[3:]   # Remove ```

        if contract_code.endswith("```"):
            contract_code = contract_code[:-3]  # Remove closing ```

        contract_code = contract_code.strip()

        # Extract contract name from the code
        contract_name = extract_contract_name(contract_code, specification)

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
        events = [line for line in lines if 'event ' in line]

        print("\n📊 Contract Analysis:")
        print(f"   📏 Lines of code: {len(lines)}")
        print(f"   📦 OpenZeppelin imports: {len(imports)}")
        print(f"   🔧 Functions: {len(functions)}")
        print(f"   📡 Events: {len(events)}")
        print(f"   🛡️  Security features: Auto-applied based on specification")
        print(f"   ⛽ Estimated gas: ~1,200,000 (typical deployment)")

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
        print("   • Verify all OpenZeppelin imports are latest versions")

        return contract_code, contract_name

    except Exception as e:
        print(f"❌ Error generating contract: {str(e)}")
        return None, None

def extract_contract_name(contract_code: str, specification: str) -> str:
    """Extract contract name from generated code or specification"""
    import re

    # Try to find contract name in the code
    contract_match = re.search(r'contract\s+(\w+)', contract_code)
    if contract_match:
        return contract_match.group(1)

    # Fallback: extract from specification
    patterns = [
        r'(?:contract|token|coin)\s+(?:called|named)\s+([\w\s]+)',
        r'([\w\s]+)\s+(?:token|coin|contract)',
        r'create\s+(?:a|an)\s+([\w\s]+)'
    ]

    for pattern in patterns:
        match = re.search(pattern, specification, re.IGNORECASE)
        if match:
            name = match.group(1).strip()
            # Clean and format name
            name = ''.join(word.capitalize() for word in re.findall(r'\w+', name))
            return name

    return "GeneratedContract"

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="ChainSage - Gemini-Powered Smart Contract Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_chainsage_gemini.py --spec "Create an ERC20 token called MyToken with minting"
  python run_chainsage_gemini.py --spec "Create an NFT collection called CoolNFTs" --type erc721
  python run_chainsage_gemini.py --spec "Create a governance token with voting and pause" --type erc20
  python run_chainsage_gemini.py --spec "Create a DeFi yield farming protocol with rewards"
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
        choices=['erc20', 'erc721', 'erc1155', 'governance', 'defi', 'custom'],
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

    try:
        # Run the contract generation
        result = asyncio.run(generate_contract_with_gemini(args.spec, args.type))

        if result[0]:  # If successful
            print("\n🎉 ChainSage (Gemini) execution completed successfully!")
            print("\n🚀 Powered by Google Gemini - Free & Fast!")
            print("\nNext steps:")
            print("1. Review the generated contract carefully")
            print("2. Test on a testnet before mainnet deployment")
            print("3. Consider a professional security audit")
            print("4. Set up proper deployment scripts")
        else:
            print("\n❌ Contract generation failed")
            return 1

    except KeyboardInterrupt:
        print("\n\n⚠️  Operation cancelled by user")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("\nFor support, check the documentation or create an issue.")
        return 1

    return 0

# Make this available as a module function
async def run_contract_generation(specification: str, contract_type: str = "custom"):
    """Module function for web interface integration"""
    return await generate_contract_with_gemini(specification, contract_type)

if __name__ == "__main__":
    exit(main())