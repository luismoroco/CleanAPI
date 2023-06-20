import attr

from core.kernel.entity import Entity

@attr.s(auto_attribs=True)
class User(Entity):
    name: str 
    password: str

    """ Base User Entity """
    def __init__(self, id: int, name: str, password: str) -> None:
        self.id = id 
        self.name = name
        self.password = password 
     