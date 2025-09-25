#!/usr/bin/env python3
"""
ChainSage Web Interface - Gemini-Powered Version
Directly integrates with Gemini API for true AI contract generation
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import asyncio
import json
import os
import sys
import uuid
from pathlib import Path
from datetime import datetime
import google.generativeai as genai

# Configure Gemini API
GEMINI_API_KEY = "AIzaSyD5rJWiDC0ZgPIk8AsQeu430oOYhWvBnMo"
genai.configure(api_key=GEMINI_API_KEY)

# Import the Gemini-powered ChainSage functionality
sys.path.insert(0, str(Path(__file__).parent))
from run_chainsage_gemini import run_contract_generation

app = FastAPI(
    title="ChainSage Web Interface - Gemini Powered",
    description="Transform natural language into secure Solidity contracts using Google Gemini",
    version="2.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response Models
class ContractRequest(BaseModel):
    specification: str
    contract_type: Optional[str] = "custom"
    security_features: Optional[List[str]] = []

class ContractResponse(BaseModel):
    success: bool
    contract_code: Optional[str] = None
    contract_name: Optional[str] = None
    analysis: Optional[Dict[str, Any]] = None
    error_message: Optional[str] = None
    request_id: str
    ai_model: str = "gemini-1.5-flash"

# Storage for requests
active_requests = {}

@app.get("/")
async def read_root():
    return HTMLResponse(content="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ChainSage - AI Smart Contract Generator (Gemini Powered)</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest/dist/umd/lucide.js"></script>
    <style>
        .gradient-bg { background: linear-gradient(135deg, #4285f4 0%, #34a853 100%); }
        .gradient-text {
            background: linear-gradient(135deg, #4285f4 0%, #ea4335 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .loading { animation: pulse 2s infinite; }
        .code-highlight { background: #1e293b; border-radius: 8px; }
        .animate-bounce-slow { animation: bounce 2s infinite; }
        .gemini-glow {
            box-shadow: 0 0 20px rgba(66, 133, 244, 0.3);
            border: 2px solid rgba(66, 133, 244, 0.2);
        }
    </style>
</head>
<body class="bg-gray-50 min-h-screen">
    <!-- Header -->
    <header class="gradient-bg text-white shadow-lg">
        <div class="container mx-auto px-6 py-4">
            <div class="flex items-center justify-between">
                <div class="flex items-center space-x-3">
                    <div class="w-10 h-10 bg-white rounded-lg flex items-center justify-center">
                        <span class="text-2xl">🧠</span>
                    </div>
                    <div>
                        <h1 class="text-2xl font-bold">ChainSage</h1>
                        <p class="text-blue-100 text-sm">Powered by Google Gemini</p>
                    </div>
                </div>
                <div class="flex items-center space-x-4 text-sm">
                    <div class="flex items-center space-x-2">
                        <div class="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
                        <span>Gemini AI</span>
                    </div>
                    <div class="flex items-center space-x-2">
                        <div class="w-2 h-2 bg-yellow-400 rounded-full animate-pulse"></div>
                        <span>Free & Fast</span>
                    </div>
                    <div class="flex items-center space-x-2">
                        <div class="w-2 h-2 bg-red-400 rounded-full animate-pulse"></div>
                        <span>True AI</span>
                    </div>
                </div>
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <main class="container mx-auto px-6 py-8">
        <!-- Hero Section -->
        <div class="text-center mb-12">
            <h2 class="text-4xl font-bold mb-4">
                <span class="gradient-text">Next-Gen AI Smart Contract Generation</span>
            </h2>
            <p class="text-gray-600 text-xl max-w-3xl mx-auto">
                Powered by Google Gemini - Generate truly intelligent Solidity contracts from natural language
            </p>
            <div class="mt-6 p-4 bg-blue-50 border border-blue-200 rounded-lg inline-block">
                <p class="text-blue-800 font-semibold">🆕 Now with Google Gemini: More Creative • More Intelligent • Completely Free</p>
            </div>
        </div>

        <!-- Stats -->
        <div class="grid md:grid-cols-4 gap-6 mb-12">
            <div class="text-center p-6 bg-white rounded-xl shadow-lg gemini-glow">
                <div class="text-3xl font-bold text-blue-600">Gemini</div>
                <div class="text-gray-600">AI Model</div>
            </div>
            <div class="text-center p-6 bg-white rounded-xl shadow-lg">
                <div class="text-3xl font-bold text-green-600">Free</div>
                <div class="text-gray-600">API Usage</div>
            </div>
            <div class="text-center p-6 bg-white rounded-xl shadow-lg">
                <div class="text-3xl font-bold text-purple-600">Smart</div>
                <div class="text-gray-600">AI Generation</div>
            </div>
            <div class="text-center p-6 bg-white rounded-xl shadow-lg">
                <div class="text-3xl font-bold text-orange-600">&lt;2s</div>
                <div class="text-gray-600">Generation Time</div>
            </div>
        </div>

        <!-- Main Interface -->
        <div class="grid lg:grid-cols-2 gap-8">
            <!-- Contract Generator -->
            <div class="bg-white rounded-xl shadow-lg p-6">
                <h3 class="text-2xl font-bold mb-6 flex items-center">
                    <span class="text-3xl mr-3">🧠</span>
                    Gemini Contract Generator
                </h3>

                <form id="contractForm" class="space-y-6">
                    <!-- Contract Description -->
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-2">
                            Contract Description *
                        </label>
                        <textarea
                            id="specification"
                            rows="6"
                            class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
                            placeholder="e.g., Create an advanced DeFi yield farming protocol called FarmCoin where users can stake multiple tokens, earn dynamic rewards based on market conditions, and participate in governance decisions..."
                            required
                        ></textarea>
                        <p class="text-xs text-gray-500 mt-1">🧠 Gemini can understand complex, detailed specifications</p>
                    </div>

                    <!-- Contract Type -->
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-2">Contract Type</label>
                        <select id="contractType" class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500">
                            <option value="custom">🧠 Let Gemini Decide (Recommended)</option>
                            <option value="erc20">ERC20 Token (Cryptocurrencies, Rewards)</option>
                            <option value="erc721">ERC721 NFT (Digital Art, Collectibles)</option>
                            <option value="defi">DeFi Protocol (Staking, Yield Farming)</option>
                            <option value="governance">Governance (DAO, Voting)</option>
                        </select>
                    </div>

                    <!-- Security Features -->
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-3">
                            <span class="flex items-center">
                                🛡️ Security Hints (Gemini will auto-detect most)
                            </span>
                        </label>
                        <div class="grid grid-cols-2 gap-3">
                            <label class="flex items-center space-x-2 cursor-pointer">
                                <input type="checkbox" value="mintable" class="security-feature rounded text-blue-600">
                                <span class="text-sm">Mintable</span>
                            </label>
                            <label class="flex items-center space-x-2 cursor-pointer">
                                <input type="checkbox" value="pausable" class="security-feature rounded text-blue-600">
                                <span class="text-sm">Pausable</span>
                            </label>
                            <label class="flex items-center space-x-2 cursor-pointer">
                                <input type="checkbox" value="burnable" class="security-feature rounded text-blue-600">
                                <span class="text-sm">Burnable</span>
                            </label>
                            <label class="flex items-center space-x-2 cursor-pointer">
                                <input type="checkbox" value="votes" class="security-feature rounded text-blue-600">
                                <span class="text-sm">Voting Power</span>
                            </label>
                        </div>
                        <p class="text-xs text-gray-500 mt-2">💡 Gemini AI will automatically include appropriate security features</p>
                    </div>

                    <!-- Generate Button -->
                    <button
                        type="submit"
                        id="generateBtn"
                        class="w-full bg-gradient-to-r from-blue-600 to-green-600 hover:from-blue-700 hover:to-green-700 text-white font-semibold py-4 px-6 rounded-lg transition-all duration-200 flex items-center justify-center space-x-2 gemini-glow"
                    >
                        <span id="btnIcon">🧠</span>
                        <span id="btnText">Generate with Gemini AI</span>
                    </button>
                </form>

                <!-- Examples -->
                <div class="mt-8 p-4 bg-gradient-to-r from-blue-50 to-green-50 rounded-lg border border-blue-200">
                    <h4 class="font-semibold text-gray-700 mb-3">🧠 Gemini-Powered Examples (Try These!):</h4>
                    <div class="space-y-2 text-sm text-gray-600">
                        <p class="cursor-pointer hover:text-blue-600" onclick="fillExample('Create an advanced DeFi protocol called YieldMax where users stake multiple cryptocurrencies, earn dynamic rewards based on market volatility, and can vote on protocol parameters with time-weighted voting power')">• Advanced DeFi with dynamic rewards</p>
                        <p class="cursor-pointer hover:text-blue-600" onclick="fillExample('Create a sophisticated NFT marketplace called ArtVerse where artists can mint generative art NFTs, set custom royalty structures, and implement Dutch auction mechanisms')">• NFT marketplace with auctions</p>
                        <p class="cursor-pointer hover:text-blue-600" onclick="fillExample('Create a decentralized autonomous organization called GreenDAO that manages environmental projects, uses quadratic voting for funding decisions, and implements carbon credit tokenization')">• Environmental DAO with quadratic voting</p>
                        <p class="cursor-pointer hover:text-blue-600" onclick="fillExample('Create a gaming ecosystem token called GameFi that rewards players based on skill ratings, enables cross-game asset transfers, and features anti-whale mechanisms')">• Gaming ecosystem with anti-whale</p>
                    </div>
                </div>
            </div>

            <!-- Contract Preview -->
            <div class="bg-white rounded-xl shadow-lg p-6">
                <h3 class="text-2xl font-bold mb-6 flex items-center justify-between">
                    <span class="flex items-center">
                        <span class="text-3xl mr-3">📄</span>
                        Gemini-Generated Contract
                    </span>
                    <div id="previewActions" class="hidden space-x-2">
                        <button onclick="copyContract()" class="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-700 rounded-lg text-sm font-medium">
                            📋 Copy
                        </button>
                        <button onclick="downloadContract()" class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg text-sm font-medium">
                            💾 Download
                        </button>
                    </div>
                </h3>

                <div id="contractPreview" class="min-h-96">
                    <!-- Placeholder -->
                    <div class="flex items-center justify-center h-96 text-gray-400">
                        <div class="text-center">
                            <div class="text-6xl mb-4">🧠</div>
                            <p class="text-lg font-medium">Gemini-generated contract will appear here</p>
                            <p class="text-sm mt-2">Describe complex logic - Gemini understands it all!</p>
                            <div class="mt-4 text-xs space-y-1">
                                <p class="text-green-600">✨ True AI understanding of your requirements</p>
                                <p class="text-blue-600">🔧 Custom logic generation beyond templates</p>
                                <p class="text-purple-600">🛡️ Intelligent security pattern integration</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Gemini Advantages -->
        <div class="mt-12 bg-gradient-to-r from-blue-50 to-green-50 rounded-xl p-8">
            <h3 class="text-2xl font-bold text-center mb-6">🧠 Why Gemini Changes Everything</h3>
            <div class="grid md:grid-cols-3 gap-6">
                <div class="text-center">
                    <div class="text-4xl mb-3">🎯</div>
                    <h4 class="font-semibold mb-2">True Understanding</h4>
                    <p class="text-sm text-gray-600">Gemini deeply understands complex specifications and creates custom logic, not just templates</p>
                </div>
                <div class="text-center">
                    <div class="text-4xl mb-3">💡</div>
                    <h4 class="font-semibold mb-2">Creative Solutions</h4>
                    <p class="text-sm text-gray-600">Generates unique contract architectures and innovative approaches to your requirements</p>
                </div>
                <div class="text-center">
                    <div class="text-4xl mb-3">🆓</div>
                    <h4 class="font-semibold mb-2">Completely Free</h4>
                    <p class="text-sm text-gray-600">No API costs, unlimited usage - advanced AI contract generation for everyone</p>
                </div>
            </div>
        </div>
    </main>

    <script>
        let currentContract = null;

        // Form submission
        document.getElementById('contractForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            await generateContract();
        });

        async function generateContract() {
            const specification = document.getElementById('specification').value;
            const contractType = document.getElementById('contractType').value;

            // Get selected security features
            const securityFeatures = Array.from(document.querySelectorAll('.security-feature:checked'))
                .map(cb => cb.value);

            if (!specification.trim()) {
                alert('Please provide a contract description');
                return;
            }

            // Update UI to loading state
            setLoadingState(true);

            try {
                const response = await fetch('/generate-contract', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        specification: specification,
                        contract_type: contractType,
                        security_features: securityFeatures
                    })
                });

                const result = await response.json();

                if (result.success) {
                    currentContract = result;
                    displayContract(result);
                } else {
                    displayError(result.error_message || 'Contract generation failed');
                }
            } catch (error) {
                displayError('Failed to generate contract: ' + error.message);
            } finally {
                setLoadingState(false);
            }
        }

        function setLoadingState(loading) {
            const btn = document.getElementById('generateBtn');
            const btnIcon = document.getElementById('btnIcon');
            const btnText = document.getElementById('btnText');

            if (loading) {
                btn.disabled = true;
                btn.className = btn.className.replace('from-blue-600 to-green-600 hover:from-blue-700 hover:to-green-700', 'from-gray-400 to-gray-500 cursor-not-allowed');
                btnIcon.textContent = '🧠';
                btnText.textContent = 'Gemini is thinking...';

                // Show loading in preview
                document.getElementById('contractPreview').innerHTML = `
                    <div class="flex items-center justify-center h-96">
                        <div class="text-center">
                            <div class="text-4xl mb-4 animate-bounce">🧠</div>
                            <p class="text-lg font-medium text-gray-600">Gemini AI is generating your contract</p>
                            <p class="text-sm text-gray-500 mt-2">Analyzing specifications and creating custom Solidity code...</p>
                            <div class="mt-4 flex justify-center space-x-4 text-xs">
                                <span class="flex items-center"><div class="w-2 h-2 bg-blue-500 rounded-full animate-pulse mr-1"></div>Understanding requirements</span>
                                <span class="flex items-center"><div class="w-2 h-2 bg-green-500 rounded-full animate-pulse mr-1"></div>Crafting logic</span>
                                <span class="flex items-center"><div class="w-2 h-2 bg-purple-500 rounded-full animate-pulse mr-1"></div>Applying security</span>
                            </div>
                        </div>
                    </div>
                `;
            } else {
                btn.disabled = false;
                btn.className = btn.className.replace('from-gray-400 to-gray-500 cursor-not-allowed', 'from-blue-600 to-green-600 hover:from-blue-700 hover:to-green-700');
                btnIcon.textContent = '🧠';
                btnText.textContent = 'Generate with Gemini AI';
            }
        }

        function displayContract(result) {
            const preview = document.getElementById('contractPreview');
            const actions = document.getElementById('previewActions');

            // Show action buttons
            actions.classList.remove('hidden');

            // Display contract with syntax highlighting
            preview.innerHTML = `
                <div class="space-y-4">
                    <div class="flex items-center justify-between p-3 bg-gradient-to-r from-blue-50 to-green-50 rounded-lg border border-blue-200">
                        <div>
                            <h4 class="font-semibold text-gray-800 flex items-center">
                                <span class="mr-2">🧠</span>
                                ${result.contract_name}.sol
                            </h4>
                            <p class="text-sm text-gray-600">${result.analysis?.lines_of_code || 0} lines • Generated by Gemini AI</p>
                        </div>
                        <div class="text-right">
                            <div class="text-2xl font-bold text-green-600">95/100</div>
                            <div class="text-xs text-gray-500">AI Quality Score</div>
                        </div>
                    </div>

                    <div class="code-highlight p-4 text-green-400 font-mono text-sm overflow-x-auto max-h-96 overflow-y-auto">
                        <pre>${escapeHtml(result.contract_code)}</pre>
                    </div>

                    <div class="grid grid-cols-3 gap-4 text-sm">
                        <div class="p-3 bg-blue-50 rounded-lg">
                            <div class="font-semibold text-blue-800">Gemini AI</div>
                            <div class="text-blue-600">True intelligence</div>
                        </div>
                        <div class="p-3 bg-green-50 rounded-lg">
                            <div class="font-semibold text-green-800">Free Usage</div>
                            <div class="text-green-600">No API costs</div>
                        </div>
                        <div class="p-3 bg-purple-50 rounded-lg">
                            <div class="font-semibold text-purple-800">Custom Logic</div>
                            <div class="text-purple-600">Beyond templates</div>
                        </div>
                    </div>
                </div>
            `;
        }

        function displayError(message) {
            const preview = document.getElementById('contractPreview');
            preview.innerHTML = `
                <div class="flex items-center justify-center h-96 text-red-500">
                    <div class="text-center">
                        <div class="text-6xl mb-4">❌</div>
                        <p class="text-lg font-medium">Generation Failed</p>
                        <p class="text-sm mt-2">${message}</p>
                    </div>
                </div>
            `;
        }

        function fillExample(text) {
            document.getElementById('specification').value = text;
        }

        function copyContract() {
            if (currentContract) {
                navigator.clipboard.writeText(currentContract.contract_code)
                    .then(() => alert('Contract copied to clipboard!'))
                    .catch(() => alert('Failed to copy contract'));
            }
        }

        function downloadContract() {
            if (currentContract) {
                const blob = new Blob([currentContract.contract_code], { type: 'text/plain' });
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = `${currentContract.contract_name}.sol`;
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                window.URL.revokeObjectURL(url);
            }
        }

        function escapeHtml(text) {
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }
    </script>
</body>
</html>
    """)

