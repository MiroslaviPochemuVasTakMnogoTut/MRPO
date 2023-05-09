from data.repository import XMLWaiter
from model.waiter import Waiter

class WaiterToXML:
    def __init__(self):
        pass
    def add(self, name, birthdate):
        repo  = XMLWaiter(Waiter)
        waiter = Waiter(name, birthdate)
        repo.add(waiter)

