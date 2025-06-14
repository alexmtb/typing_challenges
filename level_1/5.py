# from constants import ___


def is_correct_email(raw_email: str) -> bool:
    '''Check if the input email is correct.'''
    if '@' not in raw_email:
        return False
    if not raw_email.endswith('.com'):
        return False
    
    return True


if __name__ == "__main__":
    assert is_correct_email(raw_email="test@gmail.co") is False
