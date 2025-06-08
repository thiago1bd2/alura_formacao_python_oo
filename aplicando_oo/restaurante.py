class Restaurante:
    def __init__(self, nome :str, categoria :str) -> None:
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

restaurante_praca = Restaurante('Praca','Gourmet')

restaurante_pizza = Restaurante('Pizza','Italiana')

restaurantes = [restaurante_praca, restaurante_pizza]

print(restaurantes)

# dir - lista todos metodos e attr da classe
# vars - dic dos atributos
print(vars(restaurante_praca))