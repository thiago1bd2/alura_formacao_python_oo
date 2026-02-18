import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)

# print(response)

if response.status_code == 200:
    #transforma para json o response content
    dados_json = response.json()
    # print(dados_json)

    restaurantes = {}

    for restaurante in dados_json:
        nome_restaurante = restaurante['Company']
        if nome_restaurante not in restaurantes:
            restaurantes[nome_restaurante] = []

        restaurantes[nome_restaurante].append({
            "item": restaurante['Item'],
            "price": restaurante['price'],
            "description": restaurante['description']
        })

else:
    print(f'O erro foi {response.status_code}')


print(restaurantes["Pizza Hut"])

for nome_restaurante, dados in restaurantes.items():
    nome_do_arquivo = f'{nome_restaurante}.json'

    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)