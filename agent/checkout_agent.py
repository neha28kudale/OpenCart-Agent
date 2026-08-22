"""
Checkout agent.
Receives a structured purchase intent from an external AI buyer-agent,
matches it against the merchant's agent-readable catalog, runs it through
spend guardrails, and either completes a (simulated) Razorpay charge,
asks for confirmation, or declines - always with a plain-English reason.
"""

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from catalog.agent_catalog import find_matches
from agent.spend_guard import evaluate_transaction
from agent.audit_log import log_event


def handle_purchase_intent(buyer_agent_id: str, intent: dict):
    """
    intent example:
    {
      "attributes": {"category": "apparel", "color": "black", "size": "M"},
      "max_price": 1500,
      "buyer_confirmed": False
    }
    """
    query_attrs = intent.get("attributes", {})
    max_price = intent.get("max_price")
    buyer_confirmed = intent.get("buyer_confirmed", False)

    matches = find_matches(query_attrs, max_price)

    if not matches:
        result = {
            "status": "DECLINED",
            "sku": None,
            "reason": (
                f"No catalog items matched the requested attributes {query_attrs} "
                f"within budget ₹{max_price}. Nothing purchased."
            ),
        }
        log_event(buyer_agent_id, intent, result)
        return result

    best_match = matches[0]

    if best_match["stock"] <= 0:
        result = {
            "status": "DECLINED",
            "sku": best_match["sku"],
            "reason": (
                f"Best match '{best_match['name']}' ({best_match['sku']}) is out of stock. "
                f"Declining rather than substituting without buyer confirmation."
            ),
        }
        log_event(buyer_agent_id, intent, result)
        return result

    decision = evaluate_transaction(best_match, buyer_confirmed)

    if decision["requires_confirmation"]:
        result = {
            "status": "NEEDS_CONFIRMATION",
            "sku": best_match["sku"],
            "price": best_match["price"],
            "reason": decision["reason"],
        }
        log_event(buyer_agent_id, intent, result)
        return result

    if not decision["allowed"]:
        result = {
            "status": "DECLINED",
            "sku": best_match["sku"],
            "reason": decision["reason"],
        }
        log_event(buyer_agent_id, intent, result)
        return result

    # All checks passed - simulate a Razorpay test-mode charge
    result = {
        "status": "COMPLETED",
        "sku": best_match["sku"],
        "item_name": best_match["name"],
        "price": best_match["price"],
        "reason": f"Matched '{best_match['name']}' at {int(best_match['match_ratio']*100)}% attribute fit, within all guardrails. Charged via Razorpay (test mode).",
        "razorpay_order_id": f"order_test_{best_match['sku']}_{buyer_agent_id[-4:]}",
    }
    log_event(buyer_agent_id, intent, result)
    return result
