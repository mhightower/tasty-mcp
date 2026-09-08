"""MCP server exposing educational options strategy knowledge."""

from __future__ import annotations

import json

from mcp.server.fastmcp import FastMCP

from .strategies import (
    REFERENCE_URL,
    find_matching_strategies,
    get_strategy_by_name,
    get_strategy_catalog,
)

mcp = FastMCP("tasty-mcp")


@mcp.tool()
def list_options_strategies() -> list[str]:
    """Return the names of the educational strategies listed in the Tastylive strategy index."""
    return [strategy["name"] for strategy in get_strategy_catalog()]


@mcp.tool()
def get_options_strategy(strategy_name: str) -> dict[str, str]:
    """Return a single strategy summary by name or slug from the Tastylive strategy index. Use this for educational lookup only."""
    strategy = get_strategy_by_name(strategy_name)
    if strategy is None:
        raise ValueError(
            f"Unknown strategy: {strategy_name}. Use list_options_strategies() to see valid options."
        )
    return {
        "name": strategy["name"],
        "slug": strategy["slug"],
        "market_assumption": strategy["market_assumption"],
        "risk_profile": strategy["risk_profile"],
        "summary": strategy["summary"],
        "source": strategy["source"],
    }


@mcp.tool()
def find_strategies_for_market_view(
    direction: str | None = None,
    risk_tolerance: str | None = None,
    volatility: str | None = None,
    strategy_type: str | None = None,
) -> list[dict[str, str]]:
    """Recommend matching strategies from the Tastylive strategy index using direction, risk, volatility, and setup-style filters."""
    matches = find_matching_strategies(
        direction=direction,
        risk_tolerance=risk_tolerance,
        volatility=volatility,
        strategy_type=strategy_type,
    )
    recommendations = []
    for strategy in matches:
        recommendations.append({
            "name": strategy["name"],
            "market_assumption": strategy["market_assumption"],
            "risk_profile": strategy["risk_profile"],
            "volatility_bias": strategy["volatility_bias"],
            "strategy_type": strategy["strategy_type"],
            "why_it_matches": (
                f"The {strategy['name']} strategy is a fit because it is aligned with a {strategy['market_assumption']} viewpoint, "
                f"carries a {strategy['risk_profile']} risk profile, and generally fits a {strategy['volatility_bias']} volatility bias."
            ),
            "source": strategy["source"],
        })

    best_fit = None
    if recommendations:
        best_fit = recommendations[0]
        if len(recommendations) > 1:
            for recommendation in recommendations[1:]:
                if recommendation["strategy_type"] in {"income", "hedged", "directional"}:
                    best_fit = recommendation
                    break

    if best_fit is not None:
        for recommendation in recommendations:
            recommendation["best_fit"] = recommendation["name"] == best_fit["name"]

    return recommendations


@mcp.resource("tasty://strategies")
def strategies_resource() -> str:
    """Provide the full Tastylive strategy-index catalog as a JSON resource for educational lookup."""
    return json.dumps({
        "source": REFERENCE_URL,
        "catalog_type": "Tastylive strategy index",
        "strategies": get_strategy_catalog(),
    }, indent=2)


if __name__ == "__main__":
    mcp.run()
