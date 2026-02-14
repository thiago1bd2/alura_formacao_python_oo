from models.carro import Carro
from models.moto import Moto


def main():
    veiculos = []

    # Carros
    veiculos.append(Carro('Honda','Civic', 4))
    veiculos.append(Carro('Mitsubishi','Lances', 2))
    veiculos.append(Carro('Fiat','Mobi', 2))

    # Motos
    veiculos.append(Moto('Honda', 'Titan', 'Casual'))
    veiculos.append(Moto('Yamaha', 'XPTO', 'Esportiva'))
    veiculos.append(Moto('Kamikaze', 'CrossX', 'hibrida'))

    for veiculo in veiculos:
        print(veiculo)

if __name__ == '__main__':
    main()

