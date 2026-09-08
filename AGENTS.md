# AGENTS.md

## Project purpose
This repository is a Python MCP (Model Context Protocol) server for a Tastytrade-style options trading website. The server should expose trading, market, and account-related capabilities to AI clients in a structured, tool-safe way.

Treat this as a production-minded Python project with a strong emphasis on safety, observability, and clear tool boundaries.

## Working conventions
- Prefer Python 3.11+ typed code using `from __future__ import annotations` where helpful.
- Keep code organized under a top-level package such as `src/tasty_mcp/` or a similar package root instead of scattering logic in scripts.
- Use small, explicit modules with clear responsibilities such as:
  - `server.py` or `app.py` for MCP entrypoints
  - `tools/` for MCP tool definitions
  - `services/` for business logic and API integration
  - `models/` for data contracts and validation
  - `config.py` for environment handling
  - `utils/` for shared helpers
- Favor explicit names over clever abstractions; agent-created code should be readable by other engineers without deep project context.

## MCP server design expectations
- Expose tools as narrow, business-oriented actions rather than broad free-form commands.
- Each tool should have clear input schemas, validation, and predictable output models.
- Prefer returning structured JSON-like dictionaries or Pydantic models rather than raw strings when the output is machine-readable.
- For external website or API integrations, isolate the HTTP or scraping logic behind service layers and keep tool handlers thin.
- Do not add tool names that duplicate each other; keep tool semantics stable and easy to discover.

## Data and integration patterns
- Treat the Tastytrade website/API as an external dependency. Build adapters around it rather than embedding ad-hoc requests in tool code.
- Validate all user input before invoking external calls, especially account IDs, symbols, option contracts, dates, and order payloads.
- For trading and account actions, prefer readonly exploration tools and explicit mutation actions, with strong confirmation boundaries if needed.
- Use environment variables for secrets, tokens, session config, base URLs, and feature flags. Never hardcode credentials or API tokens.

## Code quality expectations
- Use type hints for function signatures and return values.
- Favor `asyncio` when the server or client integrations are I/O bound.
- Use `pytest` for unit and integration tests; prefer small tests around tool validation and service behavior.
- Add robust error handling: map external failures to actionable errors, log useful context, and avoid leaking sensitive details in responses.
- Keep side effects explicit and easy to trace. If a tool writes state or triggers an order flow, document the effect in the tool description.

## Tooling and commands
Assume a standard Python project layout and use the following conventions unless the repo later adds explicit project configuration:
- Create a virtual environment with `python -m venv .venv`
- Install project dependencies with `pip install -r requirements.txt` or `pip install -e .` when packaging is configured
- Run the server with the project’s primary entrypoint, usually something like `python -m tasty_mcp` or `uvicorn ...` if a web interface is added
- Run tests with `pytest`
- Run lint/format checks with `ruff check .` and `ruff format .` if those tools are used

If project tooling is not present yet, do not invent a large framework stack without a clear need. Prefer a minimal, maintainable Python setup.

## Security and compliance guardrails
- Never log secrets, tokens, cookies, or raw user credentials.
- Treat all data as sensitive: avoid printing account, order, or portfolio details in unredacted logs.
- Validate and constrain tool arguments to reduce misuse and injection risks.
- If any feature is financial-risk related, require explicit confirmation or a safety gate before actions that can change state.

## Repository hygiene
- Keep documentation concise and code-first. Prefer updating the README or docs when behavior, configuration, or tool contracts change.
- If adding new tools, update any relevant tool documentation or examples in the same change.
- Do not add large generated files or lock-step dependencies unless the project clearly requires them.

## Preferred implementation style for AI agents
When making changes in this repo:
1. Start by identifying the nearest existing module and keep the change consistent with it.
2. Prefer additive, narrow changes over broad refactors.
3. Validate changes with the smallest relevant tests or smoke checks.
4. Keep tool contracts stable and well described so MCP clients can rely on them.
5. If uncertainty remains, favor safe defaults and explicit error messages over magical behavior.

## Useful starting structure
A clean baseline for this project looks like:
- `src/tasty_mcp/server.py`
- `src/tasty_mcp/config.py`
- `src/tasty_mcp/tools/`
- `src/tasty_mcp/services/`
- `src/tasty_mcp/models/`
- `tests/`
- `README.md`

This is a guide, not a requirement to over-engineer. The important thing is clarity, safety, and a stable MCP tool surface.
