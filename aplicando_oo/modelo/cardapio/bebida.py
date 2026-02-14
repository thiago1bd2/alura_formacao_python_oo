from modelo.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):

    def __init__(self, nome, preco, tamanho) -> None:
        super().__init__(nome, preco)
        self._tamanho = tamanho

    def __str__(self) -> str:
        return f'{super().__str__()}|Tamanho: {self._tamanho}'