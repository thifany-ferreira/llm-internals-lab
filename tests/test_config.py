import os
from pathlib import Path

from llm_lab.config import load_env

ROOT = Path(__file__).resolve().parents[1]


def test_load_env_reads_key(tmp_path, monkeypatch):
    monkeypatch.delenv("GROQ_API_KEY", raising=False)
    env = tmp_path / ".env"
    env.write_text("# comentario\nGROQ_API_KEY=abc123\n", encoding="utf-8")
    load_env(str(env))
    assert os.environ["GROQ_API_KEY"] == "abc123"


def test_missing_env_file_does_not_crash(tmp_path):
    load_env(str(tmp_path / "nao-existe.env"))


def test_env_file_is_gitignored():
    lines = (ROOT / ".gitignore").read_text(encoding="utf-8").splitlines()
    assert ".env" in lines, "a chave do Groq nao pode ir pro GitHub"
