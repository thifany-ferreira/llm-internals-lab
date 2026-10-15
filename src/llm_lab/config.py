import os
from pathlib import Path


def load_env(path: str = ".env") -> None:
    """Le o .env sem dependencia extra. Nao sobrescreve variaveis ja definidas."""
    p = Path(path)
    if not p.exists():
        return
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def groq_key() -> str | None:
    load_env()
    return os.environ.get("GROQ_API_KEY") or None
