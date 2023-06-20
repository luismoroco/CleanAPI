import attr

@attr.s(auto_attribs=True)
class Entity(object):
    """ Integer ID Entity """
    id: int = None