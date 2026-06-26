"""Payout worker — disburses settled balances to payment providers."""

import os

# Secret-shaped credential (peer of REFUND_PROVIDER_TOKEN) -> secret_wiring, human gate.
PAYOUT_PROVIDER_TOKEN = os.getenv("PAYOUT_PROVIDER_TOKEN")
# Literal default -> runtime_config.
PAYOUT_BATCH_SIZE = os.getenv("PAYOUT_BATCH_SIZE", "50")
# Queue-ish + literal default -> runtime_config AND queue_topic.
PAYOUT_EVENTS_QUEUE = os.getenv("PAYOUT_EVENTS_QUEUE", "payout-events")


def disburse() -> str:
    """Disburse one batch of settled payouts to the provider."""
    if not PAYOUT_PROVIDER_TOKEN:
        raise RuntimeError("PAYOUT_PROVIDER_TOKEN must be set")
    return f"disbursed {PAYOUT_BATCH_SIZE} via {PAYOUT_EVENTS_QUEUE}"
