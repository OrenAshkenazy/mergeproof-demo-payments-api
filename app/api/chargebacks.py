import os

from app.workers.chargeback_worker import enqueue_chargeback


def create_chargeback(payment_id: str, reason: str) -> dict[str, str]:
    provider_url = os.environ["CHARGEBACK_PROVIDER_URL"]
    job = enqueue_chargeback(payment_id=payment_id, reason=reason)

    return {
        "payment_id": payment_id,
        "provider_url": provider_url,
        "queue": job["queue"],
        "status": "queued",
    }
