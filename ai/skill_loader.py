from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = PROJECT_ROOT / "skills"


def read_skill(path: str) -> str:

    file_path = SKILLS_DIR / path

    if not file_path.exists():
        return ""

    return file_path.read_text(
        encoding="utf-8"
    )


def load_skills(paths: list[str]) -> str:

    result = []

    for path in paths:

        content = read_skill(path)

        if not content:
            continue

        result.append(
            f"\n--- SKILL: {path} ---\n"
            f"{content}"
        )

    return "\n".join(result)
