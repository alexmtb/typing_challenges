BANNED_USERS = {167, 921}


def ban_users(users_ids: set) -> int:
    """Length of the set of banned users."""
    return len(users_ids.intersection(BANNED_USERS))


if __name__ == "__main__":
    assert ban_users(users_ids={167, 623, 209, 921}) == 2
