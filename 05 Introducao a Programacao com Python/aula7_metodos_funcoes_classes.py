# Por convenção, 'função' é todo algoritimo que retorna um valor
# ao contrário do 'método', que não retorna.

'''
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b
        
print(soma(1, 2))
print(soma(3, 4))
print(subtracao(3, 4))
print(multiplicacao(3, 4))
print(divisao(4, 2))

'''



class Calculadora:
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def soma(self):
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b


    def multiplicacao(self):
        return self.a * self.b

    def divisao(self):
        return self.a / self.b

# instanciar uma  classe
calculadora = Calculadora(10,5)

print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.multiplicacao())
print(calculadora.divisao())

