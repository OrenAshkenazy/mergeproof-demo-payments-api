import os


def enqueue_chargeback(payment_id: str, reason: str) -> dict[str, str]:
    queue_name = os.environ["CHARGEBACK_QUEUE_NAME"]

    return {
        "payment_id": payment_id,
        "reason": reason,
        "queue": queue_name,
        "worker": "chargeback_worker",
    }
