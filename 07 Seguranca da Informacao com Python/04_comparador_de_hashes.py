import hashlib

arquivo1 =  'a.txt'
arquivo2 =  'b.txt'

## decide qual o algoritimo de hash sera usado.
## Aqui é usado o ripemd160 bits
hash1 = hashlib.new('ripemd160')

## Agora vamos dizer qual arquivos/informação sera passado para comparação
## https://docs.python.org/3/library/functions.html#open
## 'rb' abertura do arquivo em modo binário
hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')

hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'O arquivo: {arquivo1} é diferente do {arquivo2}')
    
else:
    print(f'O arquivo: {arquivo1} é igual ao {arquivo2}')
    print('O hash do arquivo a.txt é: ', hash1.hexdigest())
    print('O hash do arquivo b.txt é: ', hash2.hexdigest())