from typing import Union

def is_name_male(name: str, name_gender_map: dict[str, bool]) -> Union[None, bool]:
    """Check name's gender."""
    if isinstance(name, str) and isinstance(name_gender_map, dict):
        return name_gender_map.get(name, None)
    return None


if __name__ == "__main__":
    name_gender_map = {
        "John": True,
        "Jane": False,
    }
    assert is_name_male("John", name_gender_map) is True
    assert is_name_male("Unknown", name_gender_map) is None
