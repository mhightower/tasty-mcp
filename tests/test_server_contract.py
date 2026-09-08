import runpy

from tasty_mcp import server as server_module
from tasty_mcp.server import find_strategies_for_market_view


def test_main_module_calls_server_run(monkeypatch) -> None:
    called = {"ran": False}

    def fake_run() -> None:
        called["ran"] = True

    monkeypatch.setattr(server_module.mcp, "run", fake_run)
    runpy.run_module("tasty_mcp.__main__", run_name="__main__")

    assert called["ran"] is True


def test_recommendation_contract_for_bullish_defined_low_volatility() -> None:
    results = find_strategies_for_market_view(
        direction="bullish",
        risk_tolerance="defined",
        volatility="low",
    )

    assert isinstance(results, list)
    assert results

    expected_keys = {
        "name",
        "market_assumption",
        "risk_profile",
        "volatility_bias",
        "strategy_type",
        "why_it_matches",
        "source",
        "best_fit",
    }

    for item in results:
        assert set(item.keys()) == expected_keys
        assert isinstance(item["name"], str)
        assert isinstance(item["market_assumption"], str)
        assert isinstance(item["risk_profile"], str)
        assert isinstance(item["volatility_bias"], str)
        assert isinstance(item["strategy_type"], str)
        assert isinstance(item["why_it_matches"], str)
        assert isinstance(item["source"], str)
        assert isinstance(item["best_fit"], bool)

    names = {item["name"] for item in results}
    assert {"Covered Call", "Married Put", "Protective Collar"}.issubset(names)
    assert sum(1 for item in results if item["best_fit"] is True) == 1


def test_recommendation_contract_for_income_strategies() -> None:
    results = find_strategies_for_market_view(strategy_type="income")

    assert results
    names = {item["name"] for item in results}
    assert {"Covered Call", "Iron Condor"}.issubset(names)

    for item in results:
        assert item["strategy_type"] in {"income", "hedged", "volatility", "spread", "directional", "short-volatility"}
        assert "best_fit" in item
