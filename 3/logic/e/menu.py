from model.menuElement import MenuElement
from data.repository import FakeRepo

class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item: MenuElement):
        pass

    def remove_item(self, item: MenuElement):
        pass
        # if item in self.items:
        #     del self.items[item]
        # if item in self.prices:
        #     del self.prices[item]

    def get_items(self):
        pass
        # return self.items.keys()

    def get_price(self, item: MenuElement):
        pass
        # return self.prices[item]
        

    def set_price(self, item, price):
        pass
        # if item in self.items:
        #     self.prices[item] = price


def __str__(self):
    menu_str = ""
    for item in self.items:
        menu_str += f"{item.name} - {self.prices[item]} руб.\n"
    return menu_str
