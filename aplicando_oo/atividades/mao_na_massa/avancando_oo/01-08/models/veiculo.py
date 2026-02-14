class Veiculo:

    def __init__(self, marca, modelo) -> None:
        self._marca = marca
        self._modelo = modelo
        self._ligado = False

    def __str__(self) -> str:
        return f'[INFO]: {self._marca}|{self._modelo}|{'Ligado' if self._ligado else 'Desligado'}'