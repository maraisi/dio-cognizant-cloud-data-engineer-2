# Objetivos da aula 4:
# Aprofundar nas sintaxes baśicas
# Aprender a utilizar laços de repetição
# Criar programas  com condicional e laços de repetição

# Comandos FOR, WHILE e RANGE

'''
for x in range(100):
    print(x)
    # printa os números de 0 a 99

for x in range(90, 100):
    print(x)
    # printa os números de 90 a 99
'''



'''
a = int(input('Entre com o número: '))

div = 0
for x in range(1, a+1):
    resto = a % x
    if resto == 0:
        div += 1

if div == 2:
    print('O número {} é primo.' .format(a))
else:
    print('O número {} não é primo.' .format(a))

'''


'''
a = int(input('Entre com um valor: '))
for num in range(a+1): 
    div = 0
    for x in range(1, num+1):
        resto = num % x
        if resto == 0:
            div += 1

    if div == 2:
        print(num)
   
'''


'''
a = 0
while a <= 10:
     print(a)
     a += 1
'''

a = int(input('Primeiro bimestre: '))
while a >10:
    a = int(input('Você digitou errado. Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
while b > 10:
    b = int(input('Você digitou errado. Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('Você digitou errado. Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
while d > 10:
    d = int(input('Você digitou errado. Quarto bimestre: '))
  
'''
if a <= 10 and b <= 10 and c <= 10 and  d<= 10: 
    print('Media: {}' .format(media))
else:
    print('Foi informado alguma nota errada')
''' 

media = (a + b + c + d) / 4
print('Media: {}' .format(media))