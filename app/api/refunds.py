import os

from app.workers.refund_worker import process_refund


def create_refund(payment_id: str) -> dict[str, str]:
    provider_url = os.environ["PAYMENT_PROVIDER_URL"]
    refund = process_refund(payment_id)
    return {
        "payment_id": refund["payment_id"],
        "provider_url": provider_url,
        "status": "refund_requested",
    }
