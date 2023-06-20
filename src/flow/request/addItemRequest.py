import dataclasses

from src.exception.error import ValidationError
from src.kernel.entity import Verify

@dataclasses.dataclass
class AddItemRequest(Verify):
    name: str 
    price: float
    stock: int 

    def verify(self) -> None:
        if not self.name:
            raise ValidationError('There is not name')
        elif not self.price:
            raise ValidationError('There is not price') 
        elif not self.stock:
            raise ValidationError('There is not stock')