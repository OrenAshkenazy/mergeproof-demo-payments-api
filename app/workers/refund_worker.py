"""Refund worker — consumes the chargeback intake queue."""

from __future__ import annotations

import logging
import os
import time

from app.infra.context import get_worker_queue_name

logger = logging.getLogger(__name__)


def process_batch(queue_name: str | None = None) -> str:
    """Drain one batch of chargeback events from the intake queue."""
    queue_name = queue_name or get_worker_queue_name()
    return f"processed batch from {queue_name}"


def main() -> None:
    """Entrypoint for `python -m app.workers.refund_worker`.

    Runs a simple poll loop so the worker process does not exit immediately.
    """

    logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"))

    queue_name = get_worker_queue_name()
    poll_interval_seconds = float(os.getenv("WORKER_POLL_INTERVAL_SECONDS", "5"))

    logger.info("Starting refund worker; queue=%s", queue_name)

    while True:
        try:
            result = process_batch(queue_name=queue_name)
            logger.info(result)
        except Exception:
            # Keep the worker alive; rely on logs/monitoring for alerting.
            logger.exception("Unhandled exception while processing batch")

        time.sleep(poll_interval_seconds)


if __name__ == "__main__":
    main()
