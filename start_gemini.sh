#!/bin/bash

# ChainSage Gemini Web Interface Startup Script
echo "🧠 Starting ChainSage with Google Gemini..."
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
if ! python -c "import google.generativeai" 2>/dev/null; then
    echo "📥 Installing Gemini dependencies..."
    pip install google-generativeai fastapi uvicorn python-multipart pydantic
fi

echo ""
echo "🧠 ChainSage Gemini Interface Starting..."
echo "=================================================="
echo "📡 Backend API:     http://localhost:8000"
echo "🌐 Web Interface:   http://localhost:8000"
echo "📚 API Docs:        http://localhost:8000/docs"
echo "🧠 AI Model:        Google Gemini 1.5 Flash"
echo "💰 Cost:           COMPLETELY FREE"
echo "=================================================="
echo ""
echo "✨ Gemini-Powered Features:"
echo "   🧠 True AI understanding of complex specifications"
echo "   🎯 Creative contract logic generation"
echo "   🛡️ Intelligent security pattern integration"
echo "   ⚡ Advanced DeFi mechanism implementation"
echo "   🆓 Unlimited free usage"
echo ""
echo "💡 Try these advanced examples:"
echo "   • Advanced DeFi with dynamic yield farming"
echo "   • Sophisticated NFT marketplace with auctions"
echo "   • DAO with quadratic voting mechanisms"
echo "   • Gaming ecosystem with anti-whale protection"
echo ""
echo "🛑 Press Ctrl+C to stop the server"
echo "=================================================="
echo ""

# Start the Gemini-powered web application
python3 web_app_gemini.py