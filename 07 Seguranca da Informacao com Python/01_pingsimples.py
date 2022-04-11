## criar um ping que faça a requisição de um host escolhido

import os ## Importa o módulo ou biblioteca OS que integra os programas ou recursos do sistema operacional

print('#' * 60) ## imprime '#' 60 vezes. É uma personalização

## Cria uma variável que recebe o IP ou host que será verificado
ip_ou_host = input('Digite o IP ou host a ser verificado: ')

print('-' * 60)

## Chamando módulo system da biblioteca OS e utilizando o comando ping que pertence a biblioteca 
os.system('ping -c 6 {}' .format(ip_ou_host))

print('-' * 60)