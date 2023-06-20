from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Dict, Any
from .exception import UseCaseException

import attr

T = TypeVar('T')

@attr.s(auto_attribs=True)
class UseCaseRequest(ABC):
    """ Base UseCase Request """

@attr.s(auto_attribs=True)
class UseCaseResponse(object):
    result: Any = None
    error: UseCaseException = None

    @property
    def is_succeeded(self):
        return self.error is None or self.result is not None

class UseCaseOutputPort(Generic[T]):

    def __str__(self):
        return f'{__class__.__name__} with Type: {T}'

    @abstractmethod
    def handle(self, response: T) -> None:
        return NotImplemented