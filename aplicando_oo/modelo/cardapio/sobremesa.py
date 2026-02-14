from .item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):

    def __init__(self, nome, preco, tipo, tamanho, descricao) -> None:
        super().__init__(nome, preco)
        self._tipo = tipo
        self._tamanho = tamanho
        self._descricao= descricao

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.3)

    def __str__(self) -> str:
        return f'super().__str__() | Tipo: {self._tipo} | Tamanho: {self._tamanho} | Desc.: {self._descricao}'