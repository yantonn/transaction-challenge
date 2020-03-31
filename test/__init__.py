from faker import Faker
from faker_credit_score import CreditScore

from test.factory_fake.providers.transaction_provider import Provider as TransactionProvider

fake = Faker('pt_BR')

fake.add_provider(CreditScore)
fake.add_provider(TransactionProvider)
