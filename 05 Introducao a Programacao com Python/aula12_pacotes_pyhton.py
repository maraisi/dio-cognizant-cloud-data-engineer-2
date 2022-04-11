# https://docs.python-requests.org/en/latest/

from urllib import response
import requests

def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/' .format(cep))
    print('Status da resposta HTTP: {}\n' .format(response.status_code))
    print('Texto: {}\n' .format(response.text))

    print('Formato do \'response.text\': {}\n' .format(type(response.text)))

    print('Json: {}\n' .format(response.json()))

    print('Formato do \'response.json\': {}\n' .format(type(response.json)))
    # Esta no formato de dicionário. Então é possível usar os recursos de dicionário

    dados_cep = response.json()
    print(dados_cep['logradouro'])
    return dados_cep


def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/' .format(pokemon))
    print('Status da resposta HTTP: {}\n' .format(response.status_code))
    dados_pokemon = response.json()
    print(dados_pokemon['name'])
    print(dados_pokemon['sprites']['front_shiny'])
    #print(dados_pokemon['abilities'])
    return dados_pokemon


def retorna_response(url):
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    #retorna_dados_cep(31330110)
    #retorna_dados_pokemon('pikachu')

    codigo_font = retorna_response('https://google.com/')
    print(codigo_font)