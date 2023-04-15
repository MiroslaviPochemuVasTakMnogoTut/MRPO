from dataclasses import dataclass
from typing import List
from order import Order

@dataclass(frozen=True)
class Receipt:
    orders: List[Order]
    total: float
    tax: float
    discount: float
    final_total: float

    def __str__(self):
        output = "ORDER SUMMARY:\n\n"
        for order in self.orders:
            output += f"{order}\n"
        output += "\n"
        output += f"Subtotal: ${self.total:.2f}\n"
        output += f"Tax: ${self.tax:.2f}\n"
        output += f"Discount: ${self.discount:.2f}\n"
        output += f"Total: ${self.final_total:.2f}\n"
        return output
