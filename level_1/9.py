# from constants import ___
from typing import Union


def is_correct_int(raw_int: Union[None, str]) -> bool:
    '''Check conversion str -> int'''
    try:
        int(raw_int)
        return True
    except (ValueError, TypeError):
        return False


if __name__ == "__main__":
    assert is_correct_int(raw_int="12") is True
    assert is_correct_int(raw_int="12&") is False
    assert is_correct_int(raw_int=None) is False
