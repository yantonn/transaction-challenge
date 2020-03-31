# Changelog :newspaper:

# {version} [{date}]

### Minor
   - branch(feature/add_unit_test_file_builder) - Adicionado teste unitario na classe builder de arquivos de transação
   - branch(feature/adding_main_application) - Adicionado arquivo `main.py` para executar aplicação como um todo.
   - branch(feature/transaction_file_builder):
        - Adicionado classe responsável por construir e gravar o resultado para todas as transações processadas.
        - Adicionado também arquivo de configuração de log da aplicação.
   - branch(feature/creating_transaction_business_logic):
        - Adição das classes de fachada e serviço para representar ações em uma transação, representadas por `TransactionFacade` e `TransactionService`
        - Adição de arquivo `service/exceptions.py` com classe padrão para exceções de negócio.
        - Adição de uma `factory` de dados `fakes`, utilizando a lib `faker` para trabalhar com dados mais próximos da realidade da aplicação, podendo posteriormente serem utilizados em testes integrados e automatizados.
        - Adição de um `provider` de dados fakes para uma transação.
        - Adição de diretório `test/unit` com todos os testes unitários em `TransactionFacade` e `TransactionService` utilizando o framework `pytest`. Foi criado diretório específico `test/unit` para futuramente segregar em outros tipos de teste, como `automated/`, `integrated/` entre outros.
   - branch(feature/file_loader):
        - Adição de abstrações utilizando ABC python e classes para performar leitura em um arquivo de transações txt.
        - Adição de provider de `file` para injeção de dependência 
   - branch(feature/add_sh_and_environment_info):
        - Adição de diretório `sh` com scripts para setar as variáveis de ambiente e inicializar a aplicação.
        - Adição de `.editorconfig` para padronizar configurações de editores
        - Adição de arquivo `.environment` com variáveis de ambiente do sistema.
        - Adição de `environment.py` com métodos de acesso a estas variáveis de ambiente.
        - Adição de arquivos `requirements.txt`(Possui as dependências de lib para execução do sistema) e `requirements-dev.txt`(Possui as dependências de lib em ambiente de desenvolvimento).  
   - branch(feature/creating_resource_module):
        - Criação de módulo `resource` com classe `ResourceReader` para acesso a recursos de dentro deste módulo.
        - Criação de `json` com especificação de mensagens para uso do `i18n` para padronizar mensagens no sistema.
   - branch(feature/creating_transaction_schema) - Criação de schemas para carregamento de contrato e posterior instancia de uma dataclass de transação. 
   - branch(feature/creating_data_models) - Criação de modelos para representação de um objeto de transação.

### Patch
   - branch(bugfix/file_loader_transaction_service):
        - Ajuste na mensagem de log na classe `TransactionService`
        - Adicionado arquivo de operations.txt com todas as operações passiveis de problema e sucesso.
        - Ajuste para environment apontar para ambiente local
        - Ajuste nos unitarios em razao da alteração da mensagem de log
   - branch(bugfix/adjust_unit_tests):
        - Ajuste na assinatura de alguns métodos com o type hint
        - Ajuste nos testes unitarios onde foram alteradas o padrao de mensagem
        - Criacao de novas chaves no resource visto que nao existiam no json internacionalização das mensagens da aplicação.
