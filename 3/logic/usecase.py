from data.repository import XMLRepo
from model.waiter import Waiter
# from data.modelDB.waiterDB import WaiterDB
from data.uow import AbstractUoW

class WaiterToXML:
    def __init__(self):
        self.repo  = XMLRepo(Waiter)
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
    
def add_waiter(waiter:Waiter, uow: AbstractUoW):
    with uow :
        uow.repo.add(waiter)
        
def update_waiter(waiter:dict, uow:AbstractUoW):
    with uow :
        return uow.repo.update(waiter)
        
def remove_waiter(id, uow:AbstractUoW):
    with uow :
        uow.repo.remove(id)
        
def get_waiter(id, uow:AbstractUoW):
    with uow :
        return uow.repo.get_by_id(id)
def get_waiters(uow:AbstractUoW):
    with uow :
        return uow.repo.get_all()





    # wtr = {'id':waiter.id,
    #        'name':waiter.name,
    #        'birthdate':waiter.birthdate,
    #        'phone':waiter.phone}
    # wtr = {'name':waiter.name,
    #        'birthdate':waiter.birthdate,
    #        'phone':waiter.phone}