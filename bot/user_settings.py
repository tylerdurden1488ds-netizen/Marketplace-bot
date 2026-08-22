_users = {}


def set_marketplace(user_id: int, marketplace: str):
    _users.setdefault(user_id, {})["marketplace"] = marketplace


def get_marketplace(user_id: int) -> str:
    return _users.get(user_id, {}).get(
        "marketplace",
        "universal"
    )


def set_mode(user_id: int, mode: str):
    _users.setdefault(user_id, {})["mode"] = mode


def get_mode(user_id: int) -> str:
    return _users.get(user_id, {}).get(
        "mode",
        "manual"
    )
