# https://docs.python.org/3/library/exceptions.html

""" 
# erro de divisao por zero:
divisao = 10 / 0

"""


lista = [1, 10]

# Tratamento de exceção
try:
    arquivo = open('teste.txt', 'r')
   
    #divisao = 10 / 0
    #numero = lista[3]
    x = a

    divisao = 10 / 1

except ZeroDivisionError:
    print('Não é possível realizar uma divisão por zero.')
except IndexError:
    print('Erro ao acessar um índice inválido da lista.')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}' .format(ex))

# O except possui hierarquia e funciona como uma árvore. Um exemplo é
# o BaseExeception que é o primeiro da hierarquia e se for colocado em 
# primeiro nas exceções, todo erro que ocorrer vai ser 'pego' por ele.
# A recomendação é colocar os exceptions filhos antes dos pais

else:
    print('O ELSE executa quando não ocorre uma exceção')

finally:
    print('Sempre executa')
    print('Fechando o arquivo')
    arquivo.close()

#Tudo que esta dentro do finally é executado independente da ocorrência de erro.
