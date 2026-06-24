"""Notification worker — delivers refund notifications to the provider."""

import os

# New secret-shaped credential: suffix-peer REFUND_PROVIDER_TOKEN is wired as an
# ExternalSecret in the infra repo, so this should classify as secret_wiring.
NOTIFICATION_PROVIDER_TOKEN = os.getenv("NOTIFICATION_PROVIDER_TOKEN")


def notify(message: str) -> str:
    """Deliver one refund notification using the configured provider token."""
    if not NOTIFICATION_PROVIDER_TOKEN:
        raise RuntimeError("NOTIFICATION_PROVIDER_TOKEN must be set")
    return f"notified: {message}"
