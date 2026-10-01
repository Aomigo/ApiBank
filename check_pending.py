import time
from datetime import datetime, timedelta

from complete_transaction import complete_transaction


def poll_pending(account_repo, transaction_repo):
    while True:
        limit = datetime.now() - timedelta(seconds=30)
        for transaction in transaction_repo.get_pending_transactions():
            if transaction.emited_at <= limit:
                complete_transaction(transaction, account_repo, transaction_repo)
        time.sleep(1)