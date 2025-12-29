class Artista:
    def __init__(self, nome) -> None:
        self._nome = nome

    def __str__(self) -> str:
        return f'Artista: {self._nome}'

class Musica:
    lista_musicas = []

    def __init__(self,nome: str, artista: Artista, duracao: int) -> None:
        self._nome = nome
        self._artista = artista
        self.duracao = duracao
        self.lista_musicas.append(self)

    def __str__(self) -> str:
        return f'{self._artista} - Musica: {self._nome} - duracao: {self.duracao}'

artista_1 = Artista("Agaki Band")
musica_1 = Musica("Akatsuki no Ito", artista=artista_1, duracao=5)

print(musica_1)

