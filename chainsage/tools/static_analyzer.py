"""
Static analysis integration for ChainSage using Slither and Surya.

Provides comprehensive security analysis following research/static-analysis patterns
with Docker wrapper for consistent execution environment.
"""

import asyncio
import json
import logging
import os
import tempfile
import time
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
import subprocess

from ..agents.models import (
    AuditFinding, AuditReport, SecurityLevel, StaticAnalysisResult
)
from ..core.config import get_settings

logger = logging.getLogger(__name__)


class SlitherAnalyzer:
    """
    Slither static analysis tool integration.

    Follows research/static-analysis patterns for 99 built-in detectors
    with JSON output parsing and Docker integration.
    """

    def __init__(self, use_docker: bool = True):
        self.settings = get_settings()
        self.use_docker = use_docker
        self.eth_toolbox_image = self.settings.static_analysis.eth_security_toolbox_image

        # Slither severity mapping from research
        self.severity_mapping = {
            'High': SecurityLevel.HIGH,
            'Medium': SecurityLevel.MEDIUM,
            'Low': SecurityLevel.LOW,
            'Informational': SecurityLevel.LOW,
            'Optimization': SecurityLevel.LOW
        }

        # Critical detectors that should always be flagged
        self.critical_detectors = {
            'reentrancy-eth', 'reentrancy-no-eth', 'reentrancy-unlimited-gas',
            'arbitrary-send-eth', 'controlled-delegatecall', 'weak-prng',
            'suicidal', 'unprotected-upgrade'
        }

    async def analyze_contract(
        self,
        contract_path: str,
        contract_name: str,
        timeout: int = 300
    ) -> StaticAnalysisResult:
        """
        Run Slither analysis on a contract.

        Args:
            contract_path: Path to the Solidity contract file
            contract_name: Name of the contract for reporting
            timeout: Analysis timeout in seconds

        Returns:
            StaticAnalysisResult with findings and metadata
        """
        start_time = time.time()

        try:
            if self.use_docker:
                raw_output, success = await self._run_slither_docker(contract_path, timeout)
            else:
                raw_output, success = await self._run_slither_local(contract_path, timeout)

            if not success:
                return StaticAnalysisResult(
                    tool_name="slither",
                    contract_name=contract_name,
                    findings=[],
                    raw_output=raw_output,
                    execution_successful=False,
                    error_message="Slither execution failed",
                    analysis_duration=time.time() - start_time
                )

            # Parse Slither JSON output
            findings = self._parse_slither_output(raw_output, contract_name)

            return StaticAnalysisResult(
                tool_name="slither",
                contract_name=contract_name,
                findings=findings,
                raw_output=raw_output,
                execution_successful=True,
                analysis_duration=time.time() - start_time
            )

        except Exception as e:
            logger.error(f"Slither analysis failed: {str(e)}")
            return StaticAnalysisResult(
                tool_name="slither",
                contract_name=contract_name,
                findings=[],
                raw_output=str(e),
                execution_successful=False,
                error_message=str(e),
                analysis_duration=time.time() - start_time
            )

    async def _run_slither_docker(
        self,
        contract_path: str,
        timeout: int
    ) -> Tuple[str, bool]:
        """Run Slither using Docker container."""

        # Create temporary directory for contract and output
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)

            # Copy contract to temp directory
            contract_file = temp_path / "contract.sol"
            with open(contract_path, 'r') as src, open(contract_file, 'w') as dst:
                dst.write(src.read())

            # Prepare output file
            output_file = temp_path / "slither_output.json"

            # Build Docker command following research patterns
            docker_cmd = [
                "docker", "run", "--rm",
                "-v", f"{temp_path}:/contracts",
                self.eth_toolbox_image,
                "slither", "/contracts/contract.sol",
                "--json", "/contracts/slither_output.json",
                "--disable-color",
                "--exclude-informational",  # Focus on security issues
                "--exclude-optimization",   # Exclude optimization for security focus
                "--exclude-dependencies"    # Exclude library issues
            ]

            try:
                # Run Slither with timeout
                process = await asyncio.create_subprocess_exec(
                    *docker_cmd,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE
                )

                stdout, stderr = await asyncio.wait_for(
                    process.communicate(),
                    timeout=timeout
                )

                # Read JSON output if it exists
                if output_file.exists():
                    with open(output_file, 'r') as f:
                        return f.read(), True
                else:
                    # Return stderr if no JSON output
                    error_output = stderr.decode('utf-8') if stderr else "No output generated"
                    logger.warning(f"No JSON output from Slither: {error_output}")
                    return error_output, False

            except asyncio.TimeoutError:
                logger.error(f"Slither analysis timed out after {timeout}s")
                return f"Analysis timed out after {timeout}s", False

            except Exception as e:
                logger.error(f"Docker execution failed: {str(e)}")
                return str(e), False

    async def _run_slither_local(
        self,
        contract_path: str,
        timeout: int
    ) -> Tuple[str, bool]:
        """Run Slither using local installation."""

        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as output_file:
            output_path = output_file.name

        try:
            cmd = [
                self.settings.static_analysis.slither_path,
                contract_path,
                "--json", output_path,
                "--disable-color",
                "--exclude-informational",
                "--exclude-optimization"
            ]

            process = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )

            stdout, stderr = await asyncio.wait_for(
                process.communicate(),
                timeout=timeout
            )

            # Read JSON output
            if os.path.exists(output_path):
                with open(output_path, 'r') as f:
                    result = f.read()
                os.unlink(output_path)  # Cleanup
                return result, True
            else:
                error_msg = stderr.decode('utf-8') if stderr else "No output generated"
                return error_msg, False

        except asyncio.TimeoutError:
            return f"Analysis timed out after {timeout}s", False
        except Exception as e:
            return str(e), False
        finally:
            if os.path.exists(output_path):
                os.unlink(output_path)

    def _parse_slither_output(self, json_output: str, contract_name: str) -> List[AuditFinding]:
        """Parse Slither JSON output into AuditFinding objects."""
        findings = []

        try:
            data = json.loads(json_output)
            detectors = data.get('results', {}).get('detectors', [])

            for i, detector in enumerate(detectors):
                # Extract detector information
                check_name = detector.get('check', 'unknown')
                impact = detector.get('impact', 'Low')
                confidence = detector.get('confidence', 'Medium')
                description = detector.get('description', '')
                markdown = detector.get('markdown', '')

                # Map Slither severity to our SecurityLevel
                severity = self.severity_mapping.get(impact, SecurityLevel.LOW)

                # Upgrade severity for critical detectors
                if check_name in self.critical_detectors:
                    severity = SecurityLevel.CRITICAL

                # Extract location information
                elements = detector.get('elements', [])
                location = self._extract_location(elements)

                # Generate recommendation based on detector type
                recommendation = self._generate_recommendation(check_name, description)

                # Create audit finding
                finding = AuditFinding(
                    id=f"slither-{check_name}-{i}",
                    severity=severity,
                    title=f"Slither: {check_name.replace('-', ' ').title()}",
                    description=description or markdown,
                    location=location,
                    recommendation=recommendation,
                    detector_type="slither",
                    confidence=self._map_confidence(confidence),
                    code_snippet=self._extract_code_snippet(elements)
                )

                findings.append(finding)

        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse Slither output: {e}")
            # Create a single finding for the parsing error
            findings.append(AuditFinding(
                id="slither-parse-error",
                severity=SecurityLevel.MEDIUM,
                title="Slither Analysis Error",
                description=f"Failed to parse Slither output: {str(e)}",
                location="N/A",
                recommendation="Review Slither configuration and contract syntax",
                detector_type="slither"
            ))

        except Exception as e:
            logger.error(f"Unexpected error parsing Slither output: {e}")

        return findings

    def _extract_location(self, elements: List[Dict]) -> str:
        """Extract location information from Slither elements."""
        locations = []

        for element in elements:
            if element.get('type') == 'function':
                name = element.get('name', 'unknown')
                source_mapping = element.get('source_mapping', {})
                if source_mapping:
                    filename = source_mapping.get('filename_short', 'contract')
                    line = source_mapping.get('lines', [0])[0] if source_mapping.get('lines') else 0
                    locations.append(f"{filename}:{line} ({name})")
                else:
                    locations.append(f"function {name}")

            elif element.get('type') == 'variable':
                name = element.get('name', 'unknown')
                locations.append(f"variable {name}")

        return ", ".join(locations) if locations else "N/A"

    def _extract_code_snippet(self, elements: List[Dict]) -> Optional[str]:
        """Extract relevant code snippet from elements."""
        for element in elements:
            source_mapping = element.get('source_mapping', {})
            if 'content' in source_mapping:
                return source_mapping['content'][:200] + "..." if len(source_mapping['content']) > 200 else source_mapping['content']

        return None

    def _map_confidence(self, slither_confidence: str) -> float:
        """Map Slither confidence to 0.0-1.0 scale."""
        confidence_map = {
            'High': 0.9,
            'Medium': 0.7,
            'Low': 0.5
        }
        return confidence_map.get(slither_confidence, 0.5)

    def _generate_recommendation(self, check_name: str, description: str) -> str:
        """Generate recommendations based on detector type."""

        # Common recommendations based on research patterns
        recommendations = {
            'reentrancy-eth': 'Use ReentrancyGuard modifier and follow checks-effects-interactions pattern',
            'reentrancy-no-eth': 'Use ReentrancyGuard modifier to prevent reentrancy attacks',
            'arbitrary-send-eth': 'Validate recipient addresses and use pull payment pattern',
            'controlled-delegatecall': 'Avoid delegatecall to user-controlled addresses',
            'weak-prng': 'Use secure randomness source (e.g., Chainlink VRF) instead of block properties',
            'suicidal': 'Remove selfdestruct or add proper access controls',
            'unprotected-upgrade': 'Add proper access controls to upgrade functions',
            'missing-zero-check': 'Add zero address validation for critical addresses',
            'locked-ether': 'Add withdrawal mechanism or remove payable functions',
            'timestamp-dependence': 'Avoid using block.timestamp for critical logic',
            'tx-origin': 'Use msg.sender instead of tx.origin for authentication'
        }

        return recommendations.get(check_name,
            f"Review the {check_name.replace('-', ' ')} issue and follow security best practices")


