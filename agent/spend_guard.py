"""
Spend guardrails.
Per the brief's bar: "Every money action explainable, bounded and gated."

This module enforces hard limits BEFORE any transaction is allowed to proceed,
independent of what the checkout agent "wants" to do. The agent cannot override these.
"""

# Hard-coded merchant-configured guardrails (would be a merchant dashboard setting in production)
GUARDRAILS = {
    "max_single_transaction": 2500,       # INR - hard ceiling per purchase, no override
    "requires_confirmation_above": 1000,  # INR - needs an explicit confirmation step
    "allowed_categories": ["apparel", "accessories"],
    "blocked_skus": [],                   # merchant can blocklist specific SKUs from agent purchase
    "max_daily_agent_spend": 8000,        # INR - cumulative cap across all AI-buyer transactions today
}

# Running total tracked for the demo session (would be persisted in production)
_daily_spend_tracker = {"total": 0}


def evaluate_transaction(item: dict, buyer_confirmed: bool = False):
    """
    Returns a decision dict: {"allowed": bool, "requires_confirmation": bool, "reason": str}
    Every branch has an explicit, human-readable reason - nothing is a silent pass/fail.
    """
    price = item["price"]
    sku = item["sku"]
    category = item["category"]

    if category not in GUARDRAILS["allowed_categories"]:
        return _deny(f"Category '{category}' is not enabled for AI-buyer purchases.")

    if sku in GUARDRAILS["blocked_skus"]:
        return _deny(f"SKU {sku} is blocked from agent-initiated purchase by the merchant.")

    if price > GUARDRAILS["max_single_transaction"]:
        return _deny(
            f"Price ₹{price} exceeds the merchant's max single-transaction limit "
            f"of ₹{GUARDRAILS['max_single_transaction']} for AI-buyer purchases."
        )

    projected_total = _daily_spend_tracker["total"] + price
    if projected_total > GUARDRAILS["max_daily_agent_spend"]:
        return _deny(
            f"This purchase would push today's AI-buyer spend to ₹{projected_total}, "
            f"over the ₹{GUARDRAILS['max_daily_agent_spend']} daily cap."
        )

    if price > GUARDRAILS["requires_confirmation_above"] and not buyer_confirmed:
        return {
            "allowed": False,
            "requires_confirmation": True,
            "reason": (
                f"Price ₹{price} is above ₹{GUARDRAILS['requires_confirmation_above']}, "
                f"so explicit buyer-agent confirmation is required before charging."
            ),
        }

    # Passed all gates
    _daily_spend_tracker["total"] = projected_total
    return {
        "allowed": True,
        "requires_confirmation": False,
        "reason": "Within all merchant-configured spend, category, and daily cap guardrails.",
    }


def _deny(reason):
    return {"allowed": False, "requires_confirmation": False, "reason": reason}


def get_daily_spend():
    return _daily_spend_tracker["total"]
