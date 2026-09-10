"""Interactive MCP server testing client."""

from tasty_mcp.server import (
    find_strategies_for_market_view,
    get_options_strategy,
    list_options_strategies,
    strategies_resource,
)


def test_tool_list_strategies() -> None:
    """Test: list_options_strategies()"""
    print("\n🔹 Testing: list_options_strategies()")
    print("=" * 60)
    strategies = list_options_strategies()
    print(f"Found {len(strategies)} strategies:")
    for strategy in strategies:
        print(f"  • {strategy}")


def test_tool_get_strategy() -> None:
    """Test: get_options_strategy(strategy_name)"""
    print("\n🔹 Testing: get_options_strategy('Covered Call')")
    print("=" * 60)
    result = get_options_strategy("Covered Call")
    for key, value in result.items():
        print(f"  {key}: {value}")


def test_tool_find_bullish() -> None:
    """Test: find_strategies_for_market_view(direction='bullish', ...)"""
    print("\n🔹 Testing: find_strategies_for_market_view(direction='bullish')")
    print("=" * 60)
    results = find_strategies_for_market_view(direction="bullish")
    print(f"Found {len(results)} bullish strategies:")
    for strategy in results:
        best = "⭐ BEST FIT" if strategy["best_fit"] else ""
        print(f"  • {strategy['name']} {best}")
        print(f"    → {strategy['why_it_matches']}")


def test_tool_find_income() -> None:
    """Test: find_strategies_for_market_view(strategy_type='income')"""
    print("\n🔹 Testing: find_strategies_for_market_view(strategy_type='income')")
    print("=" * 60)
    results = find_strategies_for_market_view(strategy_type="income")
    print(f"Found {len(results)} income strategies:")
    for strategy in results:
        print(f"  • {strategy['name']}")
        print(f"    Risk: {strategy['risk_profile']}")
        print(f"    Volatility: {strategy['volatility_bias']}")


def test_tool_complex_filter() -> None:
    """Test: Complex filter combination"""
    print(
        "\n🔹 Testing: find_strategies_for_market_view("
        "direction='bearish', risk_tolerance='defined', volatility='high')"
    )
    print("=" * 60)
    results = find_strategies_for_market_view(
        direction="bearish", risk_tolerance="defined", volatility="high"
    )
    print(f"Found {len(results)} strategies matching criteria:")
    for strategy in results:
        print(f"  • {strategy['name']}")


def test_resource_strategies() -> None:
    """Test: strategies_resource()"""
    print("\n🔹 Testing: strategies_resource() [JSON export]")
    print("=" * 60)
    resource = strategies_resource()
    import json

    data = json.loads(resource)
    print(f"Resource type: {data['catalog_type']}")
    print(f"Source: {data['source']}")
    print(f"Strategies in resource: {len(data['strategies'])}")


def run_all_tests() -> None:
    """Run all interactive tests."""
    print("\n" + "=" * 60)
    print("🧪 TASTY MCP SERVER - INTERACTIVE TEST SUITE")
    print("=" * 60)

    test_tool_list_strategies()
    test_tool_get_strategy()
    test_tool_find_bullish()
    test_tool_find_income()
    test_tool_complex_filter()
    test_resource_strategies()

    print("\n" + "=" * 60)
    print("✅ ALL INTERACTIVE TESTS COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    run_all_tests()
