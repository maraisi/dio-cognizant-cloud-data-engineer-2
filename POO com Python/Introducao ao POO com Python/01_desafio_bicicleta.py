class Bicicleta:
    #atributos
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro

    #métodos

    def buzinar(self):
        print('Plim plim...')
    
    def parar(self):
        print('Parando bicicleta...')
        print('Bicicleta parada')

    def correr(self):
        print('Vrummmmm....')

    #def __str__(self):
    #    return f'Bicicleta: cor = {self.cor}, modelo ={self.modelo}, ano = {self.ano}, valor = {self.valor}'

    #representação de classe
    def __str__(self):
        return f"{self.__class__.__name__}:{', '.join
([f'{chave}={valor}' for chave, valor in self.__ditc__.items()])}"


# instanciando uma Bicicleta 
caloi = Bicicleta('vermleha', 'calor', 2022, 1000)

caloi.buzinar() # essa chamada é equivalente a Bicicleta.buzinar(caloi)
caloi.correr()
caloi.parar()

print(caloi.cor, caloi.ano, caloi.modelo)