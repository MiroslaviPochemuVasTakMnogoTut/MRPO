from model.order import Order
from model.fun import *
from model.menuElement import *
import unittest

class TestOrder(unittest.TestCase):
    
    def test_add_menu_element(self):
        order = Order()
        menu_element = Dish("Pizza", 10)
        add_menu_element(order, menu_element)
        self.assertIn(menu_element, order.menu_elements)
        
    def test_get_total_cost(self):
        order = Order()
        menu_element_1 = Dish(name="Pizza", price=10)
        menu_element_2 = Dish(name="Burger", price=7)
        add_menu_element(order, menu_element_1)
        add_menu_element(order, menu_element_2)
        self.assertEqual(get_total_cost(order), 17)

    def test_get_order_items(self):
        # Создаем тестовый заказ
        order = Order()
        menu_element1 = Dish("Burger", 100)
        menu_element2 = Dish("Fries", 50)
        add_menu_element(order, menu_element1)
        add_menu_element(order, menu_element2)
        
        # Проверяем, что список позиций заказа возвращается корректно
        expected_items = ["Burger - $100, Cuisine type: Russian", "Fries - $50, Cuisine type: Russian"]
        self.assertEqual(get_order_items(order), expected_items)
