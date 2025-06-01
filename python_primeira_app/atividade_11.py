# ex1

pessoas = [
    {'nome' : 'Fulano', 'idade' : 30, 'cidade' : 'Fortaleza'},
    {'nome' : 'Cicrano', 'idade' : 25, 'cidade' : 'Rio Claro'},
    {'nome' : 'Beltrano', 'idade' : 55, 'cidade' : 'Sao Carlos'}
]

print(pessoas)

# ex2
# 1
print(f'Pessoas[0]: {pessoas[0]}')
pessoas[0].update({'idade':31})
print(f'Pessoas[0]: {pessoas[0]}')

# 2
print(f'Pessoas[1]: {pessoas[1]}')
pessoas[1].__setitem__('profissao','QA')
print(f'Pessoas[1]: {pessoas[1]}')

# 3 - Sol. 1
print(f'Pessoas[2]: {pessoas[2]}')
pessoas[2].__delitem__('cidade')
print(f'Pessoas[2]: {pessoas[2]}')

# 3 - Sol. 2
print(f'Pessoas[2]: {pessoas[2]}')
del pessoas[2]['idade']
print(f'Pessoas[2]: {pessoas[2]}')

# 4

quadrados = { x: x**2 for x in range(1,5)}
print(quadrados)

# 5
for p in pessoas:
    if p.get('profissao'):
        print(f'A chave profissao existe para {p}')
    else:
        print(f'Chave nao encontrada para {p}')

# 6
frase = "profissao das cidade as vezes a cidade da profissao"
palavras = frase.split() # quebra em um array
contagem = {} # para adicionar cada elemendo do array quebrado + nro de ocorrencias
print(palavras)
for palavra in palavras:
    contagem[palavra] = contagem.get(palavra, 0) + 1
print(contagem)