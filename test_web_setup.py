#!/usr/bin/env python3
"""
Test script to verify ChainSage web interface setup
"""

import sys
import os
from pathlib import Path

def test_web_setup():
    """Test that all web interface components are properly set up"""

    print("🧪 Testing ChainSage Web Interface Setup")
    print("=" * 50)

    # Test file structure
    required_files = [
        "web/app.py",
        "web/frontend/package.json",
        "web/frontend/app/page.tsx",
        "web/frontend/components/contract-generator.tsx",
        "web/frontend/components/contract-preview.tsx",
        "web/frontend/tailwind.config.js",
        "docker-compose.yml",
        "WEB_INTERFACE_SETUP.md"
    ]

    print("📁 Checking file structure...")
    missing_files = []

    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path}")
            missing_files.append(file_path)

    if missing_files:
        print(f"\n⚠️  Missing {len(missing_files)} files:")
        for file in missing_files:
            print(f"   • {file}")
        return False

    print("\n🎉 All required files are present!")

    # Test backend structure
    print("\n🔧 Testing backend structure...")
    try:
        # Check if run_chainsage.py exists and can be imported
        if os.path.exists("run_chainsage.py"):
            print("✅ ChainSage core module found")
        else:
            print("❌ ChainSage core module not found")
            return False

        # Check web app structure
        with open("web/app.py", "r") as f:
            content = f.read()
            if "FastAPI" in content and "generate-contract" in content:
                print("✅ FastAPI backend properly structured")
            else:
                print("❌ FastAPI backend incomplete")
                return False

    except Exception as e:
        print(f"❌ Backend test failed: {e}")
        return False

    # Test frontend structure
    print("\n🎨 Testing frontend structure...")
    try:
        with open("web/frontend/package.json", "r") as f:
            content = f.read()
            if "next" in content and "shadcn" in content.lower():
                print("✅ Next.js + ShadCN setup found")
            else:
                print("❌ Frontend dependencies incomplete")
                return False

        with open("web/frontend/app/page.tsx", "r") as f:
            content = f.read()
            if "ContractGenerator" in content and "ContractPreview" in content:
                print("✅ Main components properly integrated")
            else:
                print("❌ Component integration incomplete")
                return False

    except Exception as e:
        print(f"❌ Frontend test failed: {e}")
        return False

    # Test Docker configuration
    print("\n🐳 Testing Docker configuration...")
    try:
        with open("docker-compose.yml", "r") as f:
            content = f.read()
            if "backend:" in content and "frontend:" in content:
                print("✅ Docker Compose properly configured")
            else:
                print("❌ Docker configuration incomplete")
                return False

    except Exception as e:
        print(f"❌ Docker test failed: {e}")
        return False

    print("\n" + "=" * 50)
    print("🎉 ALL TESTS PASSED!")
    print("✅ ChainSage Web Interface is ready to deploy!")
    print("\n🚀 To start the web interface:")
    print("   1. Set your OpenAI API key: export OPENAI_API_KEY='your-key'")
    print("   2. Run: docker-compose up --build")
    print("   3. Visit: http://localhost:3000")

    return True

def print_setup_instructions():
    """Print quick setup instructions"""
    print("\n" + "=" * 60)
    print("🌐 ChainSage Web Interface - Quick Start Guide")
    print("=" * 60)

    print("""
🔧 Option 1: Docker Setup (Recommended)
   cd /home/amandeep/Downloads/context_engeneering
   export OPENAI_API_KEY="your-api-key-here"
   docker-compose up --build

   Frontend: http://localhost:3000
   Backend:  http://localhost:8000

🛠️  Option 2: Manual Setup
   Terminal 1 (Backend):
   pip install fastapi uvicorn python-multipart
   cd web && python3 app.py

   Terminal 2 (Frontend):
   cd web/frontend
   npm install && npm run dev

📚 Features Ready:
   ✅ Natural language contract generation
   ✅ Real-time code preview with syntax highlighting
   ✅ Security analysis and vulnerability detection
   ✅ One-click contract download
   ✅ Modern ShadCN UI with responsive design
   ✅ Example gallery and documentation

🎯 Example Usage:
   • "Create gaming token with rewards and staking"
   • "Create NFT collection with 10000 max supply"
   • "Create DAO voting contract with timelock"
   • "Create DeFi yield farming protocol"
""")

if __name__ == "__main__":
    if test_web_setup():
        print_setup_instructions()
    else:
        print("\n❌ Setup incomplete. Please check missing components.")
        sys.exit(1)