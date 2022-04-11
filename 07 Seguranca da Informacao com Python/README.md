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

<p>O ICMP (Internet Control Message Protocol) é um protocolo integrante do Protocolo IP utilizado para fornecer relatórios de erros à fonte original.</p>

<br><br>

## PING

<p>O PING é uma ferramenta que usa o protocolo ICMP para testar a conectividade entre nós. É um comando que consiste no envio de pacotes para o equipamento de destino e na "escuta" das respostas. <i>(Contempla o princípio da DISPONIBILIDADE)</i></p>

<br>
<pre align="center">ping -n 6 www.google.com</pre>
