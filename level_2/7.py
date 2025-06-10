

def calculate_total_spent_for_user(user: tuple[str, int, list[int]]) -> int:
    """Calculate the total sum of purhcases."""
    if isinstance(user, tuple) and len(user) == 3:
        _, _, purchase_sum = user
        if isinstance(purchase_sum, list):
            return sum(purchase_sum)
    return 0


if __name__ == "__main__":
    assert calculate_total_spent_for_user(user=("Ilya", 32, [102, 15, 63, 12])) == 192
