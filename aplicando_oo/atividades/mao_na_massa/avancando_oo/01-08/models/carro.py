from .veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, marca, modelo, n_portas) -> None:
        super().__init__(marca, modelo)
        self._n_portas = n_portas

    def __str__(self) -> str:
        return f'{super().__str__()}|N.Portas{self._n_portas}'