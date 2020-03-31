#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import json
import inject

from typing import List, TextIO

from environment import get_type_file_writer, get_file_authorized_name, get_authorized_path

from model.transaction import Transaction

from service.transaction.transaction_facade import TransactionFacade
from service._i18n import _


class AuthorizedTransactionFileBuilder:
    """
    Classe builder para representar e escrever em um arquivo de autorização
    """
    _logger = logging.getLogger(__name__)
    _transaction_facade = inject.attr(TransactionFacade)

    def __init__(self):
        self.__file_extension = get_type_file_writer()
        self._file_name = get_file_authorized_name()
        self.__file_path = f'{get_authorized_path()}/{self._file_name}.{self.__file_extension}'

    def write_authorized_transactions(self) -> None:
        """
        Método responsável por validar se existe transações não aprovadas antes de abrir e efetuar a escrita no arquivo.
        :return: Não possui
        """
        unaunthorized_transactions = self._transaction_facade.unauthorized_transactions()

        if not unaunthorized_transactions:
            self._logger.info(_('logging.no_transactions_to_write'))
            return

        with open(self.__file_path, 'w') as file:
            self.__write_file(file, unaunthorized_transactions)

        self._logger.info(_('logging.transactions_file_write_success'))

    @staticmethod
    def __write_file(file: TextIO, transactions: List[Transaction]) -> TextIO:
        """
        Método responsável pela escrita de transações em um arquivo
        :param file: Instancia de um "file" aberto para escrita
        :param transactions: Instancia de uma dataclass que representa uma transação
        :return: file: a instancia de um objeto com a escrita da transação já realizada
        """
        for transaction in transactions:
            transaction_dumped = json.dumps(transaction)

            file.write(f'{transaction_dumped}\n')

        return file

    @property
    def file_name(self) -> str:
        return self._file_name

    @file_name.setter
    def file_name(self, value: str) -> None:
        self._file_name = value + self.__file_extension

    def get_file_path(self) -> str:
        return self.__file_path
