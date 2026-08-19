from pathlib import Path


SKILLS_DIR = Path(__file__).resolve().parent.parent / "skills"


def load_skill(relative_path: str) -> str:
    path = SKILLS_DIR / relative_path
    return path.read_text(encoding="utf-8")


def build_prompt(skill_paths: list[str], user_request: str) -> str:
    parts = [load_skill(path) for path in skill_paths]
    return "\n\n".join(parts) + "\n\nUSER REQUEST:\n" + user_request
