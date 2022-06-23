import hashlib

'''
## o objeto 'resultado' recebe da hashlib um hash do tipo md5
## a string 'Python Security' é convertida em bytes(b' ') e transformada em hash.
resultado = hashlib.md5(b'Python Security')

print('O hash da string é: ', resultado.hexdigest())

'''
string = input('\nDigite o texto a ser gerado a hash: ')
hash_tipo = int(input('''\n ### ESCOLHA O TIPO DE HASH ###\n
    1) md5
    2) sha1 
    3) sha256 
    4) sha512\n
Digite o algoritimo hash a ser gerado: '''))

while (hash_tipo != 1) or (hash_tipo != 2) or (hash_tipo != 3) or (hash_tipo != 4):
    if (hash_tipo == 1) or (hash_tipo == 2) or (hash_tipo == 3) or (hash_tipo == 4):
        break
    hash_tipo = input('''\nDigitação incorreta. Escolha um dos algoritmos hash abaixo:\n
    1) md5
    2) sha1
    3) sha256
    4) sha512\n
Digite o número do hash que será gerado: ''')



if hash_tipo == 1: 
    resultado = hashlib.md5(string.encode('utf-8'))
    print('O hash MD5 da string \"', string, '\" é: ', resultado.hexdigest())

elif hash_tipo == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print('O hash SHA1 da string \"', string, '\" é: ', resultado.hexdigest())

elif hash_tipo == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print('O hash SHA256 da string \"', string, '\" é: ', resultado.hexdigest())
    
elif hash_tipo == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print('O hash SHA512 da string "', string, '" é: ', resultado.hexdigest())
else:
    print("Algo deu errado, tente novamente")

