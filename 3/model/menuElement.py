from abc import ABC, abstractmethod

class MenuElement(ABC):
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
        self.kitchen

    @abstractmethod
    def add_to_order(self, order):
        pass

    def get_info(self):
        return f'{self.name} - {self.description}, {self.price}$'
    
    def __eq__(self, other):
        if type(other).__name__ == self.__class__.__name__:
            return self.get_info() == other.get_info()
        return False
        


class Dish(MenuElement):
    def __init__(self, name, description, price, cuisine_type):
        super().__init__(name, description, price)
        self.cuisine_type = cuisine_type

    def add_to_order(self, order):
        order.add_dish(self)

    def get_info(self):
        return f'{super().get_info()}, Cuisine type: {self.cuisine_type}'

class Drink(MenuElement):
    def __init__(self, name, description, price, volume):
        super().__init__(name, description, price)
        self.volume = volume

    def add_to_order(self, order):
        order.add_drink(self)

    def get_info(self):
        return f'{super().get_info()}, Volume: {self.volume} ml'
