# Análise de log

Esta aplicação é uma implementação back-end utilizando python 2.7 e postgree.

Serviço realiza consulta personalizada para recuperar a quantidade de acessos de um determinado
artigo, qual autor é o mais populuar e qual dia teve maior incidência de requisição falhosa.
Os resultados podem ser visualizados no terminal.

Foi desenvolvido python e postgree.

## Getting Started

Para executar a aplicação em sua máquina local, siga as instruções abaixo.

### Prerequisites
Virtualbox e vagrant.
Script do banco de dados para criação e população das tabelas.

É necessário acesso ao CMD ou Terminal. Banco de dados postgree e Python 2.7 ou superior
instalado na sua máquina virtual.
Como instalar e executar uma máquina virtual pode ser verificado através dos links disponíveis
sessão de Built with.

Com o script execute: ```psql -d news -f newsdata.sql```
Para acessar os dados execute:```psql -d news```

Para conectar o código python ao banco foi utilizado o psycopg2.

### Installing
Necessário iniciar a sua VM com o Vagrant.
Clone o repositório para o mesmo diretório da sua VM que possui os arquivos de banco de dados., através do terminal ou CMD, navegue até a pasta que possui o arquivo de conexão do python.
Exemplo de execução: ```python conn.py```

Caso não haja nenhum problema, o sistema exibirá as consultas pré definidas no arquivo python.


## Deployment

Disponível apenas na versão de desenvolvimento.

## Built With


[python](https://www.python.org/)

[psycopg](http://initd.org/psycopg/)

[postgre](https://www.postgresql.org/)

[virtualbox](https://www.virtualbox.org/)

[vagrant](https://www.vagrantup.com/)

[Começando](https://www.vagrantup.com/intro/getting-started/)
