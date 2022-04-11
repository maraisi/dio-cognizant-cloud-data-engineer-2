
# Para um input somente entre 0 e 10, nos criaremos uma classe de exceção. Entretanto, para criarmos 
# uma classe de erro personalizada (InputError) é obrigatório a criação de uma outra classe de erro (Error) 
# que herda diretamente da classe Exception. Mesmo que essa não faça nada (pass), é obrigatório sua criação.
# A classe de erro personalizada herdará, então, daquela classe.

class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message


#while True mantém a execução do loop enquanto o bloco interior manter o status:
while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        # Enquanto não digitar corretamento, o código não passa da parte do input e continua o loop.
        # Quando não ocorrer mais o exception, o loop passará pelo break e saira do loop.
        
        if x > 10:
            # o comando raise permite força uma exception de sua escolha
            # no contrutor da claase tem uma mensagem, sendo necessário passar uma mensagem como parâmetro
            raise InputError('A nota não pode ser maior que 10.')

        elif x < 0:
            raise InputError('A nota não pode ser menor que 0.')

        print(x)        
        break
    except ValueError:
        print('Valor inválido. Digite apenas números.')
    except InputError as ex:
        print(ex)






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
 """