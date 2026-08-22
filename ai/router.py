from ai.skill_loader import load_skills


MARKETPLACE_SKILLS = {
    "wildberries": "marketplaces/wildberries.md",
    "ozon": "marketplaces/ozon.md",
    "avito": "marketplaces/avito.md",
    "yandex_market": "marketplaces/yandex_market.md",
}


def choose_background(user_request: str) -> str:

    text = (user_request or "").lower()

    if any(word in text for word in [
        "кухня",
        "кухон",
        "стол",
        "посуда",
        "kitchen",
    ]):
        return "backgrounds/kitchen.md"

    if any(word in text for word in [
        "ванная",
        "ванну",
        "душ",
        "bathroom",
    ]):
        return "backgrounds/bathroom.md"

    if any(word in text for word in [
        "офис",
        "компьютер",
        "office",
    ]):
        return "backgrounds/office.md"

    if any(word in text for word in [
        "мрамор",
        "marble",
    ]):
        return "backgrounds/marble.md"

    return "backgrounds/universal.md"


def choose_skills(
    user_request: str,
    marketplace: str = "universal",
) -> list[str]:

    skills = [
        "taste/core.md",
        "product/fidelity.md",
        "composition/core.md",
        "typography/core.md",
        "infographic/core.md",
        "emojis/core.md",
    ]

    background = choose_background(
        user_request
    )

    skills.append(background)

    marketplace_skill = MARKETPLACE_SKILLS.get(
        marketplace
    )

    if marketplace_skill:
        skills.append(
            marketplace_skill
        )

    return skills


def get_skill_context(
    user_request: str,
    marketplace: str = "universal",
) -> str:

    skills = choose_skills(
        user_request,
        marketplace,
    )

    return load_skills(skills)
