class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    #criar um metodo de classe
    #onde eu preciso ter acesso ao contexto da classe
    @classmethod
    def criar_data_nascimento(cls, ano, mes, dia, nome):
        #print(cls)
        
        idade = 2022 - ano
        return cls(nome, idade)
   
    #criar metodo estatico    
    #onde eu NÃO preciso ter acesso ao contexto da classe e nem da instancia do objeto
    @staticmethod
    def maior_idade(idade):
        return idade >= 18

#p1 = Pessoa("Guilherme", 28)
#print(p1.nome, p1.idade)

p2 = Pessoa.criar_data_nascimento(1994, 3, 21, "Guilherme")
print(p2.nome, p2.idade)

print(Pessoa.maior_idade(16))
print(Pessoa.maior_idade(28))