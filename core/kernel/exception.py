import attr

@attr.s(auto_attribs=True)
class UseCaseException(Exception):
    """ Base UseCase Error """
    message: str = None
