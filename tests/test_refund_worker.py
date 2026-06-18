from app.workers.refund_worker import process_refund


def test_process_refund_queues_payment(monkeypatch):
    monkeypatch.setenv("REFUND_QUEUE_NAME", "refunds")

    assert process_refund("pay_demo_456") == {
        "payment_id": "pay_demo_456",
        "queue": "refunds",
        "status": "refund_queued",
    }
