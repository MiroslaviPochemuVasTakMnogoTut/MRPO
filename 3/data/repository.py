from abc import ABC, abstractmethod
 
class Repository(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def add(self, item):
        pass
    @abstractmethod
    def remove(self, item):
        pass
    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def get_by_id(self, id):
        pass

class FakeRepo(Repository):
    def __init__(self):
        self.base = []
        pass
    def add(self, item):
        self.base.append(item)
    def remove(self, item):
        self.base.remove(item)
    def get_all(self):
        return self.base
    def get_by_id(self, id):
        return self.base[id]