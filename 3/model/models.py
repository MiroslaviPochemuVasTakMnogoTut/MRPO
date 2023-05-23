from abc import ABC, abstractmethod, abstractproperty
from typing import List
from datetime import date
from dataclasses import dataclass



class Person:
    def __init__(self, name: str, birthdate: date):
        self.id = None
        self.name = name
        self.birthdate = birthdate
        self.phone = ''
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.phone == other.phone and self.birthdate == other.birthdate and self.name == other.name 

class Employee(Person):
    def __init__(self, name: str, birthdate: date):
        super().__init__(name, birthdate)
        # self.id = None


class Courier(Employee):
    def __init__(self, name, birthdate, phone):
        super().__init__(name, birthdate, phone=phone)
        self.id = None
        self.vehicle_type
        self.vehicle_number
        self.delivery_orders = []
        self.current_location = None
        
class Waiter(Employee):
    def __init__(self, name, birthdate):
        super().__init__(name, birthdate)
        self.tables_served = []
        
    def serialize(self, serializer):
        # serializer - это объект сериализатора
        serializer.start_object('waiter', self.id)
        serializer.add_property('name', self.name)
        serializer.add_property('phone', self.phone)
        return serializer.to_str()
        
class Table:
    def __init__(self, number: int):
        self.id = None
        self.number = number
        self.capacity = 4
        self.is_available = True
        self.waiter :str= ''
        self.state = 'available'
        
    def status(self):
        while True:
            event = yield self.state # Генератор yield, используется как корутина для асинхронного вызова
            if self.state == 'Free': # 
                if event == 'Occupy Table':
                    self.state = 'Occupied'
                elif event == 'Reserve Table':
                    self.state = 'Reserved'
            elif self.state == 'Occupied':
                if event == 'Free Table':   
                    self.state = 'Free'
                elif event == 'Reserve Table':
                    self.state = 'Reserved'
            elif self.state == 'Reserved':
                if event == 'Cancel Reservation':
                    self.state = 'Free'
                elif event == 'Occupy Table':
                    self.state = 'Occupied'
                    

    def __eq__(self, other):
        if not isinstance(other, Table):
            return False
        return self.number == other.number and self.capacity == other.capacity
    
class Enterprise:
    def __init__(self, name: str, kitchens):
        self.name = name
        self.kitchens = kitchens
        self.adress
        
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name and self.adress == other.adress
        
        
class Kitchen:
    def __init__(self, name: str, enterprise: Enterprise):
        self.name = name
        self.enterprise = enterprise
        
    def cook(self, request):
        pass
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return False
        return self.name == other.name and self.enterprise == other.enterprise
    
    
class MenuElement(ABC):
    def __init__(self, name, price):
        self.name = name
        self.description = ''
        self.price = price
        self.kitchen = None


    @abstractmethod
    def get_info(self):
        return f'{self.name} - ${self.price}'
    
    def __eq__(self, other):
        if type(other).__name__ == self.__class__.__name__:
            return self.get_info() == other.get_info()
        return False
        


class Dish(MenuElement):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.cuisine_type = 'Russian'

    def get_info(self):
        return f'{super().get_info()}, Cuisine type: {self.cuisine_type}'

class Drink(MenuElement):
    def __init__(self, name, description, price, volume):
        super().__init__(name, description, price)
        self.volume = volume

    def get_info(self):
        return f'{super().get_info()}, Volume: {self.volume} ml'


class Order:
    def __init__(self):
        self.order_id      = None
        self.customer_id   = None
        self.waiter_id     = None
        self.menu_elements = []
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.order_id == other.order_id
        


class Customer(Person):
    def __init__(self, name: str, birthdate: date, email: str):
        super().__init__(name, birthdate)
        # self.customer_id
        self.phone
        self.email = email
        self.orders: List[Order] = []



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


def add_menu_element(entity, menu_element):
    entity.menu_elements.append(menu_element)

def get_total_cost(entity):
    total = 0
    for element in entity.menu_elements:
        total += element.price
    return total

def get_order_items(entity):
    items = []
    for element in entity.menu_elements:
        items.append(element.get_info())
    return items

def serve_table(entity, table:Table):
    if table.is_available:
        table.mark_as_unavailable(entity.name)##################################
        entity.tables_served.append(table)
        return f"Table {table.number} is now served by {entity.name}."
    else:
        return f"Table {table.number} is already served by {table.waiter}."


def mark_as_available(entity):
    entity.is_available = True
    entity.order = None

def mark_as_unavailable(entity, waiter):
    entity.is_available = False
    entity.waiter = waiter