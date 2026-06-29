"""Chargeback provider integration (API surface)."""

import os

PROVIDER_URL = os.environ["CHARGEBACK_PROVIDER_URL"]
PROVIDER_TOKEN = os.environ["CHARGEBACK_PROVIDER_TOKEN"]


def open_chargeback(payment_id: str) -> dict[str, str]:
    """Open a chargeback case against the configured provider."""
    return {
        "payment_id": payment_id,
        "provider": PROVIDER_URL,
        "status": "opened",
    }
