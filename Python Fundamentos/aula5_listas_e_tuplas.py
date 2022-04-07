# Objetivos aula 5:
# Aprender sobre listas e tuplas

lista_inteiros = [1, 2, 3, 5, 7]
lista_animais = ['cachorro', 'gato', 'elefante']



'''
print(lista_animais[1])


soma = 0
for x in lista_inteiros:
    print(x)
    soma += x
print(soma)


#a soma tambem pode ser obtida usando print(sum(lista_inteiros))
print(sum(lista_inteiros))
# o maior valor da lista é obtido com max(lista)
print(max(lista_inteiros))
print(max(lista_animais)) #o valor da string é o valor da primeira letra dentro do alfabeto
# o menor valor da lista é obtido com min(lista)
print(min(lista_inteiros))
print(min(lista_animais))



if 'lobo' in lista_animais:
    print('existe um lobo na lista')
else:
    print('Não existe um lobo na lista')
    print(lista_animais)
    lista_animais.append('lobo')
    #append inclui um objeto na lista
    print(lista_animais)

nova_lista = lista_animais * 3
print(nova_lista)

# a função pop remove a ultima posição da lista
lista_animais.pop()
print(lista_animais)

# ou o valor especificado da posição
lista_animais.append('lobo')
print(lista_animais)
lista_animais.pop(1)
print(lista_animais)

# a função remove é usada para remover um valor conhecido
lista_animais.remove('cachorro')
print(lista_animais)

nova_lista = lista_animais * 3
print(nova_lista)

# a função sort é usada para ordernar a lista
nova_lista.sort()
print(nova_lista)
# a função reverse ordernar inversamente a lista
nova_lista.reverse()
print(nova_lista)


'''

# listas são mutáveis, ao contrario das tuplas que são imutáveis
# tuplas usam parenteses
tupla = (1, 10, 12, 14)
print(tupla)
#a função len retorna a quantidade de elementos de uma lista ou tupla
print(len(tupla))
print(len(lista_animais))

# tuple faz a conversão de uma lista para tupla
tupla_animais = tuple(lista_animais)
print(tupla_animais)
print(type(tupla_animais))

# list faz a conversão para uma lista
tupla_animais = list(tupla_animais)
print(tupla_animais)
print(type(tupla_animais))