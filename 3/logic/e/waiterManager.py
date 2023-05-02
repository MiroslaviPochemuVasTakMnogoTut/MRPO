from model.waiter import Waiter
from employeeManager import EmployeeManager

class WaiterManager(EmployeeManager):
    def __init__(self):
        super().__init__()

    def add_employee(self, name, birthdate, phone):
        waiter = Waiter(name, birthdate, phone)
        super().employees.append(waiter)
        return waiter

    def remove_employee(self, waiter : Waiter):
        self.employees.remove(waiter)

    def find_by_name(self, name)-> Waiter:
        for waiter in super().employees:
            if waiter.name == name:
                return waiter
        return None

    def update_info(self, waiter, name=None, birthdate=None, phone=None):
        if name:
            waiter.name = name
        if birthdate:
            waiter.birthdate = birthdate
        if phone:
            waiter.phone = phone
