import decimal
from typing import Union


def get_transaction_amount(
        transaction_id: int, transactions_amounts_map: dict[int, decimal.Decimal]
    ) -> Union[None, decimal.Decimal]:
    """Get the amount of a transaction by ID."""
    if transaction_id in transactions_amounts_map:
        return transactions_amounts_map[transaction_id]
    
    return None


if __name__ == "__main__":
    transactions_amounts_map = {
        156: decimal.Decimal("30.6"),
        514: decimal.Decimal("164.1"),
        372: decimal.Decimal("92"),
    }
    assert get_transaction_amount(transaction_id=156, transactions_amounts_map=transactions_amounts_map) == decimal.Decimal("30.6")
    assert get_transaction_amount(transaction_id=1000, transactions_amounts_map=transactions_amounts_map) is None
