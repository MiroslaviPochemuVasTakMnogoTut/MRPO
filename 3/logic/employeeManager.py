from abc import ABC, abstractmethod

class EmployeeManager(ABC):
    def __init__(self):
        self.employees = []

    @abstractmethod
    def add_employee(self, name, birthdate, phone):
        pass

    @abstractmethod
    def remove_employee(self, employee):
        pass

    @abstractmethod
    def find_by_name(self, name):
        pass

    @abstractmethod
    def update_info(self, employee, name=None, birthdate=None, phone=None):
        pass
