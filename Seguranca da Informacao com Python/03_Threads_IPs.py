from threading import Thread
import time

'''
def carro1(velocidade):
    trajeto = 0
    while trajeto <= 100:
        print("Carro1: ", trajeto)
        trajeto += velocidade
        #time.sleep(2)


def carro2(velocidade):
    trajeto = 0
    while trajeto <= 100:
        print("Carro2: ", trajeto)
        trajeto += velocidade
        #time.sleep(2)

## da maneira abaixo o carro2 só executa a ação depois que o carro1 termina
#carro1(10)
#carro2(20)

'''
def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        #print("Carro: ", piloto, trajeto)
        trajeto += velocidade
        time.sleep(0.5)
        print('Piloto: {} Km: {} \n' .format(piloto, trajeto))

## Para que elas ocorram em paralelo, nos usamos o Threading
t_carro1 = Thread(target=carro, args=[1, 'Bruno'])
t_carro2 = Thread(target=carro, args=[1.5, 'Python'])

t_carro1.start()
t_carro2.start()