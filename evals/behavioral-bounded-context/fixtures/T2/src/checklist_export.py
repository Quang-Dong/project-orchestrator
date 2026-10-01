"""Export unresolved items from a task list."""


def export_checklist(items):
    """Return task labels that still need attention."""
    return [item["label"] for item in items if item["status"] != "done"]
