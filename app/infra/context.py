"""Centralized infra-context configuration loaders.

This module exists to ensure environment/secret dependencies are loaded in one
place with validation, rather than being scattered across business logic.
"""

from __future__ import annotations

from dataclasses import dataclass
import os


def _required_env(name: str) -> str:
    value = os.getenv(name)
    if value is None or value.strip() == "":
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


@dataclass(frozen=True)
class ChargebackProviderConfig:
    url: str
    token: str


def get_chargeback_provider_config() -> ChargebackProviderConfig:
    return ChargebackProviderConfig(
        url=_required_env("CHARGEBACK_PROVIDER_URL"),
        token=_required_env("CHARGEBACK_PROVIDER_TOKEN"),
    )


def get_worker_queue_name() -> str:
    # Backwards-compatible: platform-infra currently sets WORKER_QUEUE.
    queue_name = os.getenv("CHARGEBACK_QUEUE_NAME") or os.getenv("WORKER_QUEUE")
    if queue_name is None or queue_name.strip() == "":
        raise RuntimeError(
            "Missing required worker queue name. Set CHARGEBACK_QUEUE_NAME (preferred) "
            "or WORKER_QUEUE (legacy)."
        )
    return queue_name
