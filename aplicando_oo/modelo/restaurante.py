from modelo.avaliacao import Avalicao

class Restaurante:
    restaurantes :list = []

    def __init__(self, nome :str, categoria :str) -> None:
        """
        Inicializa um instancia de restaurante.
        
        :param self: Description
        :param nome: Description
        :type nome: str
        :param categoria: Description
        :type categoria: str
        """
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacoes = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self) -> str:
        return f'Nome: {self._nome} | Categoria: {self._categoria} | Ativo: {'sim' if self._ativo else 'não'} | Cardapio{self.ver_cardapio()}'
    
    @classmethod
    def listar_restaurantes(cls) -> None:
        '''
        Lista todos os restaurantes cadastrados
        
        :param cls: Description
        '''
        print(f'{'Nome restaurante'.ljust(25)}|{'Categoria'.ljust(25)}|{'Avaliacao'.ljust(25)}|{'Status'.ljust(25)}')
        for r in cls.restaurantes:
            print(f'{r._nome.ljust(25)}|{r._categoria.ljust(25)}|{str(r.media_avaliacoes).ljust(25)}|{r._ativo}')

    @property
    def ativo(self):
        return 'ativo' if self._ativo else 'desativado'

    def alternar_estado(self):
        self._ativo = not self._ativo
        
    def adicionar_avaliacao(self, cliente, nota) -> None:
        avaliacao = Avalicao(cliente, self.__validar_nota(nota))
        self._avaliacoes.append(avaliacao)

    def __validar_nota(self, value):
        if float(value) < 0:
            print(f'Nota foi negativa ({value}), assumindo 0')
            return 0
        elif float(value) > 5:
            print(f'Nota ({value}) foi maior que 5, assumindo 5')
            return 5
        else:
            return value
    
    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return '-'
        
        sum_notas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        total_avaliacoes = len(self._avaliacoes)

        return round((sum_notas / total_avaliacoes), 1)
    
    def add_bebida_cardapio(self, bebida):
        self._cardapio.append(bebida)

    def add_prato_cardapio(self, prato):
        self._cardapio.append(prato)

    def ver_cardapio(self):
        return [ item.__str__() for item in self._cardapio]
