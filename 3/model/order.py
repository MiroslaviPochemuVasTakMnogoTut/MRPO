

class Order:
    def __init__(self):
        self.menu_elements = []

    def add_menu_element(self, menu_element):
        self.menu_elements.append(menu_element)

    def get_total_cost(self):
        total = 0
        for element in self.menu_elements:
            total += element.price
        return total

    def get_order_items(self):
        items = []
        for element in self.menu_elements:
            items.append(element.get_info())
        return items
    
    