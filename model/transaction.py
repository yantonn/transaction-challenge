import datetime
from dataclasses import dataclass


@dataclass
class Transaction:
    """
    id: Unique id from transaction model
    consumer_id: Unique id from consumer_id
    score: The actual score from the client
    """
    id: int
    consumer_id: int
    score: int
    income: int
    requested_value: int
    installments: int
    time: datetime.timedelta

    @property
    def installment_value(self) -> float:
        if self.installments is 0:
            return self.requested_value

        return self.requested_value / self.installments

    def __repr__(self) -> str:
        return f'[Transaction id="{self.id}", consumer_id="{self.consumer_id}, time={self.time}, score={self.score}"]'
