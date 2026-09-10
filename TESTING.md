# MCP Testing Guide

Complete guide to testing the tasty-mcp MCP server.

## Quick Start Testing

### 1. **Unit & Integration Tests** (Recommended)
```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test file
python -m pytest tests/test_edge_cases.py -v

# Run with coverage report
python -m pytest tests/ --cov=tasty_mcp --cov-report=term-missing

# Run specific test
python -m pytest tests/test_strategies.py::test_lookup_by_slug_and_name -v
```

**Status**: ✅ 27 tests, 94.44% coverage

---

### 2. **Interactive Testing** (Manual exploration)
```bash
python test_client.py
```

This runs through all MCP tools with formatted output:
- `list_options_strategies()` - Lists all 14 strategies
- `get_options_strategy(name)` - Retrieves strategy details
- `find_strategies_for_market_view()` - Filters with various criteria
- `strategies_resource()` - JSON export test

---

### 3. **Performance Benchmarking** (Load testing)
```bash
python test_performance.py
```

Measures:
- Individual tool performance
- Throughput under realistic usage patterns
- Stress test with 200+ concurrent-like operations

**Baseline Results**:
- `list_options_strategies()`: 244,978 ops/sec
- `get_options_strategy()`: 609,013 ops/sec
- `find_strategies_for_market_view()`: 105,086 ops/sec
- Overall throughput: 127,121 ops/sec

---

## Advanced Testing Scenarios

### Test Specific Filter Combinations
```python
from tasty_mcp.server import find_strategies_for_market_view

# Bullish with defined risk and low volatility
results = find_strategies_for_market_view(
    direction="bullish",
    risk_tolerance="defined", 
    volatility="low"
)

# Income strategies only
income = find_strategies_for_market_view(strategy_type="income")

# High volatility strategies
high_vol = find_strategies_for_market_view(volatility="high")
```

### Test Error Handling
```python
from tasty_mcp.server import get_options_strategy

# This should raise ValueError
try:
    get_options_strategy("Invalid Strategy Name")
except ValueError as e:
    print(f"✅ Error handling works: {e}")
```

---

## VS Code MCP Integration Testing

Your MCP server is configured in `.vscode/mcp.json`:

1. **Open MCP Inspector**
   - Command Palette: "MCP: Open Inspector"
   - Test tools live in VS Code

2. **Use in Copilot Chat**
   - Tools should auto-suggest in chat context
   - Test with prompts like: "What strategies work for bearish outlook?"

3. **Inline Completions**
   - Tools available for inline code suggestions

---

## Test Coverage Details

### Current Coverage: 94.44%

| Module | Coverage |
|--------|----------|
| `__init__.py` | 100% ✅ |
| `__main__.py` | 100% ✅ |
| `server.py` | 95% (missing resource path branches) |
| `strategies.py` | 94% (missing edge conditions) |

### What's Tested

✅ All 3 MCP tools
✅ Resource endpoint
✅ All filter combinations
✅ Error cases and validation
✅ Data structure contracts
✅ Edge cases (case-insensitivity, slug lookup, etc.)

---

## Adding More Tests

### Template for New Test
```python
def test_my_feature() -> None:
    """Describe what you're testing."""
    from tasty_mcp.server import find_strategies_for_market_view
    
    # Setup
    results = find_strategies_for_market_view(direction="bullish")
    
    # Assert
    assert len(results) > 0
    assert all("name" in r for r in results)
```

Add to `tests/test_edge_cases.py` or create new file in `tests/`.

---

## Continuous Testing Workflow

```bash
# 1. Make changes to code
# 2. Run quick tests
python -m pytest tests/ -q

# 3. Check coverage
python -m pytest tests/ --cov=tasty_mcp

# 4. Run interactive tests
python test_client.py

# 5. Benchmark performance
python test_performance.py

# 6. Format and lint
ruff check --fix .
ruff format .
```

---

## Debugging Failed Tests

```bash
# Show full output and traceback
python -m pytest tests/test_file.py -vv -s

# Stop at first failure
python -m pytest tests/ -x

# Show local variables on failure
python -m pytest tests/ -l

# Run with print statements visible
python -m pytest tests/ -s
```

---

## Checklist Before Deployment

- [ ] `python -m pytest tests/` - All tests pass
- [ ] Coverage > 85% - Run `pytest --cov`
- [ ] `ruff check .` - No linting errors
- [ ] `ruff format --check .` - Code formatted
- [ ] `python test_client.py` - Manual smoke test
- [ ] Server starts: `python -m tasty_mcp`

---

## Quick Reference: Test Files

| File | Purpose | Run With |
|------|---------|----------|
| `test_strategies.py` | Core strategy logic | `pytest tests/test_strategies.py` |
| `test_server_contract.py` | MCP tool contracts | `pytest tests/test_server_contract.py` |
| `test_edge_cases.py` | Edge cases & filters | `pytest tests/test_edge_cases.py` |
| `test_client.py` | Interactive testing | `python test_client.py` |
| `test_performance.py` | Performance benchmarks | `python test_performance.py` |

---

Generated: 2026-09-08
