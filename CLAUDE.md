# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Context

This repository establishes coding standards and tech stack conventions for a set of related projects. `AGENTS.md` is the authoritative reference for development philosophy and standards.

## Technology Stack

### Python (Backend & Scripting)
- **Package manager**: `uv` exclusively — never `pip` directly
- Setup: `uv venv && source .venv/bin/activate && uv sync`
- API framework: FastAPI + Uvicorn
- Web UI framework: Flask
- Type hints required, Python 3.10+ syntax
- Avoid `hatchling.build` in `pyproject.toml`
- Prefer Python scripts over Bash for automation

### AI / ML
- ML/DL: PyTorch (not TensorFlow)
- Agent development: Claude Agent SDK (preferred) or LangChain ≥ 1.0.0 + LangGraph ≥ 1.0.0
- Embeddings: sentence-transformers; model hub: Hugging Face

### Infrastructure
- Database: InterSystems IRIS, instance named `IRIS`
- OS: Linux (Ubuntu LTS); no containers for demo projects

### Frontend
- Charts: lightweight-charts (TradingView)
- Styling: Google Material Design + Bootstrap Icons

## Code Standards

- Functions: < 20 lines ideally, < 100 lines maximum
- SOLID principles are non-negotiable
- No commented-out code, no TODO comments, no unused imports
- No hardcoded values — use config or environment variables
- Fail fast: typed exceptions with clear messages, never silently swallow errors
- Compose over inherit; DRY over copy-paste
- Write clean code from the start — no "clean it up later"

## Communication

- Assume 20+ years of software engineering experience; skip basic explanations
- Focus on *why* decisions were made, not *what* the code does
- Ask for clarification when requirements are ambiguous
