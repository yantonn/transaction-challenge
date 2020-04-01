#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import inject

from unittest import mock

from service.transaction.authorized_transaction_file_builder import AuthorizedTransactionFileBuilder
from test.factory_fake.transaction.transaction_fake import TransactionFake


class AuthorizedTransactionFileBuilderTest(unittest.TestCase):

    _authorized_transaction_file_builder = inject.attr(AuthorizedTransactionFileBuilder)
    _transaction_fake = inject.attr(TransactionFake)

    def setUp(self):
        self.transaction = self._transaction_fake.get_fake_transaction()

    @mock.patch('service.transaction.authorized_transaction_file_builder.json')
    @mock.patch('service.transaction.authorized_transaction_file_builder.AuthorizedTransactionFileBuilder._transaction_facade')
    def test_write_authorized_transactions_when_have_to_write_then_write(self, transaction_facade_mock, json_method_mock):

        # arrange

        transaction_facade_mock.unauthorized_transactions.return_value = [
            self.transaction
        ]

        write_text = 'teste'

        json_method_mock.dumps.return_value = write_text

        # act / assert
        with mock.patch('builtins.open', mock.mock_open()) as context:
            file = context()

            self._authorized_transaction_file_builder.write_authorized_transactions()

            file.write.assert_called_once_with(f'{write_text}\n')

            json_method_mock.dumps.assert_called_once_with(self.transaction)

    @mock.patch('service.transaction.authorized_transaction_file_builder.json')
    @mock.patch('service.transaction.authorized_transaction_file_builder.AuthorizedTransactionFileBuilder._transaction_facade')
    def test_write_authorized_transactions_when_not_have_to_write_then_do_nothing(self, transaction_facade_mock, json_method_mock):
        # arrange
        transaction_facade_mock.unauthorized_transactions.return_value = []

        json_method_mock.dumps.return_value = True

        # act / assert
        with mock.patch('builtins.open', mock.mock_open()) as context:
            file = context()

            self._authorized_transaction_file_builder.write_authorized_transactions()

            file.write.assert_not_called()
            json_method_mock.dumps.assert_not_called()
