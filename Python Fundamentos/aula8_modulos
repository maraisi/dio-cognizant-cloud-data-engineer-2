# módulos são os arquivos com extensão .py
# É possivel interagir com outros módulos de forma
# a acessar qualquer classe dos módulos ao realizar sua importação



# para acessar as classes de um modulo
import aula7_calculadora2

# para acessar somente uma classe de um modulo
from aula7_metodos_funcoes_classes import Calculadora
from aula7_televisao import Televisao

# para acessar somente uma ou mais funções de um modulo
from aula8_contador_letras import contador_letras , teste

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora(4, 5)
    print(calculadora.soma())

    calculadora = aula7_calculadora2.Calculadora2()
    print(calculadora.soma(6, 7))

    lista = ['cachorro', 'gato', 'elefante']
    print(contador_letras(lista))

    print(teste())