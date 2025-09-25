#!/bin/bash

# ChainSage Web Interface Startup Script
echo "🚀 Starting ChainSage Web Interface..."
echo "=================================================="

# Check if virtual environment exists
if [ ! -d "web_env" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv web_env
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source web_env/bin/activate

# Check if dependencies are installed
echo "📋 Checking dependencies..."
if ! python -c "import fastapi" 2>/dev/null; then
    echo "📥 Installing FastAPI dependencies..."
    pip install fastapi uvicorn python-multipart pydantic
fi

# Check for OpenAI API key
if [ -z "$OPENAI_API_KEY" ]; then
    echo "⚠️  WARNING: OPENAI_API_KEY environment variable not set"
    echo "   Please set it with: export OPENAI_API_KEY='your-api-key'"
    echo "   Or the contract generation will use mock mode"
fi

echo ""
echo "🌟 ChainSage Web Interface Starting..."
echo "=================================================="
echo "📡 Backend API:     http://localhost:8000"
echo "🌐 Web Interface:   http://localhost:8000"
echo "📚 API Docs:        http://localhost:8000/docs"
echo "❤️  Interactive:    http://localhost:8000/redoc"
echo "=================================================="
echo ""
echo "✨ Features Available:"
echo "   • Natural language contract generation"
echo "   • Real-time code preview"
echo "   • Security analysis"
echo "   • One-click download"
echo ""
echo "💡 Example descriptions to try:"
echo "   • Create gaming token with staking rewards"
echo "   • Create NFT collection with 10000 max supply"
echo "   • Create DAO voting contract with timelock"
echo ""
echo "🛑 Press Ctrl+C to stop the server"
echo "=================================================="
echo ""

# Start the web application
python3 web_app.py