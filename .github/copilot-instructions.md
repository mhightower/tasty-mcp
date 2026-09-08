# Copilot instructions for this MCP project

## Python MCP references

This repository implements a Python MCP server using the official Python SDK from the Model Context Protocol project.

Primary references:
- https://github.com/modelcontextprotocol/python-sdk
- https://modelcontextprotocol.io/docs/learn/server
- https://modelcontextprotocol.io/docs/learn/architecture
- https://modelcontextprotocol.io/docs/tools/concepts

## Local development

- Use the project virtual environment in `.venv`
- Run the server with: `python -m tasty_mcp`
- The MCP config is defined in `.vscode/mcp.json`
- Prefer stdio transport for local editor integration

## Project conventions

- Keep tools narrow and business-oriented
- Validate inputs before external calls
- Return structured dictionaries or JSON-serializable results
- Keep educational data sourced and attributed
- Treat this as a read-only strategy reference server, not a trading executor
