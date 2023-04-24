from abc import ABC, abstractmethod, abstractproperty
from typing import List
from datetime import date

class Person:
    def __init__(self, name: str, birthdate: date):
        self.id = None
        self.name = name
        self.birthdate = birthdate
        self.phone = ''
    # @abstractproperty
    # def name(self):
    #     return self._name
    
    # @abstractproperty
    # def age(self):
    #     pass
    

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.phone == other.phone and self.birthdate == other.birthdate and self.name == other.name
