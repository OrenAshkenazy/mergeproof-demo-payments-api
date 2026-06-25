"""Payouts API surface — exposes payout status to the dashboard."""

import os

PAYOUTS_PAGE_SIZE = os.getenv("PAYOUTS_PAGE_SIZE", "25")


def list_payouts() -> str:
    """Return a page of payout records for the dashboard."""
    return f"listing up to {PAYOUTS_PAGE_SIZE} payouts"
