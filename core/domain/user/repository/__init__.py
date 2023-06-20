from abc import ABC, abstractmethod
from typing import List

from core.domain.user.entity.user import User 

class UserRepository(ABC):
    
    @abstractmethod
    def getUser(self, key: int) -> User:
        return NotImplemented

    @abstractmethod
    def createUser(self, user: User) -> None:
        return NotImplemented
    
    @abstractmethod
    def getUsers(self) -> List[User]:
        return NotImplemented
    
    @abstractmethod
    def deleteUser(self, key: int) -> None:
        return NotImplemented