class SuryaAnalyzer:
    """
    Surya static analysis tool integration for contract visualization.

    Provides graph generation and structural analysis capabilities.
    """

    def __init__(self, use_docker: bool = True):
        self.settings = get_settings()
        self.use_docker = use_docker

    async def generate_contract_graph(
        self,
        contract_path: str,
        output_dir: str = None
    ) -> Tuple[bool, str, str]:
        """
        Generate contract inheritance and call graphs.

        Returns:
            Tuple of (success, graph_path, error_message)
        """
        if not output_dir:
            output_dir = self.settings.output.base_dir

        try:
            if self.use_docker:
                return await self._generate_graph_docker(contract_path, output_dir)
            else:
                return await self._generate_graph_local(contract_path, output_dir)

        except Exception as e:
            logger.error(f"Surya graph generation failed: {e}")
            return False, "", str(e)

    async def _generate_graph_docker(
        self,
        contract_path: str,
        output_dir: str
    ) -> Tuple[bool, str, str]:
        """Generate graph using Docker."""

        output_path = Path(output_dir) / f"contract_graph_{int(time.time())}.png"

        docker_cmd = [
            "docker", "run", "--rm",
            "-v", f"{os.path.dirname(contract_path)}:/contracts",
            "-v", f"{output_dir}:/output",
            self.settings.static_analysis.eth_security_toolbox_image,
            "surya", "graph",
            f"/contracts/{os.path.basename(contract_path)}",
            "|", "dot", "-Tpng", ">", f"/output/{output_path.name}"
        ]

        try:
            process = await asyncio.create_subprocess_exec(
                *docker_cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )

            stdout, stderr = await process.communicate()

            if output_path.exists():
                return True, str(output_path), ""
            else:
                error_msg = stderr.decode('utf-8') if stderr else "Graph generation failed"
                return False, "", error_msg

        except Exception as e:
            return False, "", str(e)

    async def _generate_graph_local(
        self,
        contract_path: str,
        output_dir: str
    ) -> Tuple[bool, str, str]:
        """Generate graph using local installation."""
        # Simplified local implementation
        return False, "", "Local Surya support not implemented"


