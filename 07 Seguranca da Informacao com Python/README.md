# Python Security


<h3>O que é DADO?</h3>

<br>

<p align="center">O <b>Dado</b> pode se uma representação simbólica, numérica ou textual qualquer. O *Dado* em si não possui referência e nenhuma característica de entendimento, sendo somente uma representação. Ex:</p>

<pre align="center">
<b>25</b> &mdash; o número é uma representação simbólica numérica.  
<b>Python</b> &mdash; o texto é uma representação simbólica textual.  
<b>@</b> &mdash; é uma representação simbólica.
</pre>

 
<br>

<h3>O que é INFORMAÇÃO?</h3>

<br>

<p align="center"><b>INFORMAÇÃO</b> é o <u>conjunto</u> ou a <u>junção</u> de dados que fazem um contexto ou sentido. Exemplo:</p>

<pre align="center">
<b>João tem 25 anos</b>  
<b>Python é uma linguagem de programação</b>  
<b>O email de João é joao_25@python.com</b>
</pre>

<br>

<h3> Segurança da Informação:</h3> 
<br>
<p align="center">Área que tem como objetivo assegurar que todos os dados de uma ou mais informações estejam sempre confidenciais, íntegros e disponíveis em qualquer meio de comunicação.</p>

<br><br><br>

# Princípios da Segurança da Informação

- **Confidencialidade**: principio que visa manter uma informação confidencial
  
- **Integridade**: princípio que visa proteger a informação de alterações indevidas
  
- **Disponibilidade**: princípio que visa garantir que um recurso e/ou informação esteja disponível
  
- Identificação: princípio que visa identificar uma entidade
  
- Autenticação: princípio que visa que visa verificar a entidade e suas credenciais
  
- Autorização: princípio que visa autorizar a entidade dentro de um sistema
  
- Não Repúdio: princípio que visa evitar que uma entidade negue suas ações em um sitema

<br><br>

## ICMP

<p align="center">O ICMP (Internet Control Message Protocol) é um protocolo integrante do Protocolo IP utilizado para fornecer relatórios de erros à fonte original.</p>

<br><br>

## PING

<p align="center">O PING é uma ferramenta que usa o protocolo ICMP para testar a conectividade entre nós. É um comando que consiste no envio de pacotes para o equipamento de destino e na "escuta" das respostas. <i>(Contempla o princípio da DISPONIBILIDADE)</i></p>

<br>
<pre align="center">ping -n 6 www.google.com</pre>

<br><br>

## Biblioteca OS

<p align="center"> Fornece de maneira simples o acesso de funcionalidades que são dependentes do sistema operacional.</p>


<br><br>

## Biblioteca Socket

<p align="center"> Fornece acesso de baixo nível à interface de rede. O sistema operacional fornece a API socket que relaciona o programa com a rede. </p>



<br><br>

## Protocolo TCP

<p align="center"> O TCP(Transmission Control Protocol) ou Protocolo de Controle de Transmissão é um dos protocolos de comunicação, que dão suporte a rede global Internet, verificando se os dados são enviados na sequência correta e sem erros. </p>

<p align="center"><i>(Contempla o princípio da INTEGRIDADE)</i></p>

<br><br>

## Protocolo UDP

<p align="center"> O UDP(User Datagram Protocol) ou Protocolo de Datagrama de Usuário é um protocolo simples da camada de transporte que permite que a aplicação envie um datagrama dentro num pacote IPv4 ou IPv6 a um destino, porém sem qualquer tipo de garantia que o pacote chegue corretamente.</p>

<p align="center"><i>(Contempla o princípio da DISPONIBILIDADE)</i></p>

<br><br>


## Biblioteca Random

<p align="center"> Implementa geradores de números pseudoaleatóprios para vária distribuições.
Será utilizada no gerador de senhas para randomizar letras e números e a cada execução do programa gerar uma nova senha aleatória.</p>

<p align="center"><i>(Contempla os princípios da AUTENTICAÇÃO e da CONFIDENCIALIDADE)</i></p>

<br><br>

## Hash

<p align="center">Identificador único gerado atravpes de um algoritmo que vai analisar byte a byte de determinado dados para gerar de forma única, um determinado código que só aquele arquivo terá. Se neste mesmo arquivos um único bit for alterado o hash gerado será diferente.</p> 

[Hash MD5](https://md5decrypt.net/en)

<br><br>


## Biblioteca Hashlib

<p align="center"> Implementa uma interface comum para muitos algoritimos de hash seguro com SHA1, SHA256, MD5 entre outros.</p>

<br><br>

## Multithreading

<p align="center"> Thread é o processo e no ambiente multithread, cada processo pode responder a várias solicitações concorrentemente ou mesmo simultaneamente.</p>

<br><br>

## Biblioteca Threading

<p align="center"> Constrói interfaces de alto nível para processamento usando o módulo Thread, de mais baixo nível, ou seja, relação direta com o processador.</p>

<br><br>

## Biblioteca Ipaddress

<p align="center"> Tem capacidade criar, manipular endereços IP do tipo IPv4, IPv6 e até redes inteiras.</p>

<br><br>


## Wordlists

<p align="center"> Sâo arquivos contendo uma palavra por linha. São utilizados em ataques de força bruta, como quebra de autenticação (ataque de dicionário). Pode ser usada para testar a autenticação e confidencialidade de um sistema.</p>

<br><br>

## Biblioteca Itertools

<p align="center"> Fornece condições para iterações como permutação e combinação. Pode ser usada para gerar uma lista com vários caracteres diferentes e sem repetições de palavras.</p>

<br><br>

## Web Scraping

<p align="center"> Um web scraper é uma ferramenta de coleta de dados web, uma forma de mineração que permite a extração de dados de sites da web convertendo-os em informações estruturadas para posterior análise.</p>

<br><br>

## Biblioteca BeatifulSoup

<p align="center"> Biblioteca de extração de dados de arquivos HTML e XML.</p>

<br><br>

## Biblioteca Requests

<p align="center"> Permite o envio de solicitações HTTP em Pyhton.</p>

<br><br>