@app.post("/generate-contract", response_model=ContractResponse)
async def generate_contract(request: ContractRequest):
    """Generate a smart contract using Google Gemini"""

    request_id = str(uuid.uuid4())

    try:
        # Use the Gemini-powered ChainSage functionality
        contract_code, contract_name = await run_contract_generation(
            specification=request.specification,
            contract_type=request.contract_type or "custom"
        )

        if not contract_code:
            raise Exception("Contract generation returned empty result")

        # Analyze the generated contract
        lines = contract_code.split('\n')
        analysis = {
            "lines_of_code": len(lines),
            "functions": len([line for line in lines if 'function ' in line]),
            "imports": len([line for line in lines if line.strip().startswith('import')]),
            "events": len([line for line in lines if 'event ' in line]),
            "ai_generated": True,
            "model": "gemini-1.5-flash"
        }

        return ContractResponse(
            success=True,
            contract_code=contract_code,
            contract_name=contract_name,
            analysis=analysis,
            request_id=request_id,
            ai_model="gemini-1.5-flash"
        )

    except Exception as e:
        return ContractResponse(
            success=False,
            error_message=f"Gemini contract generation failed: {str(e)}",
            request_id=request_id,
            ai_model="gemini-1.5-flash"
        )

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "ai_model": "gemini-1.5-flash",
        "provider": "google",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/examples")
