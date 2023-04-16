
from enterprise import Enterprise

class Kitchen:
    def __init__(self, name: str, enterprise: Enterprise):
        self.name = name
        self.enterprise = enterprise
        
    def cook(self, request):
        pass
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return False
        return self.name == other.name and self.enterprise == other.enterprise