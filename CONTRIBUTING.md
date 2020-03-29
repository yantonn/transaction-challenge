## Contribuindo com o projeto

### Ambiente virtual

No desenvolvimento de aplicações `python` é comum o uso de ambientes virtuais, o que possibilita o isolamento da versão do python utilizada bem como as dependências do projeto. A recomendação oficial é o uso `venv`, recurso _builtin_ do python3+. Sua criação é fácil e deve ser feita dentro da pasta do projeto com o seguinte comando:

```sh
python3.7 -m venv .env
```

Com isso, o ambiente virtual será criada na pasta `.env`. Para ativar e desativar, os seguintes comandos podem ser utilizados:

```sh
# ativar o ambiente virtual
source .env/bin/activate

# e para desativar
deactivate
```

Com o ambiente ativo (comando `source`), os comandos `python` e `pip` farão referência ao python usado na criação do ambiente. O comando `python -v` pode ser utilizado para confirmação.

Para consultar a documentação completa do recurso, [clique aqui](https://docs.python.org/3/tutorial/venv.html).

#### Troubleshooting

- Para usuários de **Ubuntu 14.04** ou anterior, a criação do `venv` pode apresentar problemas. Como solução, basta utilizar o script abaixo.

```sh
python3.7 -m venv .env --without-pip
source .env/bin/activate
curl https://bootstrap.pypa.io/get-pip.py | python
deactivate
source .env/bin/activate
```


### Gerenciamento de dependências

As dependências do projeto são mantidas nos arquivos _requirements_, existindo uma separação entre as de produção as de somente desenvolvimento. Abaixo, comando para instalar as todas as dependências.

```
pip install -r requirements.txt -r requirements-dev.txt
```

>Não esqueça de configurar o ambiente virtual dessa instalação.

#### Troubleshooting

A versão 3.7 do Python pode apresentar erros relacionados ao `pip` por conta do parametro que utilizamos `--extra-index-url`. Esse bug pode ser conferido na issue correspondente do projeto `pip` através desse [link](https://github.com/pypa/pip/issues/6428)
Para solucionar essa situação é necessário atualizar o `pip` que está sendo utilizado dentro do `venv` do projeto a partir do comando

```sh
pip install --upgrade pip
```

Lembre de estar com o ambiente `venv` ativo para atualizar localmente. Observação: A partir da versão **19** do `pip` esse erro não ocorre mais.

Um erro pego com a atualização para o Python 3.7 foi em relação as dependencia necessárias para o `psycopg2`, onde no momento de instalar as dependencias é apresentado a mensagem

```sh
Error: pg_config executable not found.
```

Caso esse erro seja apresentado no momento de instalar as dependencias do projeto, será necessário instalar os seguintes pacotes na máquina. Considerando que é um sistema operacional `debian like`, o comando seria o seguinte

```sh
sudo apt-get install python3.7-dev
sudo apt-get install libpq-dev python-dev
```

### Automatizando

#### Bash

A pasta `sh` possui alguns scripts para auxiliar na realização de algumas atividades como: exportar variáveis de ambiente, migrar a base de dados, executar a aplicação, entre outros. Abaixo os comandos possíveis, considerando que você está na raiz do projeto.

```sh
# exporta as variáveis configuradas em .environment
./sh/setenv.sh

# migra a base de dados definida no arquivo .environment
./sh/migrate_db.sh

# executa os testes da aplicação
./sh/test.sh

# executa os testes da aplicação e exporta um relatório de cobertura de teste
./sh/coverage.sh

# executa a aplicação
./sh/start.sh
```

#### make

O comando `make` é um velho conhecido dos sistemas \*nix, e é suportando com alguns _targets_.

```sh
# migra a base de dados definida no arquivo .environment
$ make migrate

# executa os testes da aplicação
$ make tests

# executa os testes integrados da aplicação
$ make integrated-tests

# executa os testes da aplicação e exporta um relatório de cobertura de teste
$ make cov

# cria um ambiente virtual localmente no diretório .env
$ make venv

# instala as dependências do projeto já aplicando o repositório pypi privado
$ make install

# instala uma lib localmente com base em caminho relativo, ou seja, no
# exemplo a lib `era6-mq` deve ter seu `clone` no mesmo nível do projeto
$ make install-lib LIB=era6-mq

# executa a aplicação
$ make run
```