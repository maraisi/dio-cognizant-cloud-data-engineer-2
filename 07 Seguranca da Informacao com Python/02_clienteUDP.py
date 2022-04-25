import socket

## Criamos o objeto de conexão (s)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) ## O UDP é o protocolo de datagrama do usuário. IPV4 e UDP

print("Cliente socket criado com sucesso!!!")

host = 'localhost'
porta = 5433

mensagem = "E ai servidor? Beleza?"

try:
    print('Cliente: ' + mensagem)
    ## A mensagem é empacotada (encode) e enviada para o host na porta 5432 
    s.sendto(mensagem.encode(), (host, 5432))

    ## Aqui são criados dois objetos/variáveis que receberam uma resposta de 4096 bytes do servidor
    dados, servidor = s.recvfrom(4096) ## O object connect recebe do servidor uma resposta de 4096 bytes
    dados = dados.decode()  ## Os dados recebidos são desempacotados
    print("Cliente: " +  dados)

finally:
    print('Cliente: Fechando a Conexão')
    s.close()

## Etapas: Sincronização, Reconhecimento e Finalização da Conexão.
## Conhecido também como Three-way Handshake