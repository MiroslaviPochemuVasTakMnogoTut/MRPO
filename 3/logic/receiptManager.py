from typing import List
from model.receipt import Receipt

class ReceiptManager:
    def __init__(self):
        self.receipts = []

    def create_receipt(self, orders, total, tax, discount, final_total):
        receipt = Receipt(orders, total, tax, discount, final_total)
        self.receipts.append(receipt)
        return receipt

    def get_receipts(self) -> List[Receipt]:
        return self.receipts
