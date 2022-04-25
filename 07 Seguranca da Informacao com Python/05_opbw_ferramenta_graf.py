import webbrowser
from tkinter import *

# o objeto root representa o tkinter
# dentro o Tk vai o screenName (nome da tela); o espaço vazio configura 'None',
# ou seja, não existe o nome da tela
root = Tk( )

# configura o título que ficará na borda da janela
root.title('Abrir Browser')

# configura o tamanho do sistema em pixels
root.geometry('300x200')


# a função abre o navegador no site espcificado
def google():
    webbrowser.open('www.google.com')


# o objeto mygoogle recebe um botão do tkinter com um texto 'Abrir o Google',
# cujo comando é a função google() e a posição (.pack(pady=20))
mygoogle = Button(root, text='Abrir o Google', command=google).pack(pady=20)

root.mainloop()