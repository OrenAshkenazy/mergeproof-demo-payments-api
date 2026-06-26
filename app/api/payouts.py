"""Payouts read API."""
import os

PAYOUTS_PAGE_SIZE = int(os.getenv("PAYOUTS_PAGE_SIZE", "25"))


def list_payouts(page: int) -> dict:
    return {"page": page, "page_size": PAYOUTS_PAGE_SIZE}
