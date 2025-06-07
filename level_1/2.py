# from constants import ___


def is_adult(age: int, country_name: str) -> bool:
    return country_name == "Russia" and age >= 16

if __name__ == "__main__":
    assert is_adult(age=17, country_name="Russia") is True
