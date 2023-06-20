from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

class EntityBase(ABC, Generic[T]):
    
    """ Abstract class for Entitys """
    id: T = None

    @abstractmethod
    def getIdentifier(self) -> T:
        return NotImplemented 

class Verify(ABC):

    @abstractmethod
    def verify(self) -> None: 
        return NotImplemented