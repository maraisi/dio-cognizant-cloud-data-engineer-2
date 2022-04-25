import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter


# Essa primeira função startar na URL que sera analisada
def start(url):
    # o conteúdo do site é armazenado na lista vazia chamada wordlist
    wordlist = []
    source_code = requests.get(url).text

    # o soup faz a requisição dos dados que seram passados e os tranforma em HTML
    soup = BeautifulSoup(source_code, 'html.parser')

    # Text in given web-page is stored under
    # the <div> tags with class <entry-content>
    # nesse código todo o contúdo do soup que possuir div e class é transformado em string
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text

        # o conteúdo que foi tranformado em string, é transformado em letras
        # minusculas e separado em linhas
        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)


# a função clean_wordlist limpa qualquer simbolo indesejado da wordlist
def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%^&*()_-–+={]}[|\;:"<>?/.,'

        for i in range(0, len(symbols)):
            # caso seja encontrado alguma dos symbols, ele será removido através
            # do replace por nada ('')
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            # se word for maior que zero ele continua limpando a lista
            clean_list.append(word)
    create_dictionary(clean_list)


# nessa função é criado um dicionário contendo cada palavra para realização de uma contagem
def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # finalizado a contagem, é feita o top 20 das palavras mais utilizadas no site
    for key, value in sorted(word_count.items(), key = operator.itemgetter(1)):
        print("% s : % s " % (key, value))

    c = Counter(word_count)

    top = c.most_common(10)
    print(top)


if __name__ == '__main__':
    start('https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar')
   