class Banco:

    def __init__(self, nome, endereco) -> None:
        self._nome = nome
        self._endereco = endereco

    def __str__(self) -> str:
        return f'{self._nome}|{self._endereco}'