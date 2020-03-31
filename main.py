import inject
import logging
import logging.config

from typing import List

from service.file_loader.base import FileLoader
from service.transaction.authorized_transaction_file_builder import AuthorizedTransactionFileBuilder
from service.transaction.transaction_facade import TransactionFacade
from service._i18n import _

STOP_INTERFACE = '2'


def configure_logging():
    logging.config.fileConfig('logging.conf', disable_existing_loggers=False)


class ProgramInterface:

    _file_loader = inject.attr(FileLoader)

    def get_options(self) -> str:
        menu_message_options =\
            '[1] - Processar Transações de Crédito\n'\
            '[2] - Sair\n:'

        option = input(menu_message_options)

        return option

    def load_operations_from_file(self) -> List[dict]:
        return self._file_loader.load_data()


def run():
    configure_logging()

    logger = logging.getLogger(__name__)
    logger.info(_('logging.app_starting'))

    program_interface = inject.instance(ProgramInterface)
    transaction_facade = inject.instance(TransactionFacade)
    authorized_transaction_file_builder = inject.instance(AuthorizedTransactionFileBuilder)

    option = program_interface.get_options()

    if option == STOP_INTERFACE:
        exit()

    success_loaded_operations, error_loaded_operations = program_interface.load_operations_from_file()

    for transaction in success_loaded_operations:
        transaction_facade.authorize_transaction(transaction)

    authorized_transaction_file_builder.write_authorized_transactions()


if __name__ == '__main__':
    run()
