from bs4 import BeautifulSoup

import requests

## o objeto site recebe o conteúdo da requisição http (request.get) do site 
# o .content pega TODO o conteúdo 
site = requests.get("https://www.climatempo.com.br/").content


## o objeto soup baixa do site o html do site
soup = BeautifulSoup(site, 'html.parser')

## o prettify transforma o html em string 
## para o print exibir
#print(soup.prettify)

#temperatura = soup.find('p class="-gray _flex _align-center"')
#print(temperatura.string)

print('\n')
print(soup.title)
print(soup.title.string)


print('\n')
print(soup.p)
print(soup.p.string)

print('\n')
print(soup.find('admin'))
