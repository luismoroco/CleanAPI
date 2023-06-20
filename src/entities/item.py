from src.kernel.entity import EntityBase
import dataclasses

@dataclasses.dataclass
class ItemEntity(EntityBase[int]):
    name: str
    price: float
    stock: int 

    """ Base Item Entity """
    def __init__(self, id: int, name: str, 
                 price: float, stock: int) -> None:
        
        self.id = id 
        self.name = name
        self.price = price
        self.stock = stock