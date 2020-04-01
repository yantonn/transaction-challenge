#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import inject

from unittest import mock

from service import FileLoader
from service.transaction.authorized_transaction_file_builder import AuthorizedTransactionFileBuilder
from service.transaction.transaction_facade import TransactionFacade
from service._i18n import _


class TransactionFacadeIntegratedTest(unittest.TestCase):

    _file_loader = inject.attr(FileLoader)
    _transaction_facade = inject.attr(TransactionFacade)
    _authorized_transaction_file_builder = inject.attr(AuthorizedTransactionFileBuilder)

    @mock.patch('service.transaction.authorized_transaction_file_builder.json')
    def test_authorize_transaction_with_integrated_test_then_validate_mock_result_file(self, json_method_mock):
        # arrange
        first_transaction_index = 0
        second_transaction_index = 1
        third_transaction_index = 2
        four_transaction_index = 3

        first_violation_index = 0

        record_data_success, record_data_error = self._file_loader.load_data()

        # act
        with mock.patch('builtins.open', mock.mock_open()) as context:
            file = context()

            for payload in record_data_success:
                self._transaction_facade.authorize_transaction(payload)

            self._authorized_transaction_file_builder.write_authorized_transactions()

            unauthorized_transactions = self._transaction_facade.unauthorized_transactions()

        # assert
        self.assertEqual(len(unauthorized_transactions), 4)

        self.assertEqual(
            unauthorized_transactions[first_transaction_index]['violations'][first_violation_index],
            _('messages.low_score')
        )

        self.assertEqual(
            unauthorized_transactions[second_transaction_index]['violations'][first_violation_index],
            _('messages.compromised_income')
        )

        self.assertEqual(
            unauthorized_transactions[third_transaction_index]['violations'][first_violation_index],
            _('messages.minimum_installments')
        )

        self.assertEqual(
            unauthorized_transactions[four_transaction_index]['violations'][first_violation_index],
            _('messages.doubled_transactions')
        )

        self.assertEqual(
            json_method_mock.dumps.call_args_list[first_transaction_index],
            mock.call(unauthorized_transactions[first_transaction_index])
        )

        self.assertEqual(
            json_method_mock.dumps.call_args_list[second_transaction_index],
            mock.call(unauthorized_transactions[second_transaction_index])
        )

        self.assertEqual(
            json_method_mock.dumps.call_args_list[third_transaction_index],
            mock.call(unauthorized_transactions[third_transaction_index])
        )

        self.assertEqual(
            json_method_mock.dumps.call_args_list[four_transaction_index],
            mock.call(unauthorized_transactions[four_transaction_index])
        )

        file.write.assert_called()
