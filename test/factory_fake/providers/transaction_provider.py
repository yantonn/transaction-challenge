import random

from uuid import uuid4
from datetime import datetime

from faker.providers import BaseProvider


class Provider(BaseProvider):

    def transaction(self) -> dict:
        pack_value = self.__get_random_transaction_pack_value()

        return {
            'id': str(uuid4()),
            'consumer_id': str(uuid4()),
            'score': pack_value['score'],
            'income': pack_value['income'],
            'installments': pack_value['installments'],
            'requested_value': pack_value['requested_value'],
            'time': datetime.now()
        }

    @staticmethod
    def __get_random_transaction_pack_value() -> dict:
        return random.choice([
            {
                'score': 400,
                'income': 2400,
                'requested_value': 8300.45,
                'installments': 6
            },
            {
                'score': 120,
                'income': 4400,
                'requested_value': 9200.00,
                'installments': 10
            },
            {
                'score': 900,
                'income': 6400,
                'requested_value': 18300.45,
                'installments': 12
            }
        ])
