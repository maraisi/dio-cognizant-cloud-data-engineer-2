conjunto = {1, 2, 3, 4}

conjunto.add(5)
#conjunto.discard(2)
print(conjunto)

conjunto2 = {5, 6, 7, 8, 9}

'''
# união entre conjuntos
conjunto_uniao = conjunto.union(conjunto2)
print('União: {}' .format(conjunto_uniao))

# interseção entre conjuntos
conjunto_intersecao = conjunto.intersection(conjunto2)
print('Interseccão: {}' .format(conjunto_intersecao))

# diferença entre conjuntos
conjunto_diferenca = conjunto.difference(conjunto2)
print('Diferença entre 1 e 2: {}' .format(conjunto_diferenca))

conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença entre 2 e 1: {}' .format(conjunto_diferenca2))

conjunto = {5, 6, 7, 9}
conjunto2 = {4, 6, 8, 9}
conjunto_diferenca_sime = conjunto2.symmetric_difference(conjunto)
print('Diferença simétrica: {}' .format(conjunto_diferenca_sime))
'''

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}

conjunto_subset = conjunto_a.issubset(conjunto_b)
print('O conjunto A é subconjunto de B? {}' .format(conjunto_subset))

conjunto_subset2 = conjunto_b.issubset(conjunto_a)
print('O conjunto B é subconjunto de A? {}' .format(conjunto_subset2))


conjunto_superset = conjunto_a.issuperset(conjunto_b)
print('O conjunto A contém o conjunto B? {}' .format(conjunto_superset))

conjunto_superset2 = conjunto_b.issuperset(conjunto_a)
print('O conjunto B contém o conjunto A? {}' .format(conjunto_superset2))


lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print(lista)

# a função set converte para conjunto
# conjuntos não possuem duplicidade de elementos, isso vai permitir a limpeza da lista
conjunto_animais = set(lista)
print(conjunto_animais)

lista_limpa = list(conjunto_animais)
print(lista_limpa)