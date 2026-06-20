"""Refund worker — consumes the chargeback intake queue."""

import os

QUEUE_NAME = os.getenv("CHARGEBACK_QUEUE_NAME", "")


def process_batch() -> str:
    """Drain one batch of chargeback events from the intake queue."""
    return f"processed batch from {QUEUE_NAME}"
