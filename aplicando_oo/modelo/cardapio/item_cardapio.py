class ItemCardapio:

    def __init__(self, nome, preco) -> None:
        self._nome = nome
        self._preco = preco

    def __str__(self) -> str:
        return f'Item:{self._nome}|Preco:{self._preco}'