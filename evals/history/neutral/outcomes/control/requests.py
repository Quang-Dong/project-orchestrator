"""Pure list helpers for a small volunteer repair desk."""

def attention_today(requests, today):
    """Return due open or in-progress requests in their input order."""
    return [
        item
        for item in requests
        if item["status"] in {"open", "in_progress"}
        and item["due_date"] is not None
        and item["due_date"] <= today
    ]
