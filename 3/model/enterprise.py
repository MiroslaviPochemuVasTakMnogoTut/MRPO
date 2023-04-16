from typing import List
from kitchen import Kitchen

class Enterprise:
    def __init__(self, name: str, kitchens: List[Kitchen]):
        self.name = name
        self.kitchens = kitchens
        self.adress
        
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name and self.adress == other.adress