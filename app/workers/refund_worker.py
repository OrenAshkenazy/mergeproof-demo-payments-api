import os


def process_refund(payment_id: str) -> dict[str, str]:
    queue_name = os.environ["REFUND_QUEUE_NAME"]
    return {
        "payment_id": payment_id,
        "queue": queue_name,
        "status": "refund_queued",
    }
