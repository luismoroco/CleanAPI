
class UseCaseBaseException(Exception):

    """ Base UseCase Error """
    def __init__(self, message: str) -> None:
        self._message: str = message
        super().__init__(message)
