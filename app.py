import os

restaurantes = ['Restaurante 1', 'Restaurante 2', 'Restaurante 3']

# misc


def exibir_nome_programa():
    """Mostrar logo."""
    print("""
    ▀█▀ █▀▀ █░░ ▄▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
    ░█░ ██▄ █▄▄ █▀█   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
    """
          )


def exibir_menu():
    """Exibir opções do menu"""
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurantes')
    print('4. Sair\n')


def escolher_opcao():
    """Trata a opção do menu escolhida."""
    try:
        opcao_escolhida = int(input('Entre com uma opcao:'))
        print(f'Opcao escolhida foi {opcao_escolhida}')  # interpolacao
        if opcao_escolhida == 1:
            print('=== Cadasrar restaurante ===')
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            print('=== Listar restaurante ===')
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('=== Ativar restaurante ===')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def finalizar_app():
    limpar_tela()
    print('encerrando...')


def opcao_invalida():
    print('Opcao invalida...!')
    voltar_menu()


def limpar_tela():
    os.system('clear')


def voltar_menu():
    input('pressione qualquer tecla para retornar ao menu...')
    main()

# funcoes principais


def cadastrar_novo_restaurante():
    limpar_tela()
    nome_restaurante = input('Entre com o nome do restaurante: ')
    restaurantes.append(nome_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado!')
    voltar_menu()


def listar_restaurantes():
    """Listar todos os restaurantes"""
    limpar_tela()
    for restaurante in restaurantes:
        print(f'Restaurante #: {restaurante}')
    voltar_menu()


def main():
    limpar_tela()
    exibir_nome_programa()
    exibir_menu()
    escolher_opcao()


if __name__ == '__main__':
    main()