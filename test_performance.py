"""Performance and stress testing for the MCP server."""

import time
from tasty_mcp.server import (
    find_strategies_for_market_view,
    get_options_strategy,
    list_options_strategies,
)


def benchmark_list_strategies(iterations: int = 100) -> None:
    """Benchmark list_options_strategies() performance."""
    print(f"\n⏱️  Benchmarking list_options_strategies() ({iterations} iterations)")
    print("=" * 60)

    start = time.perf_counter()
    for _ in range(iterations):
        list_options_strategies()
    elapsed = time.perf_counter() - start

    avg_ms = (elapsed / iterations) * 1000
    print(f"Total time: {elapsed:.3f}s")
    print(f"Avg per call: {avg_ms:.2f}ms")
    print(f"Calls/sec: {iterations / elapsed:.0f}")


def benchmark_get_strategy(iterations: int = 100) -> None:
    """Benchmark get_options_strategy() performance."""
    print(f"\n⏱️  Benchmarking get_options_strategy() ({iterations} iterations)")
    print("=" * 60)

    strategies = ["Long Call & Put Options", "Covered Call", "Straddle", "Strangle"]
    start = time.perf_counter()
    for i in range(iterations):
        get_options_strategy(strategies[i % len(strategies)])
    elapsed = time.perf_counter() - start

    avg_ms = (elapsed / iterations) * 1000
    print(f"Total time: {elapsed:.3f}s")
    print(f"Avg per call: {avg_ms:.2f}ms")
    print(f"Calls/sec: {iterations / elapsed:.0f}")


def benchmark_find_strategies(iterations: int = 100) -> None:
    """Benchmark find_strategies_for_market_view() performance."""
    print(
        f"\n⏱️  Benchmarking find_strategies_for_market_view() ({iterations} iterations)"
    )
    print("=" * 60)

    filters = [
        {"direction": "bullish"},
        {"direction": "bearish"},
        {"risk_tolerance": "defined"},
        {"volatility": "high"},
        {"strategy_type": "income"},
        {"direction": "bullish", "volatility": "low"},
    ]

    start = time.perf_counter()
    for i in range(iterations):
        filter_set = filters[i % len(filters)]
        find_strategies_for_market_view(**filter_set)
    elapsed = time.perf_counter() - start

    avg_ms = (elapsed / iterations) * 1000
    print(f"Total time: {elapsed:.3f}s")
    print(f"Avg per call: {avg_ms:.2f}ms")
    print(f"Calls/sec: {iterations / elapsed:.0f}")


def stress_test_concurrent_patterns() -> None:
    """Stress test with realistic concurrent usage patterns."""
    print("\n🔥 Stress Test: Simulating concurrent usage patterns")
    print("=" * 60)

    # Simulate a typical usage pattern
    patterns = [
        ("list strategies", lambda: list_options_strategies()),
        ("get strategy", lambda: get_options_strategy("covered call")),
        ("find bullish", lambda: find_strategies_for_market_view(direction="bullish")),
        (
            "find income",
            lambda: find_strategies_for_market_view(strategy_type="income"),
        ),
        (
            "find defined risk",
            lambda: find_strategies_for_market_view(risk_tolerance="defined"),
        ),
    ]

    total_iterations = 200
    start = time.perf_counter()

    for i in range(total_iterations):
        name, func = patterns[i % len(patterns)]
        func()

    elapsed = time.perf_counter() - start
    avg_ms = (elapsed / total_iterations) * 1000

    print(f"Completed {total_iterations} diverse operations")
    print(f"Total time: {elapsed:.3f}s")
    print(f"Avg per call: {avg_ms:.2f}ms")
    print(f"Throughput: {total_iterations / elapsed:.0f} ops/sec")


def run_all_benchmarks() -> None:
    """Run all performance tests."""
    print("\n" + "=" * 60)
    print("⚡ TASTY MCP SERVER - PERFORMANCE BENCHMARKS")
    print("=" * 60)

    benchmark_list_strategies(100)
    benchmark_get_strategy(100)
    benchmark_find_strategies(100)
    stress_test_concurrent_patterns()

    print("\n" + "=" * 60)
    print("✅ PERFORMANCE TESTS COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    run_all_benchmarks()
