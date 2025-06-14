import decimal
import uuid

# from constants import ___


def get_user_balance(user_id: uuid.UUID) -> decimal.Decimal:
    """Get user balance by user ID."""
    # Simulating a database call
    user_balance = {
        user_id: decimal.Decimal("265.2")
    }

    return user_balance.get(user_id)
    
if __name__ == "__main__":
    assert get_user_balance(user_id=uuid.uuid4()) == decimal.Decimal("265.2")
