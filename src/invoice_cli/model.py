from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class LineItem:
    description: str
    quantity: float
    unit_price: float

    @property
    def amount(self) -> float:
        return self.quantity * self.unit_price


@dataclass
class Invoice:
    number: str
    client: str
    currency: str = "USD"
    tax_rate: float = 0.0
    items: list[LineItem] = field(default_factory=list)

    @property
    def subtotal(self) -> float:
        return sum(i.amount for i in self.items)

    @property
    def tax(self) -> float:
        return self.subtotal * self.tax_rate

    @property
    def total(self) -> float:
        return self.subtotal + self.tax
