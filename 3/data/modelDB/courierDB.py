from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model.courier import Courier
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class CourierDB(Base):
    __tablename__ = 'couriers'

    id               = Column(Integer, primary_key=True)
    name             = Column(String)
    birthdate        = Column(String)
    phone            = Column(String)
    vehicle_type     = Column(String)
    vehicle_number   = Column(String)
    # current_location = Column(String)

    def __init__(self, courier):
        self.id             = courier.id
        self.name           = courier.name
        self.birthdate      = courier.birthdate
        self.phone          = courier.phone
        self.vehicle_type   = courier.vehicle_type
        self.vehicle_number = courier.vehicle_number
        # self.current_location = courier.current_location

    def to_domain(self):
        courier = Courier(
            name             = self.name,
            birthdate        = self.birthdate,
            phone            = self.phone,
            vehicle_type     = self.vehicle_type,
            vehicle_number   = self.vehicle_number,
            # current_location = None
        )
        courier.id = self.id
        return courier
