# Transaction Challenge

Basicamente consiste em um sistema que efetua a leitura de um arquivo contendo possiveis transações de crédito, onde que cada transação incorre em validações de negócio.
Após o fim do processamento, transações processadas com erro serão exportadas a um arquivo persistidas em um layout conforme sugerido pelo desafio.

# Executando em Ambiente Docker

Primeiro efetue o build da imagem utilizando o comando:

`
docker build -t transaction-challenge:0.1.0 .
`

Para executar o programa, em seu terminal execute o seguinte comando:

`
docker run -v /tmp/transaction-challenge/authorized:/tmp -it transaction-challenge:0.1.0
`

O resultado do processamento das transações poderá ser encontrado em: `tmp/transaction-challenge/authorized/authorized.txt`

# Design

- Para solucionar o problema abordei uma arquitetura simples usando um design pattern [Facade](https://www.tutorialspoint.com/design_pattern/facade_pattern.htm), visando em implementações futuras um não-acoplamento e dependência na classes de negócio, hoje se caracteriza apenas pela classe `TransactionFacade`.
- Para controle lógico do domínio `Transaction` utilizo um `service` onde possui o controle das regras de negócio em cima de uma entidade `transaction` ou qualquer regra de negócio para transações.
- Para controle a nivel de contrato(efetuando o parse de um objeto dict para uma represetação como objeto dataclass) utilizo o [marshmallow](https://marshmallow.readthedocs.io/en/2.x-line/) possibilitando uma flexibilidade tanto na leitura quanto na transformação no dado para um objeto específico.
- Todas as classes que possuem algum método ou exercem alguma lógica, possuem um teste unitário implementado.
- Para controle dos testes a serem executados utilizo o framework `pytest` dando uma velocidade na execução dos mesmos.


## Variáveis de ambiente

| Nome | Descrição | Valor padrão |
| --- | --- | --- |
| PYTHONPATH | Variável de ambiente usado pelo python para carregar os módulos da aplicação, conforme [documentação](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH) | N/A
| PYTHON_ENV | Tipos de ambiente conhecidos, sendo os possíveis `prod`, `dev` e `unittest` | prod
| TYPE_FILE_LOADER | Extenção do arquivo que sera carregado com as transações, atualmente suporta apenas `txt` | txt
| TYPE_FILE_WRITER | Extenção do arquivo de escrita para onde as transações com falha irão ser registradas, atualmente suporta apenas `txt` | txt
| OPERATIONS_PATH | Identifica onde o arquivo com as operações de transação estão localizados, por padrão aponta para a raiz do projeto | ./
| AUTHORIZED_OPERATIONS_PATH | Identifica o diretório para onde será exportado o arquivo das transações processadas com problema, por padrão aponta para a raiz do projeto | /tmp
| FILE_OPERATIONS_NAME | Identifica o nome do arquivo que irá conter as operações de transação, por padrão ele pesquisa por um arquivo chamado 'operations' | operations
| FILE_AUTHORIZED_NAME | Identifica o nome do arquivo que irá ser salvo o processamento das transações, por padrão ele salvará com o nome 'authorized' | authorized


## Referências

- [Contribua com o projeto](CONTRIBUTING.md)
- [Registro de alterações](CHANGELOG.md)
