from banco import Banco

class Agencia(Banco):

    def __init__(self, nome, endereco, numero, digito) -> None:
        super().__init__(nome, endereco)
        self._numero = numero
        self._digito = digito

    def __str__(self) -> str:
        return f'{super().__str__()}|{str(self._numero).zfill(4)}-{self._digito}'
        