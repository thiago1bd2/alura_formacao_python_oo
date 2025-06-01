import os

restaurantes = [{'nome': 'Churrasco', 'categoria': 'brasileiro', 'ativo': False},
                {'nome': 'Pizza', 'categoria': 'pizzaria', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'italiana', 'ativo': False}
                ]

# misc


def exibir_nome_programa():
    """Mostrar logo."""
    print("""
    ▀█▀ █▀▀ █░░ ▄▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
    ░█░ ██▄ █▄▄ █▀█   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
    """
          )


def exibir_menu() -> None:
    """Exibir opções do menu"""
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar/Desativar restaurantes')
    print('4. Sair\n')


def exibir_subtitutlo(texto: str) -> None:
    linha = '=' * len(texto)
    print(linha)
    print(texto)
    print(linha)


def escolher_opcao() -> None:
    """Trata a opção do menu escolhida."""
    try:
        opcao_escolhida = int(input('Entre com uma opcao:'))
        print(f'Opcao escolhida foi {opcao_escolhida}')  # interpolacao
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_status_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def finalizar_app() -> None:
    limpar_tela()
    print('encerrando...')


def opcao_invalida() -> None:
    print('Opcao invalida...!')
    voltar_menu()


def limpar_tela() -> None:
    _ = os.system(command='clear')


def voltar_menu():
    _ = input('pressione qualquer tecla para retornar ao menu...')
    main()

# funcoes principais


def cadastrar_novo_restaurante() -> None:
    '''Essa funcao cadastra novo restaurante
    Inputs:
    - Nome
    - Categoria

    Outputs:
    - Adiciona novo restaurante
    '''
    limpar_tela()

    exibir_subtitutlo('Cadstrar Novo Restaurante')

    nome_restaurante = input('Entre com o nome do restaurante: ')
    categoria = input(
        f'Digite a categoria do restaurante {nome_restaurante}: ')
    restaurante = {'nome': nome_restaurante,
                   'categoria': categoria, 'ativo': False}

    restaurantes.append(restaurante)

    print(f'O restaurante {nome_restaurante} foi cadastrado!')
    voltar_menu()


def listar_restaurantes():
    limpar_tela()

    exibir_subtitutlo('Lista de Restaurantes')

    print(
        f'|{'NOME RESTAURANTE'.ljust(20)}|{'CATEGORIA'.ljust(20)}|{'STATUS'.ljust(20)}')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']        
        categoria = restaurante['categoria']
        ativo = 'sim' if restaurante['ativo'] else 'nao'
        print(
            f'|{nome_restaurante.ljust(20)}|{categoria.ljust(20)}|{ativo.ljust(20)}|')
    voltar_menu()


def alternar_status_restaurante():
    exibir_subtitutlo('Alternar Status Restaurante')
    nome_restaurante = input('Digite qual restaurante alteranar estado:')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} esta agora ativo:{'sim' if restaurante['ativo'] == True else 'nao'}'
            print(mensagem)

    if not restaurante_encontrado:
        print(f'Restaurante nao encontrado!')

    voltar_menu()


def main():
    limpar_tela()
    exibir_nome_programa()
    exibir_menu()
    escolher_opcao()


if __name__ == '__main__':
    main()
