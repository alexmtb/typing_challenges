# from constants import ___


def send_email(header: str, text_content: str, send_to: str) -> None:
    '''Check if email is correct and send it.'''
    if '@' not in send_to or not send_to.endswith('.com'):
        raise ValueError("Corrupted email address")
    if not header or not text_content:
        raise ValueError("E-mail header and text cannot be empty")
    
    # If successfully sent, return None
    return None


if __name__ == "__main__":
    assert send_email(header="Test email", text_content="This is a test email", send_to="test@gmail.com") is None
