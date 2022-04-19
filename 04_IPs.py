## Com o ipaddress é possivel fazer calculo de ip ou imprimir rede 
## O Threads e o ipaddress podemos montar um Buffer overflow

import ipaddress


## Trabalhando com IPs
'''
ip = '192.168.0.1'

endereco = ipaddress.ip_address(ip)

print(endereco + 2000)

'''


## Trabalhando com redes

ip = '192.168.0.0/32'

#rede = ipaddress.ip_network(ip)

## Assim ele aceita qualquer endereço mesmo que não seja de uma rede verdadeira
rede = ipaddress.ip_network(ip, strict=False)

for ip in rede:
    print(ip)
