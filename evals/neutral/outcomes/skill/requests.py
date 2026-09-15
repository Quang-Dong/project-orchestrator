"""Pure list helpers for a small volunteer repair desk."""

def attention_today(requests, today):
    """Return actionable open or in-progress requests due by today."""
    return [
        item
        for item in requests
        if item["status"] in {"open", "in_progress"}
        and item["due_date"] is not None
        and item["due_date"] <= today
    ]
