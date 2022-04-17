import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


print('Socket criado com sucesso')

host = 'localhost'
port = 5432

## O bind faz a ligação entre cliente/servidor atraves do host e da porta
s.bind((host, port))
mensagem = '\nServidor: Oláaaaaa Cliente e aí? Beleza?'


while 1:  ## while 'verdadeiro' -> o 1 faz o papel de TRUE
    dados, end = s.recvfrom(4096)

    if dados:
        print('Servidor enviando mensagem')
        s.sendto(dados + (mensagem.encode()), end) 

