# Tasty MCP

This project is a lightweight Python MCP server for educational options-strategy lookups based on the Tastylive strategy index:

https://www.tastylive.com/concepts-strategies/

It is intentionally scoped to educational/reference use. The server exposes the strategy-index catalog, including entries such as Jade Lizard, Iron Butterfly, and Calendar Spread.

## Included strategies

The project focuses on the Tastylive strategy index and includes a broader set of educational strategy entries:

1. Long Call & Put Options
2. Short Call & Put Options
3. Covered Call
4. Married Put
5. Straddle
6. Strangle
7. Iron Condor
8. Broken Wing Butterfly
9. Protective Collar
10. Diagonal Spread
11. Jade Lizard
12. Iron Butterfly
13. Calendar Spread
14. Zebra

## Quick start

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
pip install -e .
python -m tasty_mcp
```

## MCP tools

- `list_options_strategies()`
- `get_options_strategy(strategy_name: str)`
- `find_strategies_for_market_view(direction: str | None = None, risk_tolerance: str | None = None, volatility: str | None = None, strategy_type: str | None = None)`
- `tasty://strategies` resource

Example:

```python
find_strategies_for_market_view(direction="bullish", risk_tolerance="defined", volatility="low")
```

## Notes

This repository intentionally avoids making trading decisions or executing orders. It focuses on structured strategy discovery and educational summaries.

## Attribution and licensing

This project is an original implementation of an educational MCP server for options strategy lookup. It references publicly available materials from Tastylive, including the article:

https://www.tastylive.com/concepts-strategies/10-options-strategies-every-trader-should-know

The code in this repository is licensed under the MIT License. This does not imply ownership of Tastylive content or website materials; the source article is cited for reference and educational context only.
