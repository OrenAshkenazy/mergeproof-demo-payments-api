"""Settlement worker — reconciles daily settlement batches with the ledger."""

import os

# New worker-scoped env read. SETTLEMENT_LEDGER_TOKEN shares the _TOKEN suffix
# with REFUND_PROVIDER_TOKEN (wired as an ExternalSecret in the infra repo), so
# MergeProof should classify it as secret_wiring and flag a human gate, while the
# worker file itself drives a worker_deployment obligation.
SETTLEMENT_LEDGER_TOKEN = os.getenv("SETTLEMENT_LEDGER_TOKEN")
if not SETTLEMENT_LEDGER_TOKEN:
    raise RuntimeError("SETTLEMENT_LEDGER_TOKEN must be set")

try:
    SETTLEMENT_BATCH_SIZE = int(os.getenv("SETTLEMENT_BATCH_SIZE", "100"))
    if SETTLEMENT_BATCH_SIZE <= 0:
        raise ValueError("SETTLEMENT_BATCH_SIZE must be a positive integer")
except ValueError as e:
    raise ValueError(f"Invalid SETTLEMENT_BATCH_SIZE: {e}") from e


def reconcile() -> str:
    """Reconcile one settlement batch against the ledger."""
    return f"reconciled batch of {SETTLEMENT_BATCH_SIZE}"