class StaticAnalysisManager:
    """
    Manager for coordinating multiple static analysis tools.

    Aggregates results from Slither and Surya following research patterns.
    """

    def __init__(self, use_docker: bool = True):
        self.slither = SlitherAnalyzer(use_docker)
        self.surya = SuryaAnalyzer(use_docker)

    async def comprehensive_analysis(
        self,
        contract_code: str,
        contract_name: str,
        include_visualization: bool = True
    ) -> AuditReport:
        """
        Run comprehensive static analysis using all available tools.

        Args:
            contract_code: Solidity contract source code
            contract_name: Name of the contract
            include_visualization: Whether to generate visual graphs

        Returns:
            Complete AuditReport with all findings
        """
        start_time = time.time()

        # Write contract to temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.sol', delete=False) as temp_file:
            temp_file.write(contract_code)
            contract_path = temp_file.name

        try:
            # Run Slither analysis
            slither_result = await self.slither.analyze_contract(
                contract_path, contract_name
            )

            all_findings = slither_result.findings
            tools_used = ["slither"]

            # Optionally generate visualizations
            graph_path = ""
            if include_visualization:
                success, graph_path, error = await self.surya.generate_contract_graph(
                    contract_path
                )
                if success:
                    tools_used.append("surya")

            # Generate comprehensive report
            report = AuditReport(
                contract_name=contract_name,
                findings=all_findings,
                overall_score=0,  # Will be calculated by Pydantic validator
                summary=self._generate_summary(all_findings),
                tools_used=tools_used,
                recommendations=self._generate_recommendations(all_findings)
            )

            return report

        finally:
            # Cleanup temporary file
            if os.path.exists(contract_path):
                os.unlink(contract_path)

    def _generate_summary(self, findings: List[AuditFinding]) -> str:
        """Generate executive summary of audit findings."""
        if not findings:
            return "No security issues detected by static analysis tools."

        severity_counts = {}
        for finding in findings:
            severity_counts[finding.severity] = severity_counts.get(finding.severity, 0) + 1

        summary = f"Static analysis completed with {len(findings)} findings:\n"

        for severity in [SecurityLevel.CRITICAL, SecurityLevel.HIGH, SecurityLevel.MEDIUM, SecurityLevel.LOW]:
            count = severity_counts.get(severity, 0)
            if count > 0:
                summary += f"- {severity.value.title()}: {count}\n"

        if severity_counts.get(SecurityLevel.CRITICAL, 0) > 0:
            summary += "\n⚠️ CRITICAL issues found - immediate attention required!"
        elif severity_counts.get(SecurityLevel.HIGH, 0) > 0:
            summary += "\n⚠️ HIGH severity issues found - review recommended before deployment."

        return summary

    def _generate_recommendations(self, findings: List[AuditFinding]) -> List[str]:
        """Generate high-level recommendations based on findings."""
        recommendations = []

        critical_count = sum(1 for f in findings if f.severity == SecurityLevel.CRITICAL)
        high_count = sum(1 for f in findings if f.severity == SecurityLevel.HIGH)

        if critical_count > 0:
            recommendations.append("🚨 Address all CRITICAL findings before any deployment")

        if high_count > 0:
            recommendations.append("⚠️ Review and fix HIGH severity issues")

        # Add pattern-based recommendations
        finding_types = {f.id.split('-')[1] if '-' in f.id else f.id for f in findings}

        if any('reentrancy' in ft for ft in finding_types):
            recommendations.append("Implement ReentrancyGuard for all state-changing functions")

        if any('access' in ft for ft in finding_types):
            recommendations.append("Review access control mechanisms and permissions")

        if not findings:
            recommendations.append("✅ Static analysis passed - consider additional manual review")

        return recommendations


if __name__ == "__main__":
    # Test static analysis
    async def test_analysis():
        manager = StaticAnalysisManager(use_docker=True)

        test_contract = '''
        // SPDX-License-Identifier: MIT
        pragma solidity ^0.8.19;

        contract TestContract {
            mapping(address => uint256) public balances;

            function withdraw() public {
                uint amount = balances[msg.sender];
                (bool success, ) = msg.sender.call{value: amount}("");
                require(success);
                balances[msg.sender] = 0; // Potential reentrancy
            }
        }
        '''

        try:
            report = await manager.comprehensive_analysis(test_contract, "TestContract")
            print("✅ Static analysis test completed")
            print(f"📋 Findings: {len(report.findings)}")
            print(f"🏆 Overall score: {report.overall_score}")
            print(f"🔧 Tools used: {report.tools_used}")
        except Exception as e:
            print(f"❌ Analysis failed: {e}")

    asyncio.run(test_analysis())