from data.repository import SQLRepository, XMLWaiter
from data.modelDB.waiterDB import WaiterDB
from model.waiter import Waiter
from logic.usecase import WaiterToXML

def main():
    waiter1 = Waiter("John","2000-01-01")
    waiter2 = Waiter("Mike","2000-01-01")
    
    service = WaiterToXML()
    service.add("John", "2001-01-01")
    # wmod1 = WaiterDB(waiter1)
    # wmod2 = WaiterDB(waiter2)
    # repo = SQLRepository(WaiterDB)
    # repo.add(wmod1)
    # repo.add(wmod2)
    # wmod3 = repo.get_by_id(1)
    # wmod3.name = 'Sghrek'
    # repo.update(wmod3)



if __name__=='__main__':
    main()