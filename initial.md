## FEATURE:

Agentic AI app with Web UI + CLI: Natural-language → Solidity smart contracts (generator) and AI audit assistant (issues, severities, diffs).

Primary Orchestrator + Subagents:

Generation Subagent: turns NL specs into Solidity (prefers OpenZeppelin, emits events, access control).

Audit Subagent: LLM-based security review (+ optional Slither/Surya hooks) and patch proposals.

Web UI (Next.js + Tailwind) for: spec input, code editor preview, run audit, view issues table, apply patches, and download artifacts.

Backend API (FastAPI) reusing the same agent logic used by the CLI.

CLI for power users: gen, audit, patch, and scaffold tests.

Outputs: /out/ folder with contracts (.sol), audit report (.md), and patches (.diff).

Env management: python-dotenv + load_env() to load .env across CLI/API.

## EXAMPLES:

In the examples/ folder, there will be a README to help you understand what the example covers and how to structure your own README when you create documentation for this feature.

examples/cli.py — use as a template for the CLI entry point (your version lives at chainsage/cli.py).

examples/agent/ — read through all files to learn best practices for agent interfaces, multi-provider/LLM support, dependency management, and tool registration.

Don’t copy these examples directly (they’re for a different project). Use them as inspiration for clean interfaces, DI, and streaming I/O patterns.

## DOCUMENTATION:

Solidity: https://docs.soliditylang.org

OpenZeppelin Contracts: https://docs.openzeppelin.com/contracts

FastAPI: https://fastapi.tiangolo.com

Next.js: https://nextjs.org/docs

Slither (optional static analyzer): https://github.com/crytic/slither

Surya (optional graphs): https://github.com/ConsenSys/surya

OpenAI Python SDK (for LLM): https://platform.openai.com/docs

## OTHER CONSIDERATIONS:

Include a .env.example and a README with setup instructions (API keys, local token paths, optional Slither/Surya).

Show the project structure tree in the README (frontend + backend + core/agents + out/).

Virtual environment is already set up with required dependencies.

Use python_dotenv and a central load_env() helper to read .env across CLI and backend.

Security: AI audit is advisory; always run static tools/tests and do manual review before production.

Persistence: By default, artifacts are written to out/; optionally wire a DB if multi-user web sessions are needed.