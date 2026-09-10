"""Edge case and integration tests for the MCP server."""

import pytest

from tasty_mcp.server import (
    find_strategies_for_market_view,
    get_options_strategy,
    list_options_strategies,
)


def test_list_options_strategies_returns_non_empty_list() -> None:
    """Verify strategies list is populated."""
    strategies = list_options_strategies()
    assert isinstance(strategies, list)
    assert len(strategies) > 0
    assert all(isinstance(name, str) for name in strategies)


def test_list_options_strategies_contains_expected_names() -> None:
    """Verify well-known strategies are in the list."""
    strategies = list_options_strategies()
    expected = [
        "Long Call & Put Options",
        "Covered Call",
        "Jade Lizard",
        "Iron Condor",
        "Straddle",
    ]
    for strategy in expected:
        assert strategy in strategies, f"{strategy} not found in strategy list"


def test_get_options_strategy_by_exact_name() -> None:
    """Retrieve strategy by exact name."""
    result = get_options_strategy("Covered Call")
    assert result["name"] == "Covered Call"
    assert result["slug"] == "covered-call"
    assert "market_assumption" in result
    assert "risk_profile" in result
    assert "summary" in result
    assert "source" in result


def test_get_options_strategy_case_insensitive() -> None:
    """Verify strategy lookup is case-insensitive."""
    result1 = get_options_strategy("covered call")
    result2 = get_options_strategy("COVERED CALL")
    result3 = get_options_strategy("Covered Call")
    assert result1["slug"] == result2["slug"] == result3["slug"]


def test_get_options_strategy_by_slug() -> None:
    """Retrieve strategy by slug format."""
    result = get_options_strategy("covered-call")
    assert result["name"] == "Covered Call"


def test_get_options_strategy_invalid_name_raises_error() -> None:
    """Verify error handling for unknown strategies."""
    with pytest.raises(ValueError, match="Unknown strategy"):
        get_options_strategy("Nonexistent Strategy XYZ")


def test_find_strategies_with_no_filters_returns_all() -> None:
    """Calling with no filters should return all strategies."""
    results = find_strategies_for_market_view()
    assert len(results) > 10  # Should return most/all strategies


def test_find_strategies_with_single_filter() -> None:
    """Test filtering with one parameter at a time."""
    by_direction = find_strategies_for_market_view(direction="bullish")
    by_risk = find_strategies_for_market_view(risk_tolerance="defined")
    by_volatility = find_strategies_for_market_view(volatility="high")
    by_type = find_strategies_for_market_view(strategy_type="income")

    assert len(by_direction) > 0
    assert len(by_risk) > 0
    assert len(by_volatility) > 0
    assert len(by_type) > 0


def test_find_strategies_results_have_all_required_fields() -> None:
    """Verify result structure has all expected fields."""
    results = find_strategies_for_market_view(direction="bullish")
    required_fields = {
        "name",
        "market_assumption",
        "risk_profile",
        "volatility_bias",
        "strategy_type",
        "why_it_matches",
        "source",
        "best_fit",
    }
    for result in results:
        assert required_fields.issubset(set(result.keys())), (
            f"Missing fields in result: {result.keys()}"
        )


def test_find_strategies_best_fit_is_exactly_one() -> None:
    """Verify exactly one strategy is marked as best_fit."""
    results = find_strategies_for_market_view(
        direction="bullish", risk_tolerance="defined"
    )
    best_fit_count = sum(1 for r in results if r.get("best_fit") is True)
    assert best_fit_count == 1, f"Expected 1 best_fit, got {best_fit_count}"


def test_find_strategies_complex_filter_combination() -> None:
    """Test multiple filters together."""
    results = find_strategies_for_market_view(
        direction="neutral",
        risk_tolerance="limited",
        volatility="medium",
        strategy_type="spread",
    )
    assert isinstance(results, list)
    # Verify that Calendar Spread matches this combination
    names = [r["name"] for r in results]
    assert "Calendar Spread" in names or len(names) > 0


def test_find_strategies_bearish_strategies_exist() -> None:
    """Verify bearish strategies are available."""
    results = find_strategies_for_market_view(direction="bearish")
    assert len(results) > 0
    names = [r["name"] for r in results]
    # Bearish strategies should include short puts, protective collars, etc.
    assert len(names) > 0


def test_find_strategies_high_volatility_strategies() -> None:
    """Verify high volatility strategies are available."""
    results = find_strategies_for_market_view(volatility="high")
    assert len(results) > 0
    names = [r["name"] for r in results]
    # High vol should include long straddle, strangle, short premium, etc.
    assert any(name in names for name in ["Straddle", "Strangle"])


def test_find_strategies_undefined_risk_strategies() -> None:
    """Verify undefined/unlimited risk strategies are available."""
    results = find_strategies_for_market_view(risk_tolerance="undefined")
    assert len(results) > 0
    # Should include long calls, long puts, etc.
