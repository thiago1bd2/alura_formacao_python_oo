class Restaurante:
    restaurantes :list = []

    def __init__(self, nome :str, categoria :str) -> None:
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
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
        print(f'{'Nome restaurante'.ljust(25)}|{'Categoria'.ljust(25)}|{'Status'.ljust(25)}')
        for r in cls.restaurantes:
            print(f'{r._nome.ljust(25)}|{r._categoria.ljust(25)}|{r._ativo}')

    @property
    def ativo(self):
        return 'ativo' if self._ativo else 'desativado'

    def alternar_estado(self):
        self._ativo = not self._ativo
            

restaurante_praca = Restaurante('praca','Gourmet')

restaurante_pizza = Restaurante('pizza','Italiana')

# restaurantes = [restaurante_praca, restaurante_pizza]

# print(restaurantes)

# dir - lista todos metodos e attr da classe
# vars - dic dos atributos

restaurante_praca.alternar_estado()
Restaurante.listar_restaurantes()
