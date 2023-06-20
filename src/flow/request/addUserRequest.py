import dataclasses

from src.exception.error import ValidationError
from src.kernel.entity import Verify

@dataclasses.dataclass
class AddUserRequest(Verify):
    name: str
    username: str 
    password: str 
    age: int 

    def verify(self) -> None:
        if not self.name:
            raise ValidationError('There is not name')
        elif not self.username:
            raise ValidationError('There is not username')
        elif not self.password:
            raise ValidationError('There is not password')
        elif not self.age:
            raise ValidationError('There is not age')