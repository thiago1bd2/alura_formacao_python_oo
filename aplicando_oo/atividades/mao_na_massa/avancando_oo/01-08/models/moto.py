from .veiculo import Veiculo

class Moto(Veiculo):

    def __init__(self, marca, modelo, tipo) -> None:
        super().__init__(marca, modelo)
        self._tipo = tipo

    def __str__(self) -> str:
        return f'{super().__str__()}|Tipo:{self._tipo}'