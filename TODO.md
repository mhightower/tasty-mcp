# Tasty MCP TODO

This is the recommended backlog for the project, in priority order based on value and fit with the current MCP server.

## Highest priority

1. Add a strategy comparison tool
   - Compare two or more strategies side by side
   - Show risk profile, volatility bias, market assumption, and summary
   - Extend the current recommendation workflow without changing the educational scope

2. Add keyword-based strategy search
   - Support search by terms such as income, hedged, neutral, butterfly, credit, or spread
   - Improve discovery and usability for clients

3. Add a smarter “best strategy for my scenario” tool
   - Accept a user scenario and return the top-ranked strategy with a short rationale
   - Build on the existing market-view recommendation logic

4. Add richer strategy detail payloads
   - Include when to use, when not to use, typical setup, max risk, and max reward concepts
   - Make the MCP output more educational and useful to AI clients

## Near-term enhancements

5. Add a JSON/CSV export resource
   - Expose the full catalog in a machine-readable format
   - Useful for integrations and client-side inspection

6. Add more filter dimensions
   - Allow filtering by payoff style, credit vs debit, long vs short, and range vs directional
   - Broaden the recommendation engine while staying safe and educational

7. Add related-strategy discovery
   - Recommend similar strategies based on shared traits or market assumptions
   - Improve exploration inside the catalog

8. Add explanatory glossary support
   - Define terms such as defined risk, undefined risk, premium, and volatility
   - Helps AI clients explain option concepts clearly

## Quality and usability

9. Improve alias handling for user inputs
   - Normalize inputs like bullish, bear, neutral, high vol, low vol, and credit spread
   - Make client usage more forgiving and consistent

10. Improve documentation and examples
   - Add tool schema examples and sample prompts for MCP clients
   - Keep the project easier to adopt and extend

## Later ideas

11. Add a spread-matrix or comparison report
   - Summarize multiple strategies at once for a market view
   - Useful for dashboards or assistant-generated recommendations

12. Add persistence or caching
   - Cache catalog lookups or computed recommendations for repeated use
   - Helpful if the server is used heavily in a shared environment

13. Add optional advanced analysis features
   - Exclude invalid combinations, add confidence scoring, or add educational warnings
   - Keep these optional and clearly labeled as educational guidance

---

## Current status

- Core MCP tool server is working
- Strategy catalog and recommendation filters are implemented
- High-value next steps are centered on comparison, discovery, and richer educational output
