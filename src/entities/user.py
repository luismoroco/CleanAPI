from src.kernel.entity import EntityBase
import dataclasses

@dataclasses.dataclass
class UserEntity(EntityBase[int]):
    name: str
    username: str 
    password: str 
    age: int 

    """ Base User Entity """
    def __init__(self, id: int, username: str, 
                 password: str, name: str, age: int) -> None:
      
      self.id = id 
      self.name = name
      self.username = username
      self.password = password
      self.age = age 