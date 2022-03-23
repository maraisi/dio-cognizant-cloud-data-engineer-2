# Linux: Introdução ao Sistema Operacional

<br/>

**CTRL+ALT+T** &emsp; &emsp; &emsp; &emsp; abre o terminal

**man** &emsp; &emsp; &emsp; &emsp; exibe o manual de um comando específico

**pwd** &emsp; &emsp; &emsp; &emsp; exibe o caminho do diretório/local atual

**ls** &emsp; &emsp; &emsp; &emsp; exibe a lista de arquivos e diretórios de uma pasta

**ls -l** &emsp; &emsp; &emsp; &emsp; exibe a lista, detalhes e privilégios de arquivos e diretórios de uma pasta

**cd** &emsp; &emsp; &emsp; &emsp; muda para um diretório específico

**cd ..** &emsp; &emsp; &emsp; &emsp; retorna para o diretório anterior ao diretório atual

**cd /** &emsp; &emsp; &emsp; &emsp; muda para um diretório raiz

**mkdir** &emsp; &emsp; &emsp; &emsp; cria um diretório

**mv** &emsp; &emsp; &emsp; &emsp; move um arquivo ou diretório. Pode ser usado para renomear

**touch** &emsp; &emsp; &emsp; &emsp; cria um arquivo vazio

**cp** &emsp; &emsp; &emsp; &emsp; copia um arquivo ou diretório

**rm** &emsp; &emsp; &emsp; &emsp; remove um arquivo ou diretório





 








<br/><br/><br/>
          
# Linux: Diretórios e Comandos Essenciais

<br/>











<br/><br/><br/>

# Linux: Fundamentos de Redes e Comandos Avançados

<br/>

**ifconfig** &emsp; &emsp; &emsp; &emsp; 

**hostname** &emsp; &emsp; &emsp; &emsp; 

**hostname -i** &emsp; &emsp; &emsp; &emsp; 

**hostname -I** &emsp; &emsp; &emsp; &emsp; 

**ping** &emsp; &emsp; &emsp; &emsp; 

**traceroute** &emsp; &emsp; &emsp; &emsp; 

**finger** &emsp; &emsp; &emsp; &emsp; 

**w** &emsp; &emsp; &emsp; &emsp; 

**whois** &emsp; &emsp; &emsp; &emsp; 

**history** &emsp; &emsp; &emsp; &emsp; mostra o histórico de ações do terminal

**history -c** &emsp; &emsp; &emsp; &emsp; limpa o histórico do terminal

**alias** &emsp; &emsp; &emsp; &emsp; especifica um determinado alias para um comando. &emsp; *Ex: alias hh=history*

**nl** &emsp; &emsp; &emsp; &emsp; exibe o arquivo e o número de linhas que ele contém. &emsp; *Ex: nl aularedes.txt*

**wc -l** &emsp; &emsp; &emsp; &emsp; exibe o número de linhas em um arquivo, incluindo as linhas em branco

**wc -w** &emsp; &emsp; &emsp; &emsp; exibe o número de palavras em um arquivo

**wc -c** &emsp; &emsp; &emsp; &emsp; exibe o número de bytes de um arquivo

**wc -m** &emsp; &emsp; &emsp; &emsp; exibe o número de caracteres em um arquivo

**ls -a** &emsp; &emsp; &emsp; &emsp; exibe todos os arquivos de um diretório, incluindo os ocultos

**ls -F** &emsp; &emsp; &emsp; &emsp; exibe os arquivos de um diretório com / no final

**cmp** &emsp; &emsp; &emsp; &emsp; compara dois arquivos byte por byte

**diff** &emsp; &emsp; &emsp; &emsp; compara dois arquivos linha por linha

**sort -n** &emsp; &emsp; &emsp; &emsp; organiza as linhas de um arquivo em ordem numerica, de acordo com o valor de string

**last reboot** &emsp; &emsp; &emsp; &emsp; exibe a informação de todas as reinicializações do sistema

**route -n** &emsp; &emsp; &emsp; &emsp; exibe as informações de Tabela de Roteamento IP do Kernel

**time** &emsp; &emsp; &emsp; &emsp; exibe o tempo de processo de um comando

**uptime** &emsp; &emsp; &emsp; &emsp; exibe a quanto tempo o sistema esta rodando

**cowsay** &emsp; &emsp; &emsp; &emsp; exibe uma string em um texto-imagem de uma vaca. &emsp; *Ex: cowsay "Linux é Bom"*

<pre>					 _____________
					< Linux é Bom >
					 -------------
					        \   ^__^
					         \  (oo)\_______
					            (__)\       )\/\
					                ||----w |
					                ||     ||

</pre>


<br/>

**cmatrix** &emsp; &emsp; &emsp; &emsp; exibe o efeito matrix no terminal

**init 0** &emsp; &emsp; &emsp; &emsp; desliga o sistema

**telinit 0** &emsp; &emsp; &emsp; &emsp; desliga o sistema

**halt** &emsp; &emsp; &emsp; &emsp; desliga o sistema através de autenticação

**seq** &emsp; &emsp; &emsp; &emsp; exibe uma sequencia de números no terminal. &emsp; *Ex: seq 1 10*

**shuf** &emsp; &emsp; &emsp; &emsp; exibe uma permutação aleatória.  &emsp; *Ex: shuf -i 0-80 -n5*

**whereis** &emsp; &emsp; &emsp; &emsp; exibe o caminho de um comando e seu manual

**which** &emsp; &emsp; &emsp; &emsp; exibe o caminho de um comando


<br/><br/><br/>



# Linux: Gerenciamento de Pacotes


### **Gerenciador APT** 

<br/>

**apt install** &emsp; &emsp; &emsp; &emsp; instala um pacote e as dependências

**apt update** &emsp; &emsp; &emsp; &emsp; atualiza a lista de pacotes com as versões mais novas

**apt upgrade** &emsp; &emsp; &emsp; &emsp; atualiza os pacotes com as novas versões

**apt remove** &emsp; &emsp; &emsp; &emsp; remove um pacote

**apt autoremove** &emsp; &emsp; &emsp; &emsp; remove pacotes que não são mais necessários


<br/>


### **Gerenciador DPKG**

<br/>

**dpkg -i** &emsp; &emsp; &emsp; &emsp; instala um pacote com extensão .deb

**dpkg -I** &emsp; &emsp; &emsp; &emsp; exibe as informações do pacote com extensão .deb

**dpkg -r** &emsp; &emsp; &emsp; &emsp; remove o pacote. É necessário usar o nome do pacote que se encontra nas informações


<br/>


### **Gerenciador RPM**

<br/>

**rpm -ivh** &emsp; &emsp; &emsp; &emsp; instala um pacote com extensão .rpm

**rpm -U** &emsp; &emsp; &emsp; &emsp; atualiza um pacote .rpm

**rpm -e** &emsp; &emsp; &emsp; &emsp; remove um pacote .rpm

<br/>


### **Gerenciador YUM**

<br/>

**yum install** &emsp; &emsp; &emsp; &emsp; instala um pacote e as dependências do pacote .rpm

**yum update** &emsp; &emsp; &emsp; &emsp; atualiza o pacote com as versão mais nova

**yum remove** &emsp; &emsp; &emsp; &emsp; remove o pacote






















































