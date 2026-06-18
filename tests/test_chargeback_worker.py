from app.workers.chargeback_worker import enqueue_chargeback


def test_enqueue_chargeback_uses_configured_queue(monkeypatch):
    monkeypatch.setenv("CHARGEBACK_QUEUE_NAME", "chargebacks-prod")

    job = enqueue_chargeback("pay_123", "duplicate")

    assert job == {
        "payment_id": "pay_123",
        "reason": "duplicate",
        "queue": "chargebacks-prod",
        "worker": "chargeback_worker",
    }
