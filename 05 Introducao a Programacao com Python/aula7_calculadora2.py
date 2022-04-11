
#para não precisar instanciar a calculadora com os valores
class Calculadora2:
    def __init__(self):
        pass

    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b


    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        return a / b

if __name__== '__main__':
    calculadora = Calculadora2()

    print(calculadora.soma(10, 5))
    print(calculadora.subtracao(4, 2))
    print(calculadora.multiplicacao(5, 7))
    print(calculadora.divisao(10, 5))
