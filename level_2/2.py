# from constants import ___


def is_recovery_code_correct(code: str, user_codes: list[str]) -> bool:
    """Check if recovery code is in user codes."""
    if isinstance(code, str) and isinstance(user_codes, list):
        return code in user_codes
    return False


if __name__ == "__main__":
    assert is_recovery_code_correct(code="5212", user_codes=["1862", "8172", "7212"]) is False
