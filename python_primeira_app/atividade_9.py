numero = int(input("Entre com um numero:"))
if numero % 2 == 0:
    print(f'#{numero} eh par')
else:
    print(f'#{numero} eh impar')

idade = int(input("qual sua idade:"))
if 0 <= idade <= 12:
    print(f'Idade #{idade} -> CRIANCA')
elif 13 <= idade <= 18:
    print(f'Idade #{idade} -> ADOLESCENTE')
else:
    print(f'Idade #{idade} -> ADULTO')

print('\n')
usuario = input('Usuario:')
senha = input('Senha:')

if usuario == 'thiago1bd2' and senha == 'qwe123':
    print('Login permitido!')
else:
    print('Usuario e/ou senha invalido')

# coord_x = int(input('Qual a coordenada X:'))
# coord_y = int(input('Qual a coordenada y:'))

def qual_quadrante(coord_x, coord_y):
    if coord_x > 0 and coord_y > 0:
        print(f'[{coord_x}, {coord_y}] -> 1º Quadrante')
    elif coord_x < 0 and coord_y > 0:
        print(f'[{coord_x}, {coord_y}]  -> 2º Quadrante')
    elif coord_x < 0 and coord_y < 0:
        print(f'[{coord_x}, {coord_y}]  -> 3º Quadrante')
    elif coord_x > 0 and coord_y < 0:
        print(f'[{coord_x}, {coord_y}]  -> 4º Quadrante')
    else:
        print(f'[{coord_x}, {coord_y}]  -> No centro dos eixos!')
# 0, 0 - eixo
# 1, 1 - 1
# -1, 1 - 2
# -1, -1 - 3
# 1, -1 - 4

qual_quadrante(0,0)
qual_quadrante(1,1)
qual_quadrante(-1,1)
qual_quadrante(-1,-1)
qual_quadrante(1,-1)
qual_quadrante(0,-1)
qual_quadrante(-1,0)

