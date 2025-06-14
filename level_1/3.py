# from constants import ___
from typing import Union


def compose_full_name(first_name: str, last_name: str, middle_name: Union[None, str]) -> str:
    '''Make a string from first name, last name, and middle name.'''
    if middle_name:
        return f"{last_name} {first_name} {middle_name}"
    else:
        return f"{last_name} {first_name}"

if __name__ == "__main__":
    assert compose_full_name(first_name="John", last_name="Doe", middle_name=None) == "Doe John"
    assert compose_full_name(first_name="Ilya", last_name="Lebedev", middle_name="Alexeyevich") == "Lebedev Ilya Alexeyevich"
