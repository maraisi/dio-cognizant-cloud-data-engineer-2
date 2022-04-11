import shutil

def escrever_arquivo(texto):
    diretorio = '/home/maraisi/Documentos/teste.txt'
    arquivo = open(diretorio, 'w')
    #arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        #print(aluno)
        #print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        #print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media


def copia_arquivo(nome_arquivo):
    #import shutil
    #copiar arquivo para outro diretório
    shutil.copy(nome_arquivo, '/home/maraisi/')
    #copiar o arquivo com outro nome
    shutil.copy(nome_arquivo, 'notas_alunos_(NOVO_NOME).txt')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, '/home/maraisi/Downloads/')

if __name__ == '__main__':
    lista_media = media_notas('notas.txt')
    print(lista_media)
    copia_arquivo('notas.txt')
    move_arquivo('notas.txt')
    #aluno = 'Rafael: 10, 10, 5, 5'
    #atualizar_arquivo('notas.txt', aluno)
    #atualizar_arquivo('Quarta linha.\n')
    #ler_arquivo('teste.txt')