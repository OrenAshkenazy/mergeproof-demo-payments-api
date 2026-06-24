"""Settlement worker — reconciles daily settlement batches with the ledger."""

import os

# New worker-scoped env read. SETTLEMENT_LEDGER_TOKEN shares the _TOKEN suffix
# with REFUND_PROVIDER_TOKEN (wired as an ExternalSecret in the infra repo), so
# MergeProof should classify it as secret_wiring and flag a human gate, while the
# worker file itself drives a worker_deployment obligation.
SETTLEMENT_LEDGER_TOKEN = os.getenv("SETTLEMENT_LEDGER_TOKEN")
SETTLEMENT_BATCH_SIZE = os.getenv("SETTLEMENT_BATCH_SIZE", "100")


def reconcile() -> str:
    """Reconcile one settlement batch against the ledger."""
    if not SETTLEMENT_LEDGER_TOKEN:
        raise RuntimeError("SETTLEMENT_LEDGER_TOKEN must be set")
    return f"reconciled batch of {SETTLEMENT_BATCH_SIZE}"
