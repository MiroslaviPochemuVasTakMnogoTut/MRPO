from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from model.table import Table

Base = declarative_base()

class Table(Base):
    __tablename__ = 'tables'

    id       = Column(Integer, primary_key=True)
    number   = Column(Integer)
    capacity = Column(Integer, default=4)
    # is_available = Column(Boolean, default=True)
    # waiter = Column(String)

    def __init__(self, table: Table):
        self.id       = table.id
        self.number   = table.number
        self.capacity = table.capacity
