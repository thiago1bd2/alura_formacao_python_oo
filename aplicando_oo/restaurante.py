class Restaurante:
    restaurantes :list = []

    def __init__(self, nome :str, categoria :str) -> None:
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self) -> str:
        return f'Nome: {self.nome} | Categoria: {self.categoria} | Ativo: {
            'sim' if self.ativo else 'não'}'
    
    def listar_restaurantes():
        for r in Restaurante.restaurantes:
            print(f'{r.nome}|{r.categoria}|{r.ativo}')

    @property
    def ativo(self):
        return 'ativo' if self.ativo else 'desativado'
            


restaurante_praca = Restaurante('Praca','Gourmet')

restaurante_pizza = Restaurante('Pizza','Italiana')

restaurantes = [restaurante_praca, restaurante_pizza]

# print(restaurantes)

# dir - lista todos metodos e attr da classe
# vars - dic dos atributos

Restaurante.listar_restaurantes()