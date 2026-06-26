"""Fan out dispute notifications to the dispute-notifications topic."""
import os

DISPUTE_NOTIFY_TOPIC = os.getenv("DISPUTE_NOTIFY_TOPIC", "dispute-notifications")
SETTLEMENT_REGION = os.getenv("SETTLEMENT_REGION")
if not SETTLEMENT_REGION:
    raise RuntimeError("SETTLEMENT_REGION must be set")


def run() -> None:
    print(f"notifying disputes in {SETTLEMENT_REGION} via {DISPUTE_NOTIFY_TOPIC}")
