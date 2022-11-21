# Python não possui interface, então o conceito de contrato
# é implementado através de "classe abstrata" atraves do módulo abc 

from abc import ABC, abstractclassmethod, abstractproperty

#class ControleRemoto:
#    def ligar(self):
#        pass
#
#    def desligar(self):
#        pass


##uma vez que a classe é abstrata, ela não pode ser instanciada diretamente
class ControleRemoto(ABC):
    ## método abstrato é um método que não tem um corpo
    ## mas todas as classes filhas são obrigadas a implementar
    @abstractclassmethod
    def ligar(self):
        pass

    @abstractclassmethod
    def desligar(self):
        pass

    # é possivel tambem obrigar uma propriedade
    @property
    @abstractproperty
    def marca(self):
        pass




class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a tv..")

    def desligar(self):
        print("Desligando a tv..")

    def marca(self):
        return "LG"



class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o ar condicionado..")
    
    def desligar(self):
        print("Desligando o ar condicionado..")
 

    def marca(self):
        return print("Philco")





controle = ControleTV()
controle.ligar()
controle.desligar()

ar_cond = ControleArCondicionado()
ar_cond.ligar()
ar_cond.marca()