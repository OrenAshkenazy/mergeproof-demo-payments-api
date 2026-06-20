"""Chargeback settlement worker.

Reads the chargeback queue name from the environment. No infra precedent shares
the _NAME suffix wiring, so this is human-gated, not auto-classified.
"""
from __future__ import annotations

import os

def _get_chargeback_queue_name() -> str:
    """Return the configured chargeback queue name.

    Do not default required worker configuration to ""; fail fast with a clear
    error so misconfigured deployments don't silently run.
    """

    value = os.getenv("CHARGEBACK_QUEUE_NAME")
    if not value:
        raise RuntimeError(
            "Missing required environment variable CHARGEBACK_QUEUE_NAME"
        )
    return value


def run() -> str:
    return _get_chargeback_queue_name()
