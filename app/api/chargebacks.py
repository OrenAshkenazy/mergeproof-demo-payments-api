"""Chargeback capture API.

Reads the chargeback provider endpoint from the environment. This URL has no
wiring precedent in the platform-infra repo, so MergeProof must gate it for a
human production decision rather than guess secret-vs-config.
"""
from __future__ import annotations

import os

CHARGEBACK_PROVIDER_URL = os.environ["CHARGEBACK_PROVIDER_URL"]


def open_chargeback(payment_id: str) -> dict[str, str]:
    return {"payment_id": payment_id, "provider": CHARGEBACK_PROVIDER_URL}
