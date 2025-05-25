import random
from functools import reduce

# ex 1
numeros = [
    1,2,3,4,5,6,7,8,9,10
]

nomes = [
    'Fulano', 'Beltrano', 'Cicrano', 'Cleyton'
]

anos = [
    1992, 2025
]

# ex 2
for i in range(len(numeros)):
    print(f'numero[{i}] : {numeros[i]}')

# ex 3
soma_impares = 0
for i in range(len(numeros)):
    if numeros[i] % 2 != 0:
        soma_impares += numeros[i]

print(f'Soma dos impares de 1 a 10 eh: {soma_impares}')

## range(start, stop, step)

# ex 4
tamanho_numeros = len(numeros)
for i in range(tamanho_numeros -1, -1, -1):
    print(f'Numero[{i}]:{numeros[i]}')

# ex 5
numero = 10 #int(input('Entre com numero:'))

if numero:
    print(f'Tabuada de 1 a 10 para {numero}')
    for i in range(1, 11, 1):
        print(f'{i} x {numero} = {numero * i}')

# ex 6
def arrayDeAleatorios(len):
    return [random.randint(1,999) for _ in range(len)]

# manual
total = 0
for n in arrayDeAleatorios(10):
    print(f'Total = {str(total).zfill(4)}, Numero = {str(n).zfill(4)} | Total depois de soma N: {str(total+n).zfill(4)}')
    total += n

print('')
# resolucao com reduce()
numeros = arrayDeAleatorios(10)
total = reduce(lambda x, y: print(f'Total = {x+y}, Numero = {y} | Total depois de soma N: {x+y}') or x + y, numeros, 0)

# resolucao map()
list(map(lambda x: print(f'Somando {str(x).zfill(4)}'), numeros))
print(f'Total da soma: {sum(numeros)}')

# ex 7
numeros = arrayDeAleatorios(9)
soma_valores = sum(numeros)

