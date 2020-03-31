#!/usr/bin/env python
# -*- coding: utf-8 -*-
from model.transaction import Transaction

from test import fake


class TransactionFake:

    @staticmethod
    def get_fake_payload() -> dict:

        transaction = fake.transaction()

        return {
            'id': transaction['id'],
            'consumer_id': transaction['consumer_id'],
            'score': transaction['score'],
            'income': transaction['income'],
            'installments': transaction['installments'],
            'requested_value': transaction['requested_value'],
            'time': transaction['time']
        }

    def get_fake_transaction(self) -> Transaction:
        return Transaction(**self.get_fake_payload())
