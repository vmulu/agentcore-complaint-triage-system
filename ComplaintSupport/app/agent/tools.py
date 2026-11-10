from langchain.tools import tool
import json, pathlib

_POLICIES = json.loads((pathlib.Path(__file__).parent / "policies.json").read_text())

# faking before adding kb
@tool
def lookup_policy(topic: str) -> str:
    """Look up company policy. topic: one of refund, outage, billing, damage, escalation."""
    return _POLICIES.get(topic, "No policy found. Do not make commitments on this topic.")

@tool
def get_reply_format(channel: str) -> str:
    """Get formatting rules for a reply. channel: email, web_form, or mail."""
    return {
        "email": "Greeting, 2-3 short paragraphs, sign-off from 'Customer Support Team'.",
        "web_form": "Brief and plain, under 120 words, no letter formatting.",
        "mail": "Formal letter format with date line and full sign-off.",
    }.get(channel, "Use email format.")