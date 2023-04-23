from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from model.menuElement import *

Base = declarative_base()

class DrinkDB(Base):
    __tablename__ = 'drinks'

    id           = Column(Integer, primary_key=True)
    name         = Column(String)
    description  = Column(String)
    price        = Column(Float)
    kitchen      = Column(String)
    cuisine_type = Column(String)
    
    def __init__(self, drink: Drink):
        self.id          = drink.id
        self.name        = drink.name
        self.description = drink.description
        self.price       = drink.price
        

    def to_domain(self) -> Dish:
        return Drink(
            name        = self.name,
            description = self.description,
            price       = self.price,
            kitchen     = self.kitchen,
            volume      = self.volume
        )
        
    class DishDB(Base):
        __tablename__ = 'dishes'
        
        id          = Column(Integer, primary_key=True)
        name        = Column(String)
        description = Column(String)
        price       = Column(Float)
        kitchen     = Column(String)
        
        def __init__(self, dish: Dish):
            self.id           = dish.id
            self.name         = dish.name
            self.description  = dish.description
            self.price        = dish.price
            self.cuisine_type = dish.cuisine_type
            

        def to_domain(self) -> Dish:
            return Dish(
                name         = self.name,
                description  = self.description,
                price        = self.price,
                kitchen      = self.kitchen,
                cuisine_type = self.cuisine_type,
            )
        
