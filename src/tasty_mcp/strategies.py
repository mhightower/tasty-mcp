"""Strategy catalog derived from the Tastylive options strategy index."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

REFERENCE_URL = "https://www.tastylive.com/concepts-strategies/"


@dataclass(frozen=True)
class Strategy:
    name: str
    slug: str
    market_assumption: str
    risk_profile: str
    summary: str
    source: str
    volatility_bias: str
    strategy_type: str

    def as_dict(self) -> dict[str, str]:
        return {
            "name": self.name,
            "slug": self.slug,
            "market_assumption": self.market_assumption,
            "risk_profile": self.risk_profile,
            "summary": self.summary,
            "source": self.source,
            "volatility_bias": self.volatility_bias,
            "strategy_type": self.strategy_type,
        }


STRATEGIES: list[Strategy] = [
    Strategy(
        name="Long Call & Put Options",
        slug="long-call-put-options",
        market_assumption="bullish for long calls; bearish for long puts",
        risk_profile="defined risk to premium paid; directional exposure",
        summary="Long options let traders speculate on directional moves with limited premium risk and an option contract representing 100 shares.",
        source=REFERENCE_URL,
        volatility_bias="directional",
        strategy_type="directional",
    ),
    Strategy(
        name="Short Call & Put Options",
        slug="short-call-put-options",
        market_assumption="neutral to directional depending on strike and bias; generally against strong move toward strike",
        risk_profile="limited profit; undefined or large risk",
        summary="Short options receive upfront premium and profit when the underlying stays away from the strike, but can carry assignment risk.",
        source=REFERENCE_URL,
        volatility_bias="high",
        strategy_type="short-volatility",
    ),
    Strategy(
        name="Covered Call",
        slug="covered-call",
        market_assumption="neutral to mildly bullish while holding stock",
        risk_profile="defined downside with capped upside",
        summary="Own 100 shares and sell a call against them to generate income while capping upside above the strike.",
        source=REFERENCE_URL,
        volatility_bias="low",
        strategy_type="income",
    ),
    Strategy(
        name="Married Put",
        slug="married-put",
        market_assumption="bullish long-term stock ownership with hedged downside",
        risk_profile="defined downside, premium paid for insurance",
        summary="Buy stock and buy a protective put to define the downside while retaining upside exposure.",
        source=REFERENCE_URL,
        volatility_bias="low",
        strategy_type="hedged",
    ),
    Strategy(
        name="Straddle",
        slug="straddle",
        market_assumption="neutral, expecting a large move in either direction",
        risk_profile="long has defined risk; short has limited profit and large risk",
        summary="Simultaneously buy or sell an at-the-money call and put with the same strike and expiration to express volatility.",
        source=REFERENCE_URL,
        volatility_bias="high",
        strategy_type="volatility",
    ),
    Strategy(
        name="Strangle",
        slug="strangle",
        market_assumption="neutral, expecting a move outside a defined range",
        risk_profile="long has defined risk; short has limited premium and undefined risk",
        summary="Use an out-of-the-money call and put with the same expiration to trade volatility with a wider break-even range than a straddle.",
        source=REFERENCE_URL,
        volatility_bias="high",
        strategy_type="volatility",
    ),
    Strategy(
        name="Iron Condor",
        slug="iron-condor",
        market_assumption="neutral, expecting the underlying to stay inside a range",
        risk_profile="defined risk and reward; limited premium",
        summary="Combine a short call spread and short put spread to collect premium when the stock stays between the strikes.",
        source=REFERENCE_URL,
        volatility_bias="low",
        strategy_type="income",
    ),
    Strategy(
        name="Broken Wing Butterfly",
        slug="broken-wing-butterfly",
        market_assumption="neutral to slightly directional, often with a credit structure",
        risk_profile="defined risk and reward; can be credit funded",
        summary="A butterfly variant with asymmetrical wings designed to reduce exposure on one side while maintaining a defined-risk structure.",
        source=REFERENCE_URL,
        volatility_bias="medium",
        strategy_type="spread",
    ),
    Strategy(
        name="Protective Collar",
        slug="protective-collar",
        market_assumption="bullish on long-term stock with desire to protect gains",
        risk_profile="defined downside with capped upside",
        summary="Own stock, buy a protective put, and sell an out-of-the-money call to offset the premium and cap the upside.",
        source=REFERENCE_URL,
        volatility_bias="low",
        strategy_type="hedged",
    ),
    Strategy(
        name="Diagonal Spread",
        slug="diagonal-spread",
        market_assumption="directional with a time-decay and volatility component",
        risk_profile="limited debit risk; directional and timing dependent",
        summary="Pair long and short options across different expirations to reduce cost basis while maintaining directional exposure.",
        source=REFERENCE_URL,
        volatility_bias="medium",
        strategy_type="spread",
    ),
    Strategy(
        name="Jade Lizard",
        slug="jade-lizard",
        market_assumption="neutral to mildly bullish income strategy",
        risk_profile="defined risk on the short call spread with short-put exposure tied to stock ownership",
        summary="A jade lizard combines a short put and a short call spread to generate premium while maintaining a bullish-to-neutral income bias.",
        source=REFERENCE_URL,
        volatility_bias="low",
        strategy_type="income",
    ),
    Strategy(
        name="Iron Butterfly",
        slug="iron-butterfly",
        market_assumption="neutral, expecting a range-bound outcome",
        risk_profile="defined risk with capped premium potential",
        summary="An iron butterfly combines short call and put spreads around the center strike to collect premium in a narrow range.",
        source=REFERENCE_URL,
        volatility_bias="low",
        strategy_type="income",
    ),
    Strategy(
        name="Calendar Spread",
        slug="calendar-spread",
        market_assumption="directional or neutral with strong time-decay expectations",
        risk_profile="limited debit risk, exposure to timing and volatility changes",
        summary="A calendar spread trades different expirations against each other to exploit time decay and volatility differences.",
        source=REFERENCE_URL,
        volatility_bias="medium",
        strategy_type="spread",
    ),
    Strategy(
        name="Zebra",
        slug="zebra",
        market_assumption="neutral to slightly directional, with a wider price expectation band",
        risk_profile="defined risk with a more asymmetric payout profile",
        summary="A zebra is a skewed butterfly-style structure designed to express a range with a different payoff profile than a traditional butterfly.",
        source=REFERENCE_URL,
        volatility_bias="medium",
        strategy_type="spread",
    ),
]


def _normalize(value: str) -> str:
    return " ".join(value.strip().lower().split())


def get_strategy_catalog() -> list[dict[str, Any]]:
    """Return the strategy catalog from the Tastylive strategy index."""
    return [strategy.as_dict() for strategy in STRATEGIES]


def get_strategy_by_name(name: str) -> dict[str, Any] | None:
    """Look up a strategy by name or slug, ignoring case and extra whitespace."""
    normalized = _normalize(name)
    for strategy in STRATEGIES:
        if normalized in {strategy.name.lower(), strategy.slug.lower()}:
            return strategy.as_dict()
    return None


def find_matching_strategies(
    direction: str | None = None,
    risk_tolerance: str | None = None,
    volatility: str | None = None,
    strategy_type: str | None = None,
) -> list[dict[str, Any]]:
    """Recommend strategies with a practical filter set based on direction, risk, volatility, and setup style."""
    normalized_direction = _normalize(direction or "")
    normalized_risk = _normalize(risk_tolerance or "")
    normalized_volatility = _normalize(volatility or "")
    normalized_type = _normalize(strategy_type or "")

    matches: list[dict[str, Any]] = []
    for strategy in STRATEGIES:
        market = strategy.market_assumption.lower()
        risk = strategy.risk_profile.lower()
        volatility_bias = strategy.volatility_bias.lower()
        strategy_style = strategy.strategy_type.lower()

        direction_match = True
        if normalized_direction:
            if normalized_direction == "bullish":
                direction_match = "bullish" in market
            elif normalized_direction == "bearish":
                direction_match = "bearish" in market
            elif normalized_direction == "neutral":
                direction_match = "neutral" in market or "range" in market
            elif normalized_direction == "directional":
                direction_match = "directional" in market or "bullish" in market or "bearish" in market

        risk_match = True
        if normalized_risk:
            if normalized_risk in {"defined", "limited", "premium"}:
                risk_match = normalized_risk in risk or (normalized_risk == "defined" and "defined" in risk)
            elif normalized_risk in {"undefined", "large"}:
                risk_match = normalized_risk in risk or "undefined" in risk or "large" in risk

        volatility_match = True
        if normalized_volatility:
            if normalized_volatility in {"low", "medium", "high"}:
                volatility_match = volatility_bias == normalized_volatility
            elif normalized_volatility == "volatility":
                volatility_match = "volatility" in strategy_style or volatility_bias in {"high", "medium"}

        type_match = True
        if normalized_type:
            type_match = normalized_type in strategy_style or normalized_type in strategy.name.lower()

        if direction_match and risk_match and volatility_match and type_match:
            matches.append(strategy.as_dict())

    return matches
