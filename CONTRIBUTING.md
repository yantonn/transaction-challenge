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

### Automatizando

#### Bash

A pasta `sh` possui alguns scripts para auxiliar na realização de algumas atividades como: exportar variáveis de ambiente, executar a aplicação, entre outros. Abaixo os comandos possíveis, considerando que você está na raiz do projeto.

```sh
# exporta as variáveis configuradas em .environment
./sh/setenv.sh

# executa os testes da aplicação
./sh/test.sh

# executa os testes da aplicação e exporta um relatório de cobertura de teste
./sh/coverage.sh

# executa a aplicação
./sh/start.sh
```
