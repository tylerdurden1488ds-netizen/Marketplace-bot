from ai.skill_loader import load_skills


def choose_skills(user_request: str) -> list[str]:
    text = (user_request or "").lower()

    skills = [
        "taste/core.md",
        "product/fidelity.md",
        "composition/core.md",
        "typography/core.md",
        "infographic/core.md",
        "emojis/core.md",
    ]

    if any(word in text for word in [
        "кухня",
        "кухон",
        "стол",
        "посуда",
        "kitchen",
    ]):
        skills.append("backgrounds/kitchen.md")

    elif any(word in text for word in [
        "ванная",
        "ванну",
        "bathroom",
    ]):
        skills.append("backgrounds/bathroom.md")

    elif any(word in text for word in [
        "офис",
        "компьютер",
        "office",
    ]):
        skills.append("backgrounds/office.md")

    elif any(word in text for word in [
        "мрамор",
        "marble",
    ]):
        skills.append("backgrounds/marble.md")

    else:
        skills.append("backgrounds/universal.md")

    return skills


def get_skill_context(user_request: str) -> str:
    skills = choose_skills(user_request)

    return load_skills(skills)
