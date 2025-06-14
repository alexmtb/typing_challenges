# from ..constants import ___

# Example usage
BANNED_USERS = [32, 42, 73]

def is_user_banned(user_id: int) -> bool:
    """Check if user_id is in banned list."""
    return user_id in BANNED_USERS

if __name__ == "__main__":
    assert is_user_banned(user_id=32) is True
