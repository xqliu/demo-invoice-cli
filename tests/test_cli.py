from pathlib import Path

import pytest

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


def _write_invoice(tmp_path, body):
    path = tmp_path / "invoice.yaml"
    path.write_text(body, encoding="utf-8")
    return path


def test_load_without_items_key_raises(tmp_path):
    path = _write_invoice(tmp_path, "number: 1\nclient: x\n")
    with pytest.raises(ValueError) as excinfo:
        load(path)
    assert str(excinfo.value) == f"no items in {path}"


def test_load_with_empty_items_raises(tmp_path):
    path = _write_invoice(tmp_path, "number: 1\nclient: x\nitems: []\n")
    with pytest.raises(ValueError) as excinfo:
        load(path)
    assert str(excinfo.value) == f"no items in {path}"


def test_main_reports_empty_invoice_on_stderr(tmp_path, capsys):
    path = _write_invoice(tmp_path, "number: 1\nclient: x\n")
    out = tmp_path / "inv.md"
    assert main([str(path), "-o", str(out)]) == 2
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err.strip() == f"no items in {path}"
    assert not out.exists()
