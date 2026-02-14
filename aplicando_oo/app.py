from modelo.restaurante import Restaurante
from modelo.cardapio.bebida import Bebida
from modelo.cardapio.prato import Prato

# Restaurante
restaurante_praca = Restaurante('praca','Gourmet')

# Avaliacao restaurante
restaurante_praca.adicionar_avaliacao('Amelia',10)

# Bebida
bebida_cafe_grande = Bebida('Expresso', 5.0, 'grande')

# Prato
prato_pao_na_chapa_medio = Prato('Pao na chapa', 2.5, 'prensado na chapa com manteiga')

def main():
    print(bebida_cafe_grande)
    print(prato_pao_na_chapa_medio)


# restaurantes = [restaurante_praca, restaurante_pizza]

# print(restaurantes)

# dir - lista todos metodos e attr da classe
# vars - dic dos atributos

# restaurante_praca.alternar_estado()
# Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()