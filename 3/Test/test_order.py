from model.order import Order
from model.menuElement import *
import unittest

class TestOrder(unittest.TestCase):
    
    def test_add_menu_element(self):
        order = Order()
        menu_element = Dish("Pizza", 10)
        order.add_menu_element(menu_element)
        self.assertIn(menu_element, order.menu_elements)
        
    def test_get_total_cost(self):
        order = Order()
        menu_element_1 = Dish(name="Pizza", price=10)
        menu_element_2 = Dish(name="Burger", price=7)
        order.add_menu_element(menu_element_1)
        order.add_menu_element(menu_element_2)
        self.assertEqual(order.get_total_cost(), 17)

    def test_get_order_items(self):
        # Создаем тестовый заказ
        order = Order()
        menu_element1 = Dish("Burger", 100)
        menu_element2 = Dish("Fries", 50)
        order.add_menu_element(menu_element1)
        order.add_menu_element(menu_element2)
        
        # Проверяем, что список позиций заказа возвращается корректно
        expected_items = ["Burger - $100, Cuisine type: Russian", "Fries - $50, Cuisine type: Russian"]
        self.assertEqual(order.get_order_items(), expected_items)
