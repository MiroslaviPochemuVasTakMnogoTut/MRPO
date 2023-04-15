from abc import ABC, abstractmethod, abstractproperty
from typing import List
from datetime import date

class Person:
    def __init__(self, name: str, birthdate: date):
        self.name = name
        self.birthdate = birthdate
        self.phone
    @abstractproperty
    def name(self):
        return self._name
    
    @abstractproperty
    def age(self):
        pass

    
    
