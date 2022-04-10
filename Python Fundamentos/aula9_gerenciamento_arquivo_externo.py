'''
# para abrir ou criar um arquivo (open()) e poder escrever ('w')
arquivo = open('teste.txt', 'w')

# escrever no arquivo
arquivo.write('Minha primeira escrita.\n')

# fechar o arquivo
arquivo.close()


# Prestar atenção se o arquivo vai ser escrito ('w') ou atualizado ('a')
# Se o arquivo já tiver sido escrito e continuar com o 'w', ele será reescrito
arquivo = open('teste.txt', 'a')
arquivo.write('Segunda linha.\n')

'''


def escrever_arquivo(texto):
    #diretorio = '/home/maraisi/Documentos/teste.txt'
    #arquivo = open(diretorio, 'w')
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)



if __name__ == '__main__':
    escrever_arquivo('Primeira linha.\n')
    atualizar_arquivo('Segunda linha.\n')
    atualizar_arquivo('Terceira linha.\n')
    atualizar_arquivo('Quarta linha.\n')
    ler_arquivo('teste.txt')