## Verificador do IP externo (IP do computador na rede mundial)
## Caracteriza o endereço do computador e NÃO deve ser compartilhado por questões de segurança

import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

# a url é aberta (urlopen) e recebida no objeto 'resposta'
resposta = urlopen(url)

# todo o javascript que se encontra no objeto 'resposta' é carregado
# e recebido no objeto 'dados'
dados = json.load(resposta)

# objeto ip pega os dados da seção 'ip'
ip = dados['ip']

# objeto org pega os dados da seção 'org'
org = dados['org']

# objeto cidade pega os dados da seção 'city'
cidade = dados['city']

# objeto pais pega os dados da seção 'country'
pais = dados['country']

# objeto regiao pega os dados da seção 'region'
regiao = dados['region']

print('\n###### Detalhes do IP externo ######\n')
print('IP: {4}\nRegião: {1}\nCidade: {2}\nPaís: {3}\nOrganização: {0}\n' .format(org, regiao, cidade, pais, ip))
