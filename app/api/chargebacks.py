"""Chargeback capture API.

Reads the chargeback provider endpoint from the environment. This URL has no
wiring precedent in the platform-infra repo, so MergeProof must gate it for a
human production decision rather than guess secret-vs-config.
"""
from __future__ import annotations

import os

def _get_chargeback_provider_url() -> str:
    """Return the configured chargeback provider URL.

    Do not read required env vars at import time; that turns a deployment
    misconfiguration into an opaque KeyError during startup/import.
    """

    value = os.getenv("CHARGEBACK_PROVIDER_URL")
    if not value:
        raise RuntimeError(
            "Missing required environment variable CHARGEBACK_PROVIDER_URL"
        )
    return value


def open_chargeback(payment_id: str) -> dict[str, str]:
    return {"payment_id": payment_id, "provider": _get_chargeback_provider_url()}
