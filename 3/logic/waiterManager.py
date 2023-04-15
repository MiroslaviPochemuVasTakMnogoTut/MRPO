from model.waiter import Waiter

class WaiterManager:
    def __init__(self):
        self.waiters = []

    def add_waiter(self, name, birthdate, phone):
        waiter = Waiter(name, birthdate, phone)
        self.waiters.append(waiter)
        return waiter

    def remove_waiter(self, waiter):
        self.waiters.remove(waiter)

    def find_waiter_by_name(self, name):
        for waiter in self.waiters:
            if waiter.name == name:
                return waiter
        return None

    def update_waiter_info(self, waiter, name=None, birthdate=None, phone=None):
        if name:
            waiter.name = name
        if birthdate:
            waiter.birthdate = birthdate
        if phone:
            waiter.phone = phone
