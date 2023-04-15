from typing import List
from datetime import date
from person import Person
        
class Employee(Person):
    def __init__(self, name: str, birthdate: date):
        super().__init__(name, birthdate)
        self.employee_id
        self.position
        self.salary