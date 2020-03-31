#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import inject

from datetime import timedelta

from unittest import mock

from service.exceptions import BusinessException
from service._i18n import _
from service.transaction.transaction_service import TransactionService

from test.factory_fake.transaction.transaction_fake import TransactionFake


class TransactionServiceTest(unittest.TestCase):

    _transaction_fake = inject.attr(TransactionFake)

    def setUp(self):
        self._transaction_service = TransactionService()
        self.transaction = self._transaction_fake.get_fake_transaction()

    def test_do_transaction_when_installments_value_excedeed_minimum_income_value_then_raise_exception(self):
        # arrange
        self.transaction.income = 600

        # act / assert
        with self.assertRaises(BusinessException) as context:
            self._transaction_service.do_transaction(self.transaction)

        self.assertEqual(_('messages.minimum_income_commited'), str(context.exception))

    def test_do_transaction_when_has_low_score_then_then_raise_exception(self):
        # arrange
        self.transaction.score = 100
        self.transaction.income = 20000

        # act / assert
        with self.assertRaises(BusinessException) as context:
            self._transaction_service.do_transaction(self.transaction)

        self.assertEqual(_('messages.score_lower_than_minimum'), str(context.exception))

    def test_do_transaction_when_transaction_installments_low_then_minimum_then_raise_exception(self):
        # arrange
        self.transaction.score = 900
        self.transaction.installments = 2
        self.transaction.requested_value = 1000
        self.transaction.income = 30000

        # act / assert
        with self.assertRaises(BusinessException) as context:
            self._transaction_service.do_transaction(self.transaction)

        self.assertEqual(_('messages.installments_lower_than_minimum'), str(context.exception))

    @mock.patch('service.transaction.transaction_facade.TransactionService.'
                '_TransactionService__is_transaction_interval_less_than_the_permitted')
    @mock.patch('service.transaction.transaction_facade.TransactionService._TransactionService__is_same_date_transaction')
    def test_do_transaction_when_transaction_time_is_different_and_is_first_transaction_then_do_nothing(self,
                                                                                                is_same_date_transaction_method_mock,
                                                                            is_transaction_interval_less_than_the_permitted_method_mock):
        # arrange
        self.transaction.score = 900
        self.transaction.installments = 7
        self.transaction.income = 30000

        # act
        self._transaction_service.do_transaction(self.transaction)

        # assert
        is_same_date_transaction_method_mock.assert_not_called()
        is_transaction_interval_less_than_the_permitted_method_mock.assert_not_called()

    @mock.patch('service.transaction.transaction_facade.TransactionService.'
                '_TransactionService__is_transaction_interval_less_than_the_permitted')
    def test_do_transaction_when_transaction_time_is_not_on_same_date_then_do_nothing(self,
                                                                            is_transaction_interval_less_than_the_permitted_method_mock):
        # arrange
        self.transaction_aux = self._transaction_fake.get_fake_transaction()
        self.transaction_aux.time += timedelta(days=1)

        self.transaction.score = 900
        self.transaction.installments = 7
        self.transaction.income = 30000

        self._transaction_service._TransactionService__last_transaction_approved = self.transaction_aux

        # act
        self._transaction_service.do_transaction(self.transaction)

        # assert
        is_transaction_interval_less_than_the_permitted_method_mock.assert_not_called()

    def test_do_transaction_when_transaction_interval_is_less_than_permitted_then_raise_exception(self):

        # arrange
        self.transaction_aux = self._transaction_fake.get_fake_transaction()
        self.transaction_aux.time += timedelta(hours=0, minutes=0, seconds=0)

        self.transaction.score = 900
        self.transaction.installments = 7
        self.transaction.income = 30000
        self.transaction.time = self.transaction_aux.time

        self.transaction.time += timedelta(minutes=1, seconds=57)

        self._transaction_service._TransactionService__last_transaction_approved = self.transaction_aux

        # act / assert
        with self.assertRaises(BusinessException) as context:
            self._transaction_service.do_transaction(self.transaction)

        self.assertEqual(_('messages.transaction_interval_less_than_the_permitted'), str(context.exception))
