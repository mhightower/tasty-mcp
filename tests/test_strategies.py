from tasty_mcp.server import find_strategies_for_market_view
from tasty_mcp.strategies import (
    REFERENCE_URL,
    find_matching_strategies,
    get_strategy_by_name,
    get_strategy_catalog,
)


def test_reference_url_matches_strategy_index() -> None:
    assert REFERENCE_URL == "https://www.tastylive.com/concepts-strategies/"


def test_strategy_catalog_contains_strategy_index_entries() -> None:
    strategies = get_strategy_catalog()
    assert len(strategies) >= 10
    names = [s["name"] for s in strategies]
    assert "Jade Lizard" in names
    assert "Iron Butterfly" in names
    assert "Calendar Spread" in names
    assert [s["name"] for s in strategies][:10] == [
        "Long Call & Put Options",
        "Short Call & Put Options",
        "Covered Call",
        "Married Put",
        "Straddle",
        "Strangle",
        "Iron Condor",
        "Broken Wing Butterfly",
        "Protective Collar",
        "Diagonal Spread",
    ]


def test_lookup_by_slug_and_name() -> None:
    assert get_strategy_by_name("covered call")["slug"] == "covered-call"
    assert get_strategy_by_name("straddle")["name"] == "Straddle"
    assert get_strategy_by_name("jade lizard")["name"] == "Jade Lizard"


def test_find_matching_strategies_for_bullish_and_defined_risk() -> None:
    matches = find_matching_strategies(direction="bullish", risk_tolerance="defined")
    names = [m["name"] for m in matches]
    assert "Long Call & Put Options" in names
    assert "Covered Call" in names
    assert "Married Put" in names
    assert "Protective Collar" in names


def test_find_matching_strategies_for_neutral_range() -> None:
    matches = find_matching_strategies(direction="neutral", risk_tolerance="limited")
    assert "Iron Condor" in [m["name"] for m in matches]
    assert "Strangle" in [m["name"] for m in matches]


def test_find_matching_strategies_for_low_volatility_income_strategies() -> None:
    matches = find_matching_strategies(volatility="low", strategy_type="income")
    assert [m["name"] for m in matches] == [
        "Covered Call",
        "Iron Condor",
        "Jade Lizard",
        "Iron Butterfly",
    ]


def test_find_matching_strategies_for_high_volatility() -> None:
    matches = find_matching_strategies(volatility="high")
    assert "Straddle" in [m["name"] for m in matches]
    assert "Strangle" in [m["name"] for m in matches]
    assert "Short Call & Put Options" in [m["name"] for m in matches]


def test_best_fit_markers_are_set_on_matches() -> None:
    matches = find_matching_strategies(direction="bullish", risk_tolerance="defined")
    assert any(match["name"] == "Covered Call" for match in matches)
    assert any(match["name"] == "Protective Collar" for match in matches)


def test_server_tool_returns_recommendations_with_best_fit_metadata() -> None:
    recommendations = find_strategies_for_market_view(
        direction="bullish",
        risk_tolerance="defined",
        volatility="low",
    )

    assert recommendations
    assert all("name" in item for item in recommendations)
    assert all("why_it_matches" in item for item in recommendations)
    assert any(item["best_fit"] is True for item in recommendations)
    assert sum(1 for item in recommendations if item.get("best_fit") is True) == 1


def test_server_tool_uses_rationale_and_strategy_type_fields() -> None:
    recommendations = find_strategies_for_market_view(strategy_type="income")
    names = [item["name"] for item in recommendations]
    assert "Covered Call" in names
    assert "Iron Condor" in names
    assert all("strategy_type" in item for item in recommendations)
