## criar um ping que faça a requisição de vários hosts

import os
import time

with open('host.txt') as file:
    dump = file.read()
    dump = dump.splitlines()
    
    for ip in dump:
        print('\n'+ '#' * 60)
        print('Verificando o ip: ', ip)
        print('-' * 60)
        os.system('ping -c 2 {}' .format(ip))
        #print('-' * 60)
        time.sleep(5)