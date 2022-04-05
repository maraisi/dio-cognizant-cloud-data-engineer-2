a = 10
b = 5
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(resto)

#print('soma: ' + soma)

print(type(soma)) # exibe o tipo da variável soma. Nesse caso: <class 'int'>
soma = str(soma) #converte a variável para o tipo string
print(type(soma))
print('soma: ' + soma)

# melhor maneira de printar concatenação de variável de tipos diferentes
print('subtração: {}' .format(subtracao))


# format com mais de uma variável e as variáveis dentro do format deveram estar na ordem correta
print('Subtração: {};  Multiplifcação: {}' .format(subtracao, multiplicacao))

# outra forma de realizar a mesma ação. Nesse caso a ordem das variáveis dentro do form não importa
print('Subtração: {subtr};  Multiplifcação: {multip}' .format(multip=multiplicacao, subtr=subtracao))

# usando newline aka \n
print('\nSubtração: {}'   
        '\nMultiplicação: {}'
        '\nDivisão: {}' 
        '\nResto: {}' .format(subtracao, multiplicacao, divisao, resto))


# Entrando com strings através do terminal. "input=()""
# Como vamos trabalhar com números é necessário converter as strings usando int().
a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

print(  '\nSoma: {}'
        '\nSubtração: {}'   
        '\nMultiplicação: {}'
        '\nDivisão: {}' 
        '\nResto: {}' .format(soma, subtracao, multiplicacao, divisao, resto))
