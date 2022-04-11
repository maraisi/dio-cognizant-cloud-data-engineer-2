# ex identificação de padroes

arroz_kg = 7.00
feijão_kg = 9.00
carne_kg = 35.00

comida = ('Arroz', 'Feijão', 'Carne')

for i in range(3):
    valor = float(input('Entre com o preço do {}: ' . format(comida[i])))
    if valor <= 10.00:
        print('Posso comprar!')
    else:
            print('Não posso comprar!')
        