import random, string
from secrets import choice
from unicodedata import digit

## para gerar senhas com 16 digitos
#tamanho = 16

tamanho = int(input("Digite o tamanho de senha que você deseja: "))


## ascii_letter vai envolver a criação de letra maiúsculas e minúsculas
## caso queira somente letras maiúsculas usar ascii_uppercase
## para letras minúsculas usar ascii_lowercase

#chars = string.ascii_letters + string.digits + '!@#$%&*()-=+,.;:/?'

letras = input("Digite se você quer que a senha tenha letras maiúsculas(M), minúsculas(m) ou ambas(l): ")
while (letras != 'M') or (letras != 'm') or (letras != 'l'):
    if (letras == 'M') or (letras == 'm') or (letras == 'l'):
        break
    else:    
        letras = input("Digite se você quer que a senha tenha letras maiúsculas(M), minúsculas(m) ou ambas(l): ")
    

digitos = input("Digite se você quer que a senha tenha digitos númericos (S/N)): ")

while (digitos != 'S') or (digitos != 's') or (digitos != 'N') or (digitos != 'n'):
    if (digitos == 'S') or (digitos == 's') or (digitos == 'N') or (digitos == 'n'):
        if digitos == 'S' or digitos =='s':
            digitos = True
        else:
            digitos = False
        break
    digitos = input("Digite se você quer que a senha tenha digitos númericos (S/N)): ")
    
    

caracteres = input("Digite se você quer que a senha tenha caracteres '!@#$%&*()-=+,.;:/?' (S/N)): ")
while (caracteres != 'S') or (caracteres != 's') or (caracteres != 'N') or (caracteres != 'n'):
    if (caracteres == 'S') or (caracteres == 's') or (caracteres == 'N') or (caracteres == 'n'):
        if caracteres == 'S' or caracteres =='s':
            caracteres = True
        else:
            caracteres = False
        break
    caracteres = input("Digite se você quer que a senha tenha caracteres '!@#$%&*()-=+,.;:/?' (S/N)): ")
    
    

rnd = random.SystemRandom() ## SystemRandom puxa da biblioteca OS a classe urandom (os.urandom)


if letras == 'M' and digitos == True and caracteres == True:
    chars = string.ascii_uppercase + string.digits + '!@#$%&*()-=+,.;:/?'

elif letras == 'm' and digitos == True and caracteres == True:
    chars = string.ascii_lowercase + string.digits + '!@#$%&*()-=+,.;:/?'

elif letras == 'l' and digitos == True and caracteres == True:
    chars = string.ascii_letters + string.digits + '!@#$%&*()-=+,.;:/?'




elif letras == 'M' and digitos == False and caracteres == True:
    chars = string.ascii_uppercase + '!@#$%&*()-=+,.;:/?'

elif letras == 'm' and digitos == False and caracteres == True:
    chars = string.ascii_lowercase + '!@#$%&*()-=+,.;:/?'

elif letras == 'l' and digitos == False and caracteres == True:
    chars = string.ascii_letters + '!@#$%&*()-=+,.;:/?'




elif (letras == 'M') and (digitos == True) and (caracteres == False):
    chars = string.ascii_uppercase + string.digits

elif letras == 'm' and digitos == True and caracteres == False:
    chars = string.ascii_lowercase + string.digits

elif letras == 'l' and digitos == True and caracteres == False:
    chars = string.ascii_letters + string.digits




elif letras == 'M' and digitos == False and caracteres == False:
    chars = string.ascii_uppercase

elif letras == 'm' and digitos == False and caracteres == False:
    chars = string.ascii_lowercase

elif letras == 'l' and digitos == False and caracteres == False:
#else:
    chars = string.ascii_letters



print(''.join(rnd.choice(chars) for i in range(tamanho)))