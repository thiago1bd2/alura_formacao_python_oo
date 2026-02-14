from modelo.restaurante import Restaurante
from modelo.cardapio.bebida import Bebida
from modelo.cardapio.prato import Prato


def main():
    # Restaurante
    restaurante_praca = Restaurante('praca','Gourmet')

    # Avaliacao restaurante
    restaurante_praca.adicionar_avaliacao('Amelia',10)

    # Bebida
    bebida_cafe_grande = Bebida('Expresso', 5.0, 'grande')

    # Prato
    prato_pao_na_chapa_medio = Prato('Pao na chapa', 2.5, 'prensado na chapa com manteiga')

    restaurante_praca.add_bebida_cardapio(bebida_cafe_grande)
    restaurante_praca.add_prato_cardapio(prato_pao_na_chapa_medio)

    print(restaurante_praca)


# restaurantes = [restaurante_praca, restaurante_pizza]

# print(restaurantes)

# dir - lista todos metodos e attr da classe
# vars - dic dos atributos

# restaurante_praca.alternar_estado()
# Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()