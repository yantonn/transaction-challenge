# Changelog :newspaper:

# {version} [{date}]

### Minor
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
