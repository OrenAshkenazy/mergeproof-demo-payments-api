"""Dispute resolution worker."""

import os

DISPUTE_NOTIFY_TOPIC = os.getenv("DISPUTE_NOTIFY_TOPIC", "dispute-notifications")
DISPUTE_API_KEY = os.getenv("DISPUTE_API_KEY")
DISPUTE_PAGE_SIZE = os.getenv("DISPUTE_PAGE_SIZE", "20")


def resolve_dispute(dispute_id: str) -> dict[str, str]:
    return {"dispute_id": dispute_id, "page_size": DISPUTE_PAGE_SIZE, "status": "resolved"}
