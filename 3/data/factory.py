from data.repository import *
from data.uow import *

class WaiterSerializer:
    def repositize(self, format):
        serializer = get_repositizer(format)
        return serializer()

def get_repositizer(format:str):
    if format.lower() == 'json':
        return _json_repositizer
    elif format.lower() == 'xml':
        return _xml_repositizer
    else: return ValueError('Invalid format')
    
def _json_repositizer():
    return JsonRepo()
    # uow = JsonUoW()
    # with uow:
    #     uow.repo.add(waiter)

def _xml_repositizer():
    return XMLRepo()
    # uow = XMLUoW()
    # with uow:
    #     uow.repo.add(waiter)