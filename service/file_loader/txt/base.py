#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import logging
from typing import Tuple, List

from environment import get_read_operations_path, get_file_operations_name
from service._i18n import _
from service.file_loader.base import FileLoader


class TXTLoader(FileLoader):

    __logger = logging.getLogger(__name__)

    def __init__(self, fields: dict):
        self._fields = fields

    def load_data(self, file_name: str = get_file_operations_name()) -> Tuple[List, List]:
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
                    data = json.loads(line)

                    for field, value in zip(self._fields.keys(), data.values):
                        data[field] = self._fields[field](value) if value else None

                        data = self.get_default_fields(data)

                        record_success.append(data)

                except ValueError as ex:
                    self.__logger.error(_('logging.loader_field_value_error'), exc_info=True)
                    record_errors.append(ex.__str__())

            return record_success, record_errors

    def get_default_fields(self, data_load: dict):
        return data_load
