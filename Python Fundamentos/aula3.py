'''
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))

if a > b:
    print('O maior número é {}' .format(a))
elif a == b:
    print('Os dois números são iguais.')    
else:
    print('O maior número é {}' .format(b))
print('Final do programa 1. \n')



a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a > b and a > c:
    print('O maior número é {}' .format(a))
elif b > a and b > c:
    print('O maior número é {}' .format(b))
elif a == b and b == c:
    print('Os três números são iguais.')    
else:
    print('O maior número é {}' .format(c))



a = int(input('Entre com o priemiro valor: '))
b = int(input('Entre com o segundo valor: '))

resto_a = a % 2
resto_b = b % 2

if resto_a == 0 or not resto_b > 0:
    print('O número é par')
else:
    print('Nenhum número par foi digitado')

'''



a = int(input('Primeiro bimestre: '))
if a > 10:
    a = int(input('Você digitou errado. Primeiro bimestre: '))
b = int(input('segundo bimestre: '))
if b > 10:
    b = int(input('Você digitou errado. Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
if c > 10:
    c = int(input('Você digitou errado. Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
if d > 10:
    d = int(input('Você digitou errado. Quarto bimestre: '))
  
'''
if a <= 10 and b <= 10 and c <= 10 and  d<= 10: 
    print('Media: {}' .format(media))
else:
    print('Foi informado alguma nota errada')
''' 

media = (a + b + c + d) / 4
print('Media: {}' .format(media))
