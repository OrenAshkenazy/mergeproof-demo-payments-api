"""Dispute worker — publishes chargeback disputes to the notifications topic."""

import os

# Topic-ish + literal default -> runtime_config AND queue_topic.
DISPUTE_NOTIFY_TOPIC = os.getenv("DISPUTE_NOTIFY_TOPIC", "dispute-notifications")


def publish(dispute_id: str) -> str:
    """Publish one dispute event to the notifications topic."""
    return f"published {dispute_id} to {DISPUTE_NOTIFY_TOPIC}"
