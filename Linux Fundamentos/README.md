# Linux: Introdução ao Sistema Operacional

<br/>

 &emsp; &emsp; **CTRL+ALT+T** &emsp; &emsp; &emsp; &emsp; abre o terminal

 &emsp; &emsp; **man** &emsp; &emsp; &emsp; &emsp; exibe o manual de um comando específico

 &emsp; &emsp; **pwd** &emsp; &emsp; &emsp; &emsp; exibe o caminho do diretório/local atual

 &emsp; &emsp; **ls** &emsp; &emsp; &emsp; &emsp; exibe a lista de arquivos e diretórios de uma pasta

 &emsp; &emsp; **ls -l** &emsp; &emsp; &emsp; &emsp; exibe a lista, detalhes e privilégios de arquivos e diretórios de uma pasta

 &emsp; &emsp; **cd** &emsp; &emsp; &emsp; &emsp; muda para um diretório específico

 &emsp; &emsp; **cd ..** &emsp; &emsp; &emsp; &emsp; retorna para o diretório anterior ao diretório atual

 &emsp; &emsp; **cd /** &emsp; &emsp; &emsp; &emsp; muda para um diretório raiz

 &emsp; &emsp; **mkdir** &emsp; &emsp; &emsp; &emsp; cria um diretório

 &emsp; &emsp; **mv** &emsp; &emsp; &emsp; &emsp; move um arquivo ou diretório. Pode ser usado para renomear

 &emsp; &emsp; **touch** &emsp; &emsp; &emsp; &emsp; cria um arquivo vazio

 &emsp; &emsp; **cp** &emsp; &emsp; &emsp; &emsp; copia um arquivo ou diretório

 &emsp; &emsp; **rm** &emsp; &emsp; &emsp; &emsp; remove um arquivo ou diretório





 








<br/><br/><br/>
          
# Linux: Diretórios e Comandos Essenciais

<br/>











<br/><br/><br/>

# Linux: Fundamentos de Redes e Comandos Avançados

<br/>

 &emsp; &emsp; **ifconfig** &emsp; &emsp; &emsp; &emsp; 

 &emsp; &emsp; **hostname** &emsp; &emsp; &emsp; &emsp; 

 &emsp; &emsp; **hostname -i** &emsp; &emsp; &emsp; &emsp; 

 &emsp; &emsp; **hostname -I** &emsp; &emsp; &emsp; &emsp; 

 &emsp; &emsp; **ping** &emsp; &emsp; &emsp; &emsp; 

 &emsp; &emsp; **traceroute** &emsp; &emsp; &emsp; &emsp; 

 &emsp; &emsp; **finger** &emsp; &emsp; &emsp; &emsp; 

 &emsp; &emsp; **w** &emsp; &emsp; &emsp; &emsp; 

 &emsp; &emsp; **whois** &emsp; &emsp; &emsp; &emsp; 

 &emsp; &emsp; **history** &emsp; &emsp; &emsp; &emsp; mostra o histórico de ações do terminal

 &emsp; &emsp; **history -c** &emsp; &emsp; &emsp; &emsp; limpa o histórico do terminal

 &emsp; &emsp; **alias** &emsp; &emsp; &emsp; &emsp; especifica um determinado alias para um comando. &emsp; *Ex: alias hh=history*

 &emsp; &emsp; **nl** &emsp; &emsp; &emsp; &emsp; exibe o arquivo e o número de linhas que ele contém. &emsp; *Ex: nl aularedes.txt*

 &emsp; &emsp; **wc -l** &emsp; &emsp; &emsp; &emsp; exibe o número de linhas em um arquivo, incluindo as linhas em branco

 &emsp; &emsp; **wc -w** &emsp; &emsp; &emsp; &emsp; exibe o número de palavras em um arquivo

 &emsp; &emsp; **wc -c** &emsp; &emsp; &emsp; &emsp; exibe o número de bytes de um arquivo

 &emsp; &emsp; **wc -m** &emsp; &emsp; &emsp; &emsp; exibe o número de caracteres em um arquivo

 &emsp; &emsp; **ls -a** &emsp; &emsp; &emsp; &emsp; exibe todos os arquivos de um diretório, incluindo os ocultos

 &emsp; &emsp; **ls -F** &emsp; &emsp; &emsp; &emsp; exibe os arquivos de um diretório com / no final

 &emsp; &emsp; **cmp** &emsp; &emsp; &emsp; &emsp; compara dois arquivos byte por byte

 &emsp; &emsp; **diff** &emsp; &emsp; &emsp; &emsp; compara dois arquivos linha por linha

 &emsp; &emsp; **sort -n** &emsp; &emsp; &emsp; &emsp; organiza as linhas de um arquivo em ordem numerica, de acordo com o valor de string

 &emsp; &emsp; **last reboot** &emsp; &emsp; &emsp; &emsp; exibe a informação de todas as reinicializações do sistema

 &emsp; &emsp; **route -n** &emsp; &emsp; &emsp; &emsp; exibe as informações de Tabela de Roteamento IP do Kernel

 &emsp; &emsp; **time** &emsp; &emsp; &emsp; &emsp; exibe o tempo de processo de um comando

 &emsp; &emsp; **uptime** &emsp; &emsp; &emsp; &emsp; exibe a quanto tempo o sistema esta rodando

 &emsp; &emsp; **cowsay** &emsp; &emsp; &emsp; &emsp; exibe uma string em um texto-imagem de uma vaca. &emsp; *Ex: cowsay "Linux é Bom"*

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

 &emsp; &emsp; **cmatrix** &emsp; &emsp; &emsp; &emsp; exibe o efeito matrix no terminal

 &emsp; &emsp; **init 0** &emsp; &emsp; &emsp; &emsp; desliga o sistema

 &emsp; &emsp; **telinit 0** &emsp; &emsp; &emsp; &emsp; desliga o sistema

 &emsp; &emsp; **halt** &emsp; &emsp; &emsp; &emsp; desliga o sistema através de autenticação

 &emsp; &emsp; **seq** &emsp; &emsp; &emsp; &emsp; exibe uma sequencia de números no terminal. &emsp; *Ex: seq 1 10*

 &emsp; &emsp; **shuf** &emsp; &emsp; &emsp; &emsp; exibe uma permutação aleatória.  &emsp; *Ex: shuf -i 0-80 -n5*

 &emsp; &emsp; **whereis** &emsp; &emsp; &emsp; &emsp; exibe o caminho de um comando e seu manual

 &emsp; &emsp; **which** &emsp; &emsp; &emsp; &emsp; exibe o caminho de um comando


<br/><br/><br/>



# Linux: Gerenciamento de Pacotes


### **Gerenciador APT** 

<br/>

 &emsp; &emsp; **apt install** &emsp; &emsp; &emsp; &emsp; instala um pacote e as dependências

 &emsp; &emsp; **apt update** &emsp; &emsp; &emsp; &emsp; atualiza a lista de pacotes com as versões mais novas

 &emsp; &emsp; **apt upgrade** &emsp; &emsp; &emsp; &emsp; atualiza os pacotes com as novas versões

 &emsp; &emsp; **apt remove** &emsp; &emsp; &emsp; &emsp; remove um pacote

 &emsp; &emsp; **apt autoremove** &emsp; &emsp; &emsp; &emsp; remove pacotes que não são mais necessários


<br/>


### **Gerenciador DPKG**

<br/>

 &emsp; &emsp; **dpkg -i** &emsp; &emsp; &emsp; &emsp; instala um pacote com extensão .deb

 &emsp; &emsp; **dpkg -I** &emsp; &emsp; &emsp; &emsp; exibe as informações do pacote com extensão .deb

 &emsp; &emsp; **dpkg -r** &emsp; &emsp; &emsp; &emsp; remove o pacote. É necessário usar o nome do pacote que se encontra nas informações


<br/>


### **Gerenciador RPM**

<br/>

 &emsp; &emsp; **rpm -ivh** &emsp; &emsp; &emsp; &emsp; instala um pacote com extensão .rpm

 &emsp; &emsp; **rpm -U** &emsp; &emsp; &emsp; &emsp; atualiza um pacote .rpm

 &emsp; &emsp; **rpm -e** &emsp; &emsp; &emsp; &emsp; remove um pacote .rpm

<br/>


### **Gerenciador YUM**

<br/>

 &emsp; &emsp; **yum install** &emsp; &emsp; &emsp; &emsp; instala um pacote e as dependências do pacote .rpm

 &emsp; &emsp; **yum update** &emsp; &emsp; &emsp; &emsp; atualiza o pacote com as versão mais nova

 &emsp; &emsp; **yum remove** &emsp; &emsp; &emsp; &emsp; remove o pacote


<br><br><br>


<H1>Linux: Controle de usuários e (Des)Compactações de Arquivos</H1>
<!---
<div style="text-indent: 35px">
	<p>	<b>adduser nomedousuario </b> &emsp;&mdash;&emsp; comando para adicionar um novo usuário</p>
	<p>	<b>su nomedousuario </b> &emsp;&mdash;&emsp; mudar de usuário no terminal</p>
	<p>	<b>passwd nomedousuario </b> &emsp;&mdash;&emsp; mudar a senha do usuário</p>
	<p>	<b>lastlog</b> &emsp;&mdash;&emsp; exibe informações de login de todos os usuários do sistema.</p>
	<p>	<b>last</b> &emsp;&mdash;&emsp; exibe uma listagem de entrada e saída do usuário no sistema.</p>
	<p>	<b>logname</b> &emsp;&mdash;&emsp; exibe o nome do usuário logado no sistema.</p>
	<p>	<b>id</b> &emsp;&mdash;&emsp; exibe todos os identificadores do usuário.</p>
	<p>	<b>userdel -r nomedousuario</b> &emsp;&mdash;&emsp; remove o usuário e sua respectiva pasta pessoal (-r).</p>
	<p>	<b>cat /etc/group</b> &emsp;&mdash;&emsp; exibe todos os grupos do sistema.</p>
	<p>	<b>groups</b> &emsp;&mdash;&emsp; exibe todos os grupos do usuário.</p>
	<p>	<b>addgroup nomedogrupo</b> &emsp;&mdash;&emsp; adiciona um grupo ao sistema.</p>
	<p>	<b>adduser nomedousuario nomedogrupo</b> &emsp;&mdash;&emsp; adiciona um usuário a um grupo.</p>
	<p>	<b>gpasswd -a nomedousuario nomedogrupo</b> &emsp;&mdash;&emsp; adiciona um usuário a um grupo.</p>
	<p>	<b>gpasswd -d nomedousuario nomedogrupo</b> &emsp;&mdash;&emsp; remove um usuário de um grupo.</p>
	<p>	<b>groupdel nomedogrupo</b> &emsp;&mdash;&emsp; remove o grupo.</p>
	<p>	<b>ls -lh</b> &emsp;&mdash;&emsp; lista os arquivos e exibe as permissões de leitura, escrita e execução do diretório.</p>
	<p>	<b>chmod xxx nomedoarquivo</b> &emsp;&mdash;&emsp; modifica as permissões de um arquivo/pasta. O chmod usa o <i>Modo Octal</i>, onde xxx são três números que vão de 0 a 7 (seguindo as permissões da tabela abaixo).</p>	<br>
	--->

 &emsp; &emsp; **gzip arquivo** &emsp; &emsp; &emsp; &emsp; compacta o arquivo usando o programa gzip

 &emsp; &emsp; **adduser nomedousuario** &emsp; &emsp; &emsp; &emsp; comando para adicionar um novo usuário.

 &emsp; &emsp; **su nomedousuario** &emsp; &emsp; &emsp; &emsp; mudar de usuário no terminal

 &emsp; &emsp; **passwd nomedousuario** &emsp; &emsp; &emsp; &emsp; mudar a senha do usuário

 &emsp; &emsp; **lastlog** &emsp; &emsp; &emsp; &emsp; exibe informações de login de todos os usuários do sistema.

 &emsp; &emsp; **last** &emsp; &emsp; &emsp; &emsp; exibe uma listagem de entrada e saída do usuário no sistema.

 &emsp; &emsp; **logname** &emsp; &emsp; &emsp; &emsp; exibe o nome do usuário logado no sistema.

 &emsp; &emsp; **id** &emsp; &emsp; &emsp; &emsp; exibe todos os identificadores do usuário.

 &emsp; &emsp; **userdel -r nomedousuario** &emsp; &emsp; &emsp; &emsp; remove o usuário e sua respectiva pasta pessoal (-r).

 &emsp; &emsp; **cat /etc/group** &emsp; &emsp; &emsp; &emsp; exibe todos os grupos do sistema.

 &emsp; &emsp; **groups** &emsp; &emsp; &emsp; &emsp; exibe todos os grupos do usuário.

 &emsp; &emsp; **addgroup nomedogrupo** &emsp; &emsp; &emsp; &emsp; adiciona um grupo ao sistema.

 &emsp; &emsp; **adduser nomedousuario nomedogrupo** &emsp; &emsp; &emsp; &emsp; adiciona um usuário a um grupo.

 &emsp; &emsp; **gpasswd -a nomedousuario nomedogrupo** &emsp; &emsp; &emsp; &emsp; adiciona um usuário a um grupo.

 &emsp; &emsp; **gpasswd -d nomedousuario nomedogrupo** &emsp; &emsp; &emsp; &emsp; remove um usuário de um grupo.

 &emsp; &emsp; **groupdel nomedogrupo** &emsp; &emsp; &emsp; &emsp; remove o grupo.

 &emsp; &emsp; **ls -lh** &emsp; &emsp; &emsp; &emsp; lista os arquivos e exibe as permissões de leitura, escrita e execução do diretório.

 <pre>
	<table align="center">
		<tbody>
			<tr align="center">
				<td colspan="3">Owner</td>
				<td colspan="3">Group</td>
				<td colspan="3">Other</td>
			</tr>
			<tr>
				<td>R</td>
				<td>W</td>
				<td>X</td>
				<td>R</td>
				<td>W</td>
				<td>X</td>
				<td>R</td>
				<td>W</td>
				<td>X</td>
			</tr>
			<tr>
				<td>4</td>
				<td>2</td>
				<td>1</td>
				<td>4</td>
				<td>2</td>
				<td>1</td>
				<td>4</td>
				<td>2</td>
				<td>1</td>
			</tr>
		</tbody>
	</table>
</pre>

<br/>


### **Compactador gzip**

<br/>

 &emsp; &emsp; **gzip arquivo** &emsp; &emsp; &emsp; &emsp; compacta o arquivo usando o programa gzip

 &emsp; &emsp; **gunzip arquivo.gz** &emsp; &emsp; &emsp; &emsp; descompacta o arquivo usando o programa gzip

 &emsp; &emsp; **gzip -9 arquivo** &emsp; &emsp; &emsp; &emsp; usa a compactação máxima para compactar o arquivo

<br/>


### **Compactador zip**

<br/>

 &emsp; &emsp; **zip arquivo.zip arquivo1 arquivo2 ...** &emsp; &emsp; &emsp; &emsp; compacta o(s) arquivo(s) usando o programa zip

 &emsp; &emsp; **unzip arquivo.zip** &emsp; &emsp; &emsp; &emsp; descompacta o arquivo usando o programa zip


<br/>


### **Compactador bzip2**

<br/>

 &emsp; &emsp; **bzip arquivo** &emsp; &emsp; &emsp; &emsp; compacta o arquivo usando o programa bzip2

 &emsp; &emsp; **bzip -d arquivo.bz2** &emsp; &emsp; &emsp; &emsp; descompacta o arquivo usando o programa bzip2

<br/>


### **Compactador rar**

<br/>

 &emsp; &emsp; **rar a arquivo.rar nomedoarquivo** &emsp; &emsp; &emsp; &emsp; compacta o arquivo
 
 &emsp; &emsp; **rar x arquivo.rar** &emsp; &emsp; &emsp; &emsp; descompacta o arquivo


### **Arquivador tar**

<br/>

 &emsp; &emsp; **tar -cf arquivo.tar arquivo1 arquivo2 ...** &emsp; &emsp; &emsp; &emsp; cria um único arquivo de vários arquivos.

 &emsp; &emsp; **tar -xvf arquivo.tar.gz** &emsp; &emsp; &emsp; &emsp; descompacta e desarquiva os arquivos































