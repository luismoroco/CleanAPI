import attr

from core.kernel.entity import Entity

@attr.s(auto_attribs=True)
class User(Entity):
    """ Base User Entity """
    name: str = None
    age: int = None
    isActive: bool = True
    password: str = None
    account: str = None