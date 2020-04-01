#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import inject

from unittest import mock

from service.exceptions import BusinessException
from service.transaction.transaction_facade import TransactionFacade
from service._i18n import _

from test.factory_fake.transaction.transaction_fake import TransactionFake


class TransactionFacadeTest(unittest.TestCase):

    _transaction_fake = inject.attr(TransactionFake)

    def setUp(self):
        self._transaction_facade = TransactionFacade()
        self.transaction = self._transaction_fake.get_fake_transaction()
        self.payload = self._transaction_fake.get_fake_payload()

    @mock.patch('service.transaction.transaction_facade.TransactionFacade._transaction_schema')
    @mock.patch('service.transaction.transaction_facade.TransactionFacade._transaction_service')
    def test_authorize_transaction_when_payload_error_then_do_nothing_and_set_unauthorized_transactiob(self, service_mock,
                                                                                                            schema_mock: dict):
        # arrange
        loaded = mock.MagicMock()
        loaded.errors = 'teste'

        schema_mock.load.return_value = loaded

        service_mock.do_transaction.return_value = True

        # act
        self._transaction_facade.authorize_transaction(self.payload)

        # assert
        schema_mock.load.assert_called_once_with(self.payload, many=False)
        service_mock.do_transaction.assert_not_called()

        self.assertEqual(len(self._transaction_facade.unauthorized_transactions()), 1)

    @mock.patch('service.transaction.transaction_facade.TransactionFacade._transaction_schema')
    @mock.patch('service.transaction.transaction_facade.TransactionFacade._transaction_service')
    def test_authorize_transaction_when_payload_error_then_do_nothing_and_set_unauthorized_transaction(self, service_mock,
                                                                                                            schema_mock: dict):
        # arrange
        first_transaction_index = 0
        loaded = mock.MagicMock()
        loaded.errors = 'teste'

        schema_mock.load.return_value = loaded

        service_mock.do_transaction.return_value = True

        # act
        self._transaction_facade.authorize_transaction(self.payload)

        # assert
        schema_mock.load.assert_called_once_with(self.payload, many=False)
        service_mock.do_transaction.assert_not_called()

        transaction_payload = self._transaction_facade.unauthorized_transactions()[first_transaction_index]

        self.assertEqual(transaction_payload['violations'][0], _('messages.payload_error'))
        self.assertEqual(len(self._transaction_facade.unauthorized_transactions()), 1)

    @mock.patch('service.transaction.transaction_facade.TransactionFacade._transaction_schema')
    @mock.patch('service.transaction.transaction_facade.TransactionFacade._transaction_service')
    def test_authorize_transaction_when_raise_business_exception_then_set_unauthorized_transaction(self, service_mock,
                                                                                                            schema_mock: dict):
        # arrange
        first_transaction_index = 0

        loaded = mock.MagicMock()
        dumped = mock.MagicMock()

        loaded.errors = []
        loaded.data = self.transaction

        dumped.data = self.payload

        schema_mock.load.return_value = loaded
        schema_mock.dump.return_value = dumped

        service_mock.do_transaction.side_effect = BusinessException('teste')

        # act
        self._transaction_facade.authorize_transaction(self.payload)

        # assert
        schema_mock.load.assert_called_once_with(self.payload, many=False)
        schema_mock.dump.assert_called_once_with(self.transaction)

        transaction_payload = self._transaction_facade.unauthorized_transactions()[first_transaction_index]

        self.assertEqual(transaction_payload['violations'][0], 'teste')
        self.assertEqual(len(self._transaction_facade.unauthorized_transactions()), 1)
