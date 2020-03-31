#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from typing import Tuple, List

from dateutil.parser import parse as date_parser

from environment import get_file_operations_name, get_read_operations_path, get_type_file_loader
from service.file_loader.txt.base import TXTLoader


class TransactionTXTLoader(TXTLoader):

    def __init__(self):
        super().__init__(fields={
            'id': int,
            'consumer_id': int,
            'score': int,
            'income': int,
            'requested_value': int,
            'installments': int,
            'time': str
        })

    def load_data(self, file_name: str = f'{get_file_operations_name()}.{get_type_file_loader()}') -> Tuple[List[dict], List[dict]]:
        """
        Objetivo do método é efetuar iteração sobre as linhas do arquivo de importação, criando objeto conforme o modelo
        definido pelos fields

        :param file_name: Caminho do arquivo
        :return: Lista de dicionários representando o modelo definido pelos fields
        """
        record_success = []
        record_errors = []

        file_path = f'{get_read_operations_path()}/{file_name}'

        with open(file_path, 'r') as file_data:
            lines = file_data.readlines()

            for line in lines:
                try:
                    data = json.loads(line)['transaction']

                    for field, value in zip(self._fields.keys(), data.values()):
                        data[field] = self._fields[field](value) if value else None

                        data = self.get_default_fields(data)

                    record_success.append(data)

                except ValueError as ex:
                    self.__logger.error(_('logging.line_processed_with_error', line=line), exc_info=True)

                    record_errors.append({
                        'line_error': line,
                        'validations': [_('messages.line_processed_with_error')],
                        'error': ex.__str__()
                    })

            return record_success, record_errors
