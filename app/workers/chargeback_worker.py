"""Chargeback settlement worker.

Reads the chargeback queue name from the environment. No infra precedent shares
the _NAME suffix wiring, so this is human-gated, not auto-classified.
"""
from __future__ import annotations

import os

CHARGEBACK_QUEUE_NAME = os.getenv("CHARGEBACK_QUEUE_NAME", "")


def run() -> str:
    return CHARGEBACK_QUEUE_NAME
