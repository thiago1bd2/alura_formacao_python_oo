from abc import ABC, abstractmethod

class Veiculo(ABC):

    def __init__(self, marca, modelo) -> None:
        self._marcam = marca
        self._modelo = modelo

    @abstractmethod
    def ligar():
        pass