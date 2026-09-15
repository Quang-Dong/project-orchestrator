"""Pure list helpers for a small volunteer repair desk."""

def attention_today(requests, today):
    """Return requests for the overview; today's business rule is pending."""
    return [item for item in requests if item["status"] == "open"]
