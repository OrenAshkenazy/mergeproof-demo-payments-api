"""Refund processing worker."""

import os

REFUND_BATCH_SIZE = os.getenv("REFUND_BATCH_SIZE", "25")
REFUND_EVENTS_QUEUE = os.getenv("REFUND_EVENTS_QUEUE", "refund-events")
REFUND_PROVIDER_TOKEN = os.getenv("REFUND_PROVIDER_TOKEN")
SETTLEMENT_REGION = os.environ["SETTLEMENT_REGION"]


def process_refund(refund_id: str) -> dict[str, str]:
    return {"refund_id": refund_id, "region": SETTLEMENT_REGION, "status": "processed"}
