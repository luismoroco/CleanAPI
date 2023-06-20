from abc import ABC, abstractmethod
from typing import List

from core.domain.user.entity.user import User 

class UserRepository(ABC):
    
    @abstractmethod
    def getUser(self, key: int) -> User:
        pass

    @abstractmethod
    def createUser(self, user: User) -> None:
        pass
    
    @abstractmethod
    def getUsers(self) -> List[User]:
        pass
    
    @abstractmethod
    def deleteUser(self, key: int) -> None:
        pass
