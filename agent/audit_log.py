"""
Audit trail.
Per the brief: every money action must be explainable and show an audit trail.
Every decision the checkout agent makes - approved, declined, or needing
confirmation - is logged here with full context, nothing happens silently.
"""

import json
import os
from datetime import datetime

_LOG_PATH = os.path.join(os.path.dirname(__file__), "..", "dashboard", "audit_log.json")
_events = []


def log_event(buyer_agent_id: str, intent: dict, result: dict):
    event = {
        "timestamp": datetime.now().isoformat(),
        "buyer_agent_id": buyer_agent_id,
        "intent": intent,
        "result": result,
    }
    _events.append(event)
    _flush()


def _flush():
    with open(os.path.abspath(_LOG_PATH), "w") as f:
        json.dump(_events, f, indent=2)


def get_all_events():
    return _events
