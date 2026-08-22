"""
OpenCart Agent - main simulation.
Simulates several external AI buyer-agents sending purchase intents to the
merchant's checkout agent. Includes: a clean approval, a confirmation-required
case, and the required graceful-failure case (out of stock).

Run: python3 main.py
"""

import json
import os
from agent.checkout_agent import handle_purchase_intent
from agent.audit_log import get_all_events

SIMULATED_BUYER_REQUESTS = [
    {
        "buyer_agent_id": "chatgpt-shopper-8841",
        "intent": {
            "attributes": {"category": "apparel", "color": "white", "size": "M"},
            "max_price": 800,
            "buyer_confirmed": False,
        },
        "note": "Should COMPLETE - cheap, in-stock, clean match",
    },
    {
        "buyer_agent_id": "perplexity-buyer-3390",
        "intent": {
            "attributes": {"category": "apparel", "color": "black", "size": "M"},
            "max_price": 1500,
            "buyer_confirmed": False,
        },
        "note": "Should NEED CONFIRMATION - ₹1299 is above the ₹1000 auto-approve threshold",
    },
    {
        "buyer_agent_id": "perplexity-buyer-3390",
        "intent": {
            "attributes": {"category": "apparel", "color": "black", "size": "M"},
            "max_price": 1500,
            "buyer_confirmed": True,
        },
        "note": "Same request, now CONFIRMED - should COMPLETE",
    },
    {
        "buyer_agent_id": "rogue-agent-0001",
        "intent": {
            "attributes": {"category": "apparel", "color": "blue", "size": "L", "material": "denim"},
            "max_price": 999999,
            "buyer_confirmed": True,
        },
        "note": "Hard cap demo - denim jacket (₹2999) exceeds the ₹2500 max transaction limit, blocked even with confirmation",
    },
    {
        "buyer_agent_id": "chatgpt-shopper-8841",
        "intent": {
            "attributes": {"category": "apparel", "color": "black", "size": "L"},
            "max_price": 1500,
            "buyer_confirmed": False,
        },
        "note": "Graceful failure demo - matches hoodie but OUT OF STOCK, must decline cleanly",
    },
]


def run_simulation():
    print("=" * 70)
    print("OPENCART AGENT — Simulated AI Buyer-Agent Purchase Flow")
    print("=" * 70)

    for i, req in enumerate(SIMULATED_BUYER_REQUESTS, 1):
        print(f"\n[{i}] Buyer: {req['buyer_agent_id']}")
        print(f"    Intent: {req['intent']}")
        print(f"    Expected: {req['note']}")
        result = handle_purchase_intent(req["buyer_agent_id"], req["intent"])
        print(f"    -> STATUS: {result['status']}")
        print(f"    -> REASON: {result['reason']}")

    events = get_all_events()
    print(f"\n{'=' * 70}")
    print(f"Audit trail written with {len(events)} events -> dashboard/audit_log.json")
    print("=" * 70)


if __name__ == "__main__":
    run_simulation()
