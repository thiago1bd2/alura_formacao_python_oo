from modelo.avaliacao import Avalicao

class Restaurante:
    restaurantes :list = []

    def __init__(self, nome :str, categoria :str) -> None:
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)

    def __str__(self) -> str:
        return f'Nome: {self._nome} | Categoria: {self._categoria} | Ativo: {
            'sim' if self._ativo else 'não'}'
    
    @classmethod
    def listar_restaurantes(cls) -> None:
        '''
        Lista todos os restaurantes cadastrados
        
        :param cls: Description
        '''
        print(f'{'Nome restaurante'.ljust(25)}|{'Categoria'.ljust(25)}|{'Avaliacao'.ljust(25)}|{'Status'.ljust(25)}')
        for r in cls.restaurantes:
            print(f'{r._nome.ljust(25)}|{r._categoria.ljust(25)}|{str(r.media_avaliacoes()).ljust(25)}|{r._ativo}')

    @property
    def ativo(self):
        return 'ativo' if self._ativo else 'desativado'

    def alternar_estado(self):
        self._ativo = not self._ativo
        
    def adicionar_avaliacao(self, cliente, nota) -> None:
        avaliacao = Avalicao(cliente, nota)
        self._avaliacoes.append(avaliacao)

    def media_avaliacoes(self):
        if not self._avaliacoes:
            return 0
        
        sum_notas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        total_avaliacoes = len(self._avaliacoes)

        return round((sum_notas / total_avaliacoes), 1)