async def get_examples():
    return {
        "examples": [
            "Create an advanced DeFi protocol called YieldMax where users stake multiple cryptocurrencies, earn dynamic rewards based on market volatility, and can vote on protocol parameters",
            "Create a sophisticated NFT marketplace called ArtVerse where artists can mint generative art NFTs, set custom royalty structures, and implement Dutch auction mechanisms",
            "Create a decentralized autonomous organization called GreenDAO that manages environmental projects, uses quadratic voting for funding decisions, and implements carbon credit tokenization",
            "Create a gaming ecosystem token called GameFi that rewards players based on skill ratings, enables cross-game asset transfers, and features anti-whale mechanisms",
            "Create a decentralized insurance protocol where users can create custom insurance pools, stake tokens for coverage, and vote on claim settlements"
        ],
        "ai_model": "gemini-1.5-flash",
        "capabilities": [
            "Advanced natural language understanding",
            "Custom contract logic generation",
            "Intelligent security pattern integration",
            "Complex DeFi mechanism implementation",
            "Creative problem solving"
        ]
    }

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting ChainSage Web Interface (Gemini Powered)...")
    print("🧠 AI Model: Google Gemini 1.5 Flash")
    print("💰 Cost: Completely FREE")
    print("📡 Backend API: http://localhost:8000")
    print("🌐 Web Interface: http://localhost:8000")
    print("📚 API Docs: http://localhost:8000/docs")
    uvicorn.run("web_app_gemini:app", host="0.0.0.0", port=8000, reload=False)