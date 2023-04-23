from typing import List
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from model.order import Order, MenuElement


Base = declarative_base()


class OrderDB(Base):
    __tablename__ = 'orders'

    id            = Column(Integer, primary_key=True)
    customer_id   = Column(Integer, ForeignKey('customers.id'))
    waiter_id     = Column(Integer, ForeignKey('waiters.id'))
    menu_elements = relationship('dish_to_order', secondary='order_menu_elements', back_populates='orders')

    def __init__(self, order: Order):
        self.order_id    = order.order_id
        self.customer_id = order.customer_id
        self.waiter_id   = order.waiter_id
        # self.menu_elements = [MenuElementDB(menu_element) for menu_element in order.menu_elements]

    def to_domain(self) -> Order:
        return Order(
            order_id    = self.id,
            customer_id = self.customer_id,
            waiter_id   = self.waiter_id,
            # menu_elements=[menu_element.to_domain() for menu_element in self.menu_elements]
        )
class dish_to_orderDB:
    __tablename__ = 'dish_to_order'
    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
    item_id  = Column(Integer, ForeignKey('dishes.id'), nullable=False)

class drink_to_orderDB:
    __tablename__ = 'drink_to_order'
    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
    item_id  = Column(Integer, ForeignKey('drinks.id'), nullable=False)
