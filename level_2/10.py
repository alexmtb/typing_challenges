

def is_point_in_square(
        point: tuple[int],
        left_upper_corner: tuple[int],
        right_bottom_corner: tuple[int]) -> bool:
    pass


if __name__ == "__main__":
    assert is_point_in_square(
        point=(10, 12),
        left_upper_corner=(5, 5),
        right_bottom_corner=(20, 15)
    ) is True
