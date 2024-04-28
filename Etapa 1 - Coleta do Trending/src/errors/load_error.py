class LoadError(Exception):
    '''Erro para caso de falha na etapa de carregamento (load)'''
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.error_type = 'LoadError'
