#!/usr/bin/env python3
"""
ChainSage Web Interface - FastAPI Backend
Provides REST API endpoints for the ChainSage smart contract generator
"""

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import asyncio
import json
import os
import sys
from pathlib import Path
from datetime import datetime
import traceback
import uuid

# Add the parent directory to Python path to import ChainSage modules
sys.path.insert(0, str(Path(__file__).parent.parent))

app = FastAPI(
    title="ChainSage Web Interface",
    description="Agentic AI Smart Contract Generator & Auditor - Web Interface",
    version="1.0.0"
)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response Models
class ContractGenerationRequest(BaseModel):
    specification: str
    contract_type: Optional[str] = "custom"
    security_features: Optional[List[str]] = []
    additional_options: Optional[Dict[str, Any]] = {}

class ContractGenerationResponse(BaseModel):
    success: bool
    contract_code: Optional[str] = None
    contract_name: Optional[str] = None
    file_path: Optional[str] = None
    analysis: Optional[Dict[str, Any]] = None
    error_message: Optional[str] = None
    generation_time: Optional[float] = None
    request_id: str

class AnalysisRequest(BaseModel):
    contract_code: str
    contract_name: Optional[str] = "Contract"

class AnalysisResponse(BaseModel):
    success: bool
    vulnerabilities: Optional[List[Dict[str, Any]]] = None
    recommendations: Optional[List[str]] = None
    security_score: Optional[int] = None
    error_message: Optional[str] = None

# Storage for ongoing requests
generation_requests: Dict[str, Dict[str, Any]] = {}

@app.get("/")
async def read_root():
    return {
        "message": "ChainSage Web Interface API",
        "version": "1.0.0",
        "status": "operational",
        "endpoints": [
            "/generate-contract",
            "/analyze-contract",
            "/get-contract-types",
            "/get-security-features",
            "/download-contract/{request_id}",
            "/request-status/{request_id}"
        ]
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "chainsage-web-api"
    }

@app.get("/get-contract-types")
async def get_contract_types():
    """Get available contract types"""
    return {
        "contract_types": [
            {
                "value": "erc20",
                "label": "ERC20 Token",
                "description": "Fungible tokens (cryptocurrencies, loyalty points, etc.)"
            },
            {
                "value": "erc721",
                "label": "ERC721 NFT",
                "description": "Non-fungible tokens (digital art, collectibles, etc.)"
            },
            {
                "value": "erc1155",
                "label": "ERC1155 Multi-Token",
                "description": "Multi-token standard (gaming items, mixed collections)"
            },
            {
                "value": "governance",
                "label": "Governance Contract",
                "description": "DAO voting and governance systems"
            },
            {
                "value": "defi",
                "label": "DeFi Protocol",
                "description": "Decentralized finance (DEX, lending, staking)"
            },
            {
                "value": "custom",
                "label": "Custom Contract",
                "description": "Custom logic contracts (escrow, multi-sig, etc.)"
            }
        ]
    }

@app.get("/get-security-features")
async def get_security_features():
    """Get available security features"""
    return {
        "security_features": [
            {
                "value": "mintable",
                "label": "Mintable",
                "description": "Allow creation of new tokens by authorized addresses"
            },
            {
                "value": "burnable",
                "label": "Burnable",
                "description": "Allow token holders to destroy their tokens"
            },
            {
                "value": "pausable",
                "label": "Pausable",
                "description": "Emergency pause functionality for all operations"
            },
            {
                "value": "votes",
                "label": "Voting Power",
                "description": "Enable governance voting capabilities"
            },
            {
                "value": "access_control",
                "label": "Role-Based Access",
                "description": "Advanced role-based permission system"
            },
            {
                "value": "upgradeable",
                "label": "Upgradeable",
                "description": "Allow contract upgrades via proxy pattern"
            }
        ]
    }

@app.post("/generate-contract", response_model=ContractGenerationResponse)
async def generate_contract(
    request: ContractGenerationRequest,
    background_tasks: BackgroundTasks
):
    """Generate a smart contract from natural language specification"""

    request_id = str(uuid.uuid4())
    start_time = datetime.now()

    try:
        # Initialize request tracking
        generation_requests[request_id] = {
            "status": "processing",
            "start_time": start_time,
            "request": request.dict()
        }

        # Import and run ChainSage generation
        from run_chainsage import run_contract_generation

        contract_code, contract_name = await run_contract_generation(
            specification=request.specification,
            contract_type=request.contract_type or "custom"
        )

        # Calculate generation time
        generation_time = (datetime.now() - start_time).total_seconds()

        # Save contract file
        output_dir = Path("out/contracts")
        output_dir.mkdir(parents=True, exist_ok=True)
        file_path = output_dir / f"{contract_name}.sol"

        # Perform basic analysis
        analysis = analyze_generated_contract(contract_code)

        # Update request status
        generation_requests[request_id].update({
            "status": "completed",
            "contract_code": contract_code,
            "contract_name": contract_name,
            "file_path": str(file_path),
            "analysis": analysis,
            "generation_time": generation_time
        })

        return ContractGenerationResponse(
            success=True,
            contract_code=contract_code,
            contract_name=contract_name,
            file_path=str(file_path),
            analysis=analysis,
            generation_time=generation_time,
            request_id=request_id
        )

    except Exception as e:
        error_message = f"Contract generation failed: {str(e)}"

        # Update request status with error
        generation_requests[request_id].update({
            "status": "error",
            "error_message": error_message
        })

        return ContractGenerationResponse(
            success=False,
            error_message=error_message,
            request_id=request_id
        )

@app.post("/analyze-contract", response_model=AnalysisResponse)
async def analyze_contract(request: AnalysisRequest):
    """Analyze a smart contract for security vulnerabilities"""

    try:
        # Perform static analysis (mock implementation)
        vulnerabilities = [
            {
                "type": "reentrancy",
                "severity": "medium",
                "line": 45,
                "description": "Potential reentrancy vulnerability in transfer function",
                "recommendation": "Add ReentrancyGuard modifier"
            },
            {
                "type": "access-control",
                "severity": "high",
                "line": 23,
                "description": "Missing access control on critical function",
                "recommendation": "Add onlyOwner modifier"
            }
        ]

        recommendations = [
            "Consider adding comprehensive unit tests",
            "Implement proper error handling for edge cases",
            "Add events for important state changes",
            "Consider gas optimization opportunities"
        ]

        security_score = calculate_security_score(request.contract_code, vulnerabilities)

        return AnalysisResponse(
            success=True,
            vulnerabilities=vulnerabilities,
            recommendations=recommendations,
            security_score=security_score
        )

    except Exception as e:
        return AnalysisResponse(
            success=False,
            error_message=f"Contract analysis failed: {str(e)}"
        )

@app.get("/request-status/{request_id}")
async def get_request_status(request_id: str):
    """Get the status of a contract generation request"""

    if request_id not in generation_requests:
        raise HTTPException(status_code=404, detail="Request not found")

    request_data = generation_requests[request_id]
    return {
        "request_id": request_id,
        "status": request_data["status"],
        "start_time": request_data["start_time"].isoformat(),
        "generation_time": request_data.get("generation_time"),
        "contract_name": request_data.get("contract_name"),
        "error_message": request_data.get("error_message")
    }

@app.get("/download-contract/{request_id}")
async def download_contract(request_id: str):
    """Download generated contract file"""

    if request_id not in generation_requests:
        raise HTTPException(status_code=404, detail="Request not found")

    request_data = generation_requests[request_id]

    if request_data["status"] != "completed":
        raise HTTPException(status_code=400, detail="Contract not ready for download")

    file_path = request_data.get("file_path")
    if not file_path or not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Contract file not found")

    return FileResponse(
        path=file_path,
        filename=f"{request_data['contract_name']}.sol",
        media_type="text/plain"
    )

@app.get("/examples")
async def get_examples():
    """Get example contract specifications"""
    return {
        "examples": [
            {
                "title": "Gaming Reward Token",
                "specification": "Create a gaming reward token called GameCoin that players earn for achievements with minting and burning capabilities",
                "type": "erc20",
                "features": ["mintable", "burnable"]
            },
            {
                "title": "Digital Art NFT",
                "specification": "Create an NFT collection called ArtistsNFT for digital artwork with royalty payments and 10000 max supply",
                "type": "erc721",
                "features": []
            },
            {
                "title": "DAO Governance Token",
                "specification": "Create a governance token called DAOToken with voting capabilities and emergency pause functionality for community decisions",
                "type": "erc20",
                "features": ["votes", "pausable"]
            },
            {
                "title": "DeFi Staking Pool",
                "specification": "Create a staking contract where users can stake tokens and earn rewards with compound interest and time locks",
                "type": "defi",
                "features": []
            },
            {
                "title": "Multi-Signature Wallet",
                "specification": "Create a multi-signature wallet contract requiring 3 out of 5 signatures for transactions with daily spending limits",
                "type": "custom",
                "features": ["access_control"]
            }
        ]
    }

# Helper functions
def analyze_generated_contract(contract_code: str) -> Dict[str, Any]:
    """Analyze generated contract and return metrics"""
    lines = contract_code.split('\n')

    return {
        "lines_of_code": len(lines),
        "functions": len([line for line in lines if 'function ' in line]),
        "imports": len([line for line in lines if line.strip().startswith('import')]),
        "events": len([line for line in lines if 'event ' in line]),
        "modifiers": len([line for line in lines if 'modifier ' in line]),
        "estimated_gas": 1200000  # Placeholder
    }

def calculate_security_score(contract_code: str, vulnerabilities: List[Dict]) -> int:
    """Calculate security score based on contract analysis"""
    base_score = 100

    for vuln in vulnerabilities:
        severity = vuln.get("severity", "low")
        if severity == "high":
            base_score -= 20
        elif severity == "medium":
            base_score -= 10
        elif severity == "low":
            base_score -= 5

    return max(0, base_score)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)