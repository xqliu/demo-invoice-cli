from invoice_cli.model import Invoice, LineItem


def test_amount_and_totals():
    inv = Invoice(number="1", client="c", tax_rate=0.1, items=[LineItem("a", 2, 10.0), LineItem("b", 1, 5.0)])
    assert inv.subtotal == 25.0
    assert inv.tax == 2.5
    assert inv.total == 27.5
