from typing import Union

def stringify(value: Union[None, int, float, str]) -> str:
    try:
        return str(value)
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    assert stringify(value="12") == "12"
    assert stringify(value=15) == "15"
    assert stringify(value=.5) == "0.5"
    assert stringify(value=None) == "None"
