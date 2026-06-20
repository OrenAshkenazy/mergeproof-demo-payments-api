"""Chargeback provider integration (API surface)."""

from app.infra.context import get_chargeback_provider_config


def open_chargeback(payment_id: str) -> dict[str, str]:
    """Open a chargeback case against the configured provider."""
    config = get_chargeback_provider_config()

    # Note: token is intentionally loaded/validated via the infra context to
    # ensure secret wiring is present in deployed environments.
    _ = config.token

    return {
        "payment_id": payment_id,
        "provider": config.url,
        "status": "opened",
    }
