# Lambda é uma função anônima, uma forma de simplicar
# uma função que será usada varias vezes.

# Ex: a função contador_letras possui 6 linhas de código

'''
def contador_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador
'''
# usando Lambda, a função contador_letras é igual:
contador_letras = lambda lista: [len(x) for x in lista]

# contador_letras é a função anônima que avalia o parametro lista 
# e retorna uma outra lista ([]) contendo a número de letras (len()) das 
# palavras dentro do parametro (for x in lista)

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b

print(soma(5,10))
print(subtracao(10,7))

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a*b,
    'divisao': lambda a, b: a/b
}


soma = calculadora['soma']
# isso é a mesma coisa de soma = lambda a, b: a + b

subtracao = calculadora['subtracao']

print('A soma é: {}'.format(soma(5, 6)))
print('A subtração é: {}'.format(subtracao(5, 6)))