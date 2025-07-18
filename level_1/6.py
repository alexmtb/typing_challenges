# from constants import ___
from typing import Union


def is_loan_amount_too_big(
        loan_amount_usd: int,
        max_loan_amount_for_user_usd: Union[None, int]
    ) -> bool:
    """Check if the loan amount is too big for the user."""

    if max_loan_amount_for_user_usd is None:
        return False
    
    return loan_amount_usd > max_loan_amount_for_user_usd


if __name__ == "__main__":
    assert is_loan_amount_too_big(
        loan_amount_usd=1000, max_loan_amount_for_user_usd=4000) is False
    assert is_loan_amount_too_big(
        loan_amount_usd=1000, max_loan_amount_for_user_usd=None) is False
