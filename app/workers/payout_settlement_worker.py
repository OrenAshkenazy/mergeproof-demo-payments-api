"""Settle payouts in batches off the payout-events queue."""
import os

PAYOUT_BATCH_SIZE = int(os.getenv("PAYOUT_BATCH_SIZE", "50"))
PAYOUT_EVENTS_QUEUE = os.getenv("PAYOUT_EVENTS_QUEUE", "payout-events")
PAYOUT_PROVIDER_TOKEN = os.getenv("PAYOUT_PROVIDER_TOKEN")


def run() -> None:
    print(f"settling up to {PAYOUT_BATCH_SIZE} from {PAYOUT_EVENTS_QUEUE}")
