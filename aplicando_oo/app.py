from modelo.restaurante import Restaurante

restaurante_praca = Restaurante('praca','Gourmet')
restaurante_pizza = Restaurante('pizza','Italiana')
restaurante_local = Restaurante('Local', 'Caseira')

restaurante_praca.adicionar_avaliacao('Amelia',10)
restaurante_praca.adicionar_avaliacao('Laura',8)
restaurante_praca.adicionar_avaliacao('Thiago',5)
restaurante_praca.adicionar_avaliacao('Thiago',-15)
restaurante_praca.adicionar_avaliacao('Thiago',0)
restaurante_praca.adicionar_avaliacao('Thiago',12)

def main():
    pass


# restaurantes = [restaurante_praca, restaurante_pizza]

# print(restaurantes)

# dir - lista todos metodos e attr da classe
# vars - dic dos atributos

restaurante_praca.alternar_estado()
Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()