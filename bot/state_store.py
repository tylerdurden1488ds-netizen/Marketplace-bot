_users = {}


def set_mode(user_id: int, mode: str):
    _users.setdefault(user_id, {})["mode"] = mode


def get_mode(user_id: int) -> str:
    return _users.get(user_id, {}).get(
        "mode",
        "manual"
    )


def set_pending_photo(
    user_id: int,
    photo_bytes: bytes,
    mime_type: str,
):
    _users.setdefault(user_id, {})["pending"] = {
        "photo_bytes": photo_bytes,
        "mime_type": mime_type,
    }


def get_pending_photo(user_id: int):

    return _users.get(
        user_id,
        {}
    ).get("pending")


def clear_user(user_id: int):

    _users.pop(
        user_id,
        None
    )
