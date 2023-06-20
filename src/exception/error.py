from src.kernel.error import UseCaseBaseException

class ValidationError(UseCaseBaseException):
    
    """ Validation Error """
    def __init__(self, cause: str) -> None:
        super().__init__(message=f'Invalid request by. {cause}')


class UnexpectedError(UseCaseBaseException):
    
    """ Unexpected Error """
    def __init__(self, state: str) -> None:
        super().__init__(message=f'Unexpected Error ocurred: {state} Contac with Admin')