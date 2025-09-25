# ChainSage Quick Start Guide

## 🚀 How to Run ChainSage

ChainSage is now ready to run! Here are several ways to get started:

## Option 1: Simple Python Runner (Recommended for Testing)

```bash
# Navigate to ChainSage directory
cd /home/amandeep/Downloads/context_engeneering

# Run with a simple ERC20 token
python run_chainsage.py --spec "Create an ERC20 token called MyToken with minting capabilities"

# Run with an NFT collection
python run_chainsage.py --spec "Create an NFT collection called CoolNFTs with 10000 max supply" --type erc721

# Run with governance token
python run_chainsage.py --spec "Create a governance token called DAOToken with voting and emergency pause" --type erc20

# Custom contract
python run_chainsage.py --spec "Create a contract for managing user deposits and withdrawals"
```

## Option 2: Interactive Python Session

```bash
# Start Python in ChainSage directory
cd /home/amandeep/Downloads/context_engeneering
python3 -i run_chainsage.py --spec "Create a simple ERC20 token"
```

## Option 3: Direct Component Testing

Test individual components directly:

```bash
# Test Solidity Generator
python3 -c "
import sys
sys.path.append('/home/amandeep/Downloads/context_engeneering')
# Run individual tests here
"
```

## 🎯 Example Commands

### Generate ERC20 Tokens
```bash
# Basic ERC20
python run_chainsage.py --spec "Create a token called BasicToken"

# Advanced ERC20 with features
python run_chainsage.py --spec "Create a governance token called VoteToken with minting, burning, and pause functionality" --type erc20

# Supply-capped token
python run_chainsage.py --spec "Create a token called LimitedToken with maximum supply of 1 million tokens"
```

### Generate NFT Collections
```bash
# Basic NFT
python run_chainsage.py --spec "Create an NFT collection called ArtNFTs" --type erc721

# Gaming NFT
python run_chainsage.py --spec "Create NFTs for a game called GameItems with special minting rules" --type erc721
```

### Generate Custom Contracts
```bash
# DeFi Contract
python run_chainsage.py --spec "Create a staking contract where users can stake tokens and earn rewards"

# Escrow Contract
python run_chainsage.py --spec "Create an escrow contract for secure peer-to-peer transactions"

# Multisig Wallet
python run_chainsage.py --spec "Create a multi-signature wallet requiring 3 out of 5 signatures"
```

## 📋 Command Line Options

```bash
python run_chainsage.py [OPTIONS]

Required:
  --spec TEXT     Natural language specification for the smart contract

Optional:
  --type CHOICE   Contract type: erc20, erc721, erc1155, governance, custom (default: auto-detect)
  --output PATH   Output directory (default: out/contracts)
  --help          Show help message
```

## 📁 Output Files

Generated contracts are saved to:
```
out/
├── contracts/          # Generated .sol files
├── audits/            # Audit reports (when analysis runs)
├── patches/           # Security patches
└── tests/             # Test files (future feature)
```

## 🛠️ Advanced Usage

### With Full Dependencies (Production Setup)

1. **Install Python Dependencies**:
```bash
pip install -r requirements.txt
```

2. **Set Environment Variables**:
```bash
export OPENAI_API_KEY="your-openai-api-key"
export OPENAI_MODEL="gpt-4o-2024-11-20"
```

3. **Run with Full Agent System**:
```bash
python -c "
import asyncio
from chainsage.agents.generation_agent import GenerationAgent
from chainsage.agents.models import GenerationRequest, ContractType

async def main():
    agent = GenerationAgent()
    request = GenerationRequest(
        specification='Create a governance token with advanced voting',
        contract_type=ContractType.ERC20,
        security_features=['mintable', 'pausable', 'votes']
    )
    result = await agent.generate_contract(request)
    print(result.solidity_code)

asyncio.run(main())
"
```

## 🔧 Troubleshooting

### Common Issues:

1. **Import Errors**: Use the mock runner for testing without dependencies
2. **Permission Issues**: Ensure write permissions to output directory
3. **Python Path**: Make sure you're in the correct directory

### Solutions:
```bash
# Fix Python path
export PYTHONPATH="/home/amandeep/Downloads/context_engeneering:$PYTHONPATH"

# Create output directories
mkdir -p out/{contracts,audits,patches,tests}

# Test basic functionality
python run_chainsage.py --spec "Create a simple token" --help
```

## 🎨 Example Outputs

### Generated ERC20 Token:
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MyToken is ERC20, Ownable {
    constructor(address initialOwner)
        ERC20("MyToken", "MTK")
        Ownable(initialOwner)
    {}

    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }
}
```

### Sample Output:
```
╔══════════════════════════════════════════════════════════════╗
║                          ChainSage                           ║
║          Agentic AI Smart Contract Generator & Auditor       ║
║                                                              ║
║  Transform natural language into secure Solidity contracts  ║
╚══════════════════════════════════════════════════════════════╝

🤖 Processing specification: 'Create an ERC20 token called MyToken'
📋 Contract type: erc20
------------------------------------------------------------
🏗️  Generating ERC20 contract...
🏷️  Contract name: MyToken
🔒 Security features: ['mintable']

✅ Contract Generation Complete!
============================================================
📄 Generated Solidity Contract:
[Contract code displayed here]
============================================================

📊 Contract Analysis:
   📏 Lines of code: 35
   📦 OpenZeppelin imports: 2
   🔧 Functions: 2
   🛡️  Security features: 1
   ⛽ Estimated gas: ~1,200,000

💾 Contract saved to: out/contracts/MyToken.sol

🔒 Security Recommendations:
   • Test thoroughly on testnets before mainnet deployment
   • Consider professional security audit for production use
   • Follow principle of least privilege for access controls
```

## 🎉 Success!

You now have ChainSage running and generating smart contracts! The system will:

1. **Parse** your natural language specification
2. **Generate** appropriate Solidity code with security patterns
3. **Apply** OpenZeppelin best practices
4. **Save** the contract to the output directory
5. **Provide** security recommendations

Ready to create your first smart contract? Try the examples above!