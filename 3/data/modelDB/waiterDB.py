from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from model.waiter import Waiter
Base = declarative_base()


class WaiterDB(Base):
    __tablename__ = 'waiters'

    id        = Column(Integer, primary_key=True)
    name      = Column(String)
    birthdate = Column(String)
    phone     = Column(String)

    def __init__(self, waiter: Waiter):
        self.id        = waiter.id
        self.name      = waiter.name
        self.birthdate = waiter.birthdate
        self.phone     = waiter.phone

    def to_domain(self):
        waiter = Waiter(
            name      = self.name,
            birthdate = self.birthdate,
            phone     = self.phone,
        )
        waiter.id = self.id
        return waiter
