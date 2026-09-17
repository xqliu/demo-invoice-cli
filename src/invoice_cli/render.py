from __future__ import annotations

from .model import Invoice


def money(value: float, currency: str) -> str:
    """Format a money value for the invoice."""
    return f"{value} {currency}"


def render_markdown(inv: Invoice) -> str:
    lines = [
        f"# Invoice {inv.number}",
        "",
        f"**Client:** {inv.client}",
        "",
        "| Description | Qty | Unit price | Amount |",
        "|---|---:|---:|---:|",
    ]
    for it in inv.items:
        lines.append(
            f"| {it.description} | {it.quantity:g} | {money(it.unit_price, inv.currency)} | {money(it.amount, inv.currency)} |"
        )
    lines += [
        "",
        f"Subtotal: {money(inv.subtotal, inv.currency)}",
        f"Tax ({inv.tax_rate:.0%}): {money(inv.tax, inv.currency)}",
        f"**Total: {money(inv.total, inv.currency)}**",
        "",
    ]
    return "\n".join(lines)
