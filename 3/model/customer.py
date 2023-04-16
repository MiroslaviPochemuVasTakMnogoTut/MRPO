from typing import List
from datetime import date
from person import Person
from order import Order
        
class Customer(Person):
    def __init__(self, name: str, birthdate: date, email: str):
        super().__init__(name, birthdate)
        # self.customer_id
        self.phone
        self.email = email
        self.orders: List[Order] = []
