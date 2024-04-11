class TransformError(Exception):
    '''Erro para caso de falha na etapa de extração'''
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.error_type = 'TransformError'