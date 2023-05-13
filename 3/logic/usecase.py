from data.repository import XMLWaiter
from model.waiter import Waiter

class WaiterToXML:
    def __init__(self):
        self.repo  = XMLWaiter(Waiter)
    def add(self, name, birthdate):

        waiter = {'name': name, 'birthdate': birthdate}
        self.repo.add(waiter, 'waiters')
    
    def update(self, waiter: Waiter):
        wid = waiter.id
        nitem = {'name': waiter.name, 'birthdate': waiter.birthdate}
        self.repo.update(wid, nitem, 'waiters')
    
    def remove(self, id):
        self.repo.remove(id,'waiters')
        
    def get_all(self):
        waiters = self.repo.get_all('waiters')
        lst =[]
        for wtr in waiters:
            lst.append(Waiter(wtr['name'], wtr['birthdate']))
        return lst
