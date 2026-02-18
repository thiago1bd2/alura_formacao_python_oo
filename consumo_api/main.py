from fastapi import FastAPI, Query
import requests
import json

app = FastAPI()

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

@app.get('/api/hello')
def hello_world():
    """Rertona mensagem se server esta executando.

    Returns:
        str: mensagem
    """
    return {'Hello World!'}

@app.get('/api/restaurantes')
def get_restaurantes(restaurante: str = Query(None)):
    """Obter restaurantes, todos se param é None

    Args:
        restaurante (str, optional): nome do restaurante. Defaults to Query(None).

    Returns:
        JSON: Restaurante e seus itens.
    """

    if response.status_code == 200:
        #transforma para json o response content
        dados_json = response.json()
        dados_restaurantes = []

        if restaurante is None:
            return dados_json
        
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurantes.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
        
        return {'Restaurante': restaurante, 'Cardapio': dados_restaurantes}
    else:
        return {'Error':f'{response.status_code} - {response.text}'}