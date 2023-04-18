from typing import List
from datetime import date
from model.person import Person


class Employee(Person):
    def __init__(self, name: str, birthdate: date):
        super().__init__(name, birthdate)
        self.employee_id = None
        self.position = None
        self.salary = None

    # def __eq__(self, other):
    #     if not isinstance(other, self.__class__):
    #         return False
    #     return (super().__eq__(other) and
    #             self.employee_id == other.employee_id and 
    #             self.position == other.position and 
    #             self.salary == other.salary)
