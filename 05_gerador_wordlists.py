import itertools


## objeto 'resultado' recebe da itertools o método chamado permutations
## .permutations('caracteres', qtd. de permutações)
#resultado = itertools.permutations('abcdef', 6)

string = input("String a ser permutada: ")
## o permutations pega a string do unput e o tamanho da string (len)
resultado = itertools.permutations(string, len(string))


for i in resultado:
    ## cada caracteres da permutação é unido
    print(''.join(i))