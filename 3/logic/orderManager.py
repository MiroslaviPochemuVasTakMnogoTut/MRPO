from typing import List
from datetime import datetime
from model.order import Order
from model.table import Table
from model.waiter import Waiter
class OrderManager:
    def __init__(self):
        self.orders = []

    def create_order(self, client, waiter, dishes):
        order = Order(client, waiter, dishes)
        self.orders.append(order)
        client.orders.append(order)  # добавляем заказ в список заказов клиента
        return order

    def create_order(self, table: Table, waiter: Waiter, items: List[str], menu) -> Order:
        # order_id = len(self.orders) + 1
        order = Order(table_number, waiter, items)
        total = order.get_total(menu)
        order.total = total
        self.orders.append(order)
        return order

    def get_order_by_id(self, order_id: int) -> Order:
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None

    def get_orders_by_table_number(self, table_number: int) -> List[Order]:
        orders = []
        for order in self.orders:
            if order.table_number == table_number:
                orders.append(order)
        return orders

    def get_orders_by_waiter(self, waiter: str) -> List[Order]:
        orders = []
        for order in self.orders:
            if order.waiter == waiter:
                orders.append(order)
        return orders

    def complete_order(self, order_id: int):
        order = self.get_order_by_id(order_id)
        if order:
            order.complete_order()

    def get_total_sales(self):
        total_sales = 0
        for order in self.orders:
            if order.time_completed:
                total_sales += order.total
        return total_sales
