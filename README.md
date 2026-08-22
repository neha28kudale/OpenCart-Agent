# OpenCart Agent — Making Merchants Transactable by AI Buyers

**Track:** AI Growth & Agentic Commerce — Razorpay AI Builder Internship 2026

## The brief

Grow merchant revenue, and make merchants transactable by AI buyers end-to-end
(ACP, AP2, x402-style agent-to-agent commerce). The bar: every money action must be
explainable, bounded and gated, with an audit trail and one gracefully handled failure.

## What this does

1. **Agent-readable catalog** (`catalog/agent_catalog.py`) — merchant's products exposed
   in a structured format any AI shopping agent (ChatGPT, Perplexity buyer-agents, etc.)
   can query directly, no HTML scraping.
2. **Checkout agent** (`agent/checkout_agent.py`) — receives a structured purchase intent
   from an external buyer-agent, matches it to catalog items, and drives the transaction
   through to a simulated Razorpay test-mode charge.
3. **Spend guardrails** (`agent/spend_guard.py`) — every transaction is bounded (hard price
   ceiling, category allowlist, daily spend cap) and gated (confirmation required above a
   threshold) *before* any charge happens. These are merchant-controlled and cannot be
   overridden by the agent.
4. **Audit trail** (`agent/audit_log.py`) — every decision, approved, declined, or pending
   confirmation, is logged with full context and a plain-English reason. Nothing happens silently.
5. **Graceful failure** — when the best-matching item is out of stock, the agent declines
   cleanly with a clear reason instead of silently substituting or guessing.

## Run it

```bash
python3 main.py              # runs 5 simulated AI-buyer purchase requests
open dashboard/index.html    # view the transaction gate log
```

## Simulated scenarios (see main.py)

| # | Scenario | Expected outcome |
|---|----------|------------------|
| 1 | Cheap, in-stock, clean match | COMPLETED |
| 2 | Price above confirmation threshold, unconfirmed | NEEDS_CONFIRMATION |
| 3 | Same request, now confirmed | COMPLETED |
| 4 | Price above hard cap, even with confirmation | DECLINED |
| 5 | Best match is out of stock | DECLINED (graceful) |

## Tech stack

Python (catalog matching, guardrails, audit logging), HTML/CSS/JS dashboard.
Designed to plug into Razorpay test-mode APIs and real agent-commerce protocols
(ACP, AP2, x402) in production.

## Build challenges (fill in as you extend this)

- [ ] Note real obstacles as you build further — e.g. handling partial attribute
      matches, tuning confirmation thresholds, or integrating a live Razorpay test key.
