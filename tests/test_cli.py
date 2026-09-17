from pathlib import Path

from invoice_cli.cli import load, main


def test_load_example():
    inv = load(Path(__file__).parent.parent / "examples" / "acme-2026-09.yaml")
    assert inv.client == "Acme Robotics"
    assert len(inv.items) == 3


def test_main_writes_markdown(tmp_path, capsys):
    src = Path(__file__).parent.parent / "examples" / "acme-2026-09.yaml"
    out = tmp_path / "inv.md"
    assert main([str(src), "-o", str(out)]) == 0
    text = out.read_text()
    assert text.startswith("# Invoice 2026-014")
    assert "Acme Robotics" in text
