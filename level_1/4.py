import datetime


def calculate_age(date_of_birth: datetime.date) -> int:
    '''Calculate age from date of birth.'''
    today = datetime.date.today().year
    age = today - date_of_birth.year
    return age


if __name__ == "__main__":
    assert calculate_age(date_of_birth=datetime.date(1965, 6, 2)) == 60 # 57


# В оригинальном задании было сравнение с возарстом = 57 лет.
# С поправкой на дату составленния курса исправил на актуальное значение.