from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

from .model import Invoice, LineItem
from .render import render_markdown


def load(path: Path) -> Invoice:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    items = [LineItem(**row) for row in data.get("items", [])]
    return Invoice(
        number=str(data["number"]),
        client=data["client"],
        currency=data.get("currency", "USD"),
        tax_rate=float(data.get("tax_rate", 0.0)),
        items=items,
    )


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="invoice", description="YAML line items in, Markdown invoice out.")
    ap.add_argument("file", type=Path, help="invoice YAML")
    ap.add_argument("-o", "--output", type=Path, help="write Markdown here instead of stdout")
    args = ap.parse_args(argv)
    md = render_markdown(load(args.file))
    if args.output:
        args.output.write_text(md, encoding="utf-8")
    else:
        sys.stdout.write(md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
