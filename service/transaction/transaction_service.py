import datetime
from typing import Optional

from model.transaction import Transaction

from service.exceptions import BusinessException
from service._i18n import _

MININUM_SCORE_VALUE_PERMITED = 200
MINIMUM_INSTALLMENTS_PERMITED = 6
MINIMUM_TRANSACTION_INTERVAL_PERMITTED_SECONDS = 120
MINIMUM_COMMITED_VALUE_PERCENTAGE = 30 / 100


class TransactionService:
    """
    Classe de serviço de uma transação, domina e acopla todas as regras de negócio ligadas ao domínio "Transaction"
    """

    def __init__(self):
        self.__last_transaction_approved = None

    def do_transaction(self, transaction: Transaction) -> Transaction:
        """
        Método base para efetuar uma transação, efetua as validações de negócio e regitra a ultima transação aprovada.
        :param transaction: Instância de um objeto dataclass com representando uma entidade "transaction"
        :return: Instância de um objeto dataclass com representando uma entidade "transaction"
        """

        self.__validate_before_do_transaction(transaction)
        self.__last_transaction_approved = transaction

        return transaction

    def __validate_before_do_transaction(self, transaction: Transaction) -> Optional:
        """
        Método responsável por efetuar a chamada das validações de negócio que devem ser
        efetuadas em uma transaçtion
        :param transaction: Instância de um objeto dataclass com representando uma entidade "transaction"
        :return: Opcional exception "BusinessException" com uma mensagem padrão de erro.
        """
        self.__validate_committed_transaction_income(transaction)
        self.__validate_transaction_low_score(transaction)
        self.__validate_transaction_installments(transaction)
        self.__validate_transaction_time(transaction)

    @staticmethod
    def __validate_committed_transaction_income(transaction: Transaction) -> Optional:
        """
        Método responsável por validar se o valor da parcela de uma operação de crédito
        compromete mais que 30% do cliente requerinte do parcelamento
        :param transaction:
        :return: Opcional exception "BusinessException" com uma mensagem padrão de erro.
        """
        minimum_income_committed = transaction.income * MINIMUM_COMMITED_VALUE_PERCENTAGE

        if transaction.installment_value > minimum_income_committed:
            raise BusinessException(_('messages.compromised_income'))

    @staticmethod
    def __validate_transaction_low_score(transaction: Transaction) -> None:
        """
        Método responsável por verificar se uma transação possui um score menor que o mínimo permitido
        :param transaction: Instância de um objeto dataclass com representando uma entidade "transaction"
        :return: Opcional exception "BusinessException" com uma mensagem padrão de erro.
        """
        if transaction.score < MININUM_SCORE_VALUE_PERMITED:
            raise BusinessException(_('messages.low_score'))

    @staticmethod
    def __validate_transaction_installments(transaction: Transaction) -> None:
        """
        Método responsável por verificar se uma transação possui o mínimo de prestações permitidas
        :param transaction: Instância de um objeto dataclass com representando uma entidade "transaction"
        :return: Opcional exception "BusinessException" com uma mensagem padrão de erro.
        """
        if transaction.installments < MINIMUM_INSTALLMENTS_PERMITED:
            raise BusinessException(_('messages.minimum_installments'))

    def __validate_transaction_time(self, transaction: Transaction) -> Optional:
        """
        Método responsável por efetuar validações paralelas com transações já efetuadas
        anteriormente efetuando validações em cima de tempo e dia e se já foi processado ao menos uma transação.
        :param transaction: Opcional exception "BusinessException" com uma mensagem padrão de erro.
        :return:
        """
        if not self.__last_transaction_approved:
            return

        if not self.__is_same_date_transaction(transaction.time):
            return

        if self.__is_transaction_interval_less_than_the_permitted(transaction.time):
            raise BusinessException(_('messages.doubled_transactions'))

    def __is_same_date_transaction(self, current_transaction_time: datetime.timedelta) -> bool:
        """
        Método responsável por validar se a transação atual e a processada anteriormente são do mesmo dia, mês e ano
        :param transaction: Instância de um objeto dataclass com representando uma entidade "transaction"
        :return: bool
                    - True - Transação atual e anterior são do mesmo dia, mes e ano
                    - False - Transação atual e anterior não são do mesmo dia, mes e ano
        """
        last_approved_date = (
            self.__last_transaction_approved.time.day,
            self.__last_transaction_approved.time.month,
            self.__last_transaction_approved.time.year
        )

        current_transaction_date = (
            current_transaction_time.day,
            current_transaction_time.month,
            current_transaction_time.year
        )

        if current_transaction_date != last_approved_date:
            return False

        return True

    def __is_transaction_interval_less_than_the_permitted(self, current_transaction_time: datetime.timedelta) -> bool:
        """
        Método responsável por validar se o intervalo de tempo da transação atual e a anterior é menor que 2 minutos
        :param transaction: Instância de um objeto dataclass com representando uma entidade "transaction"
        :return: bool
                    - True - Diferença de tempo de processamento da transação atual para com a anterior é menor que 2 minutos
                    - False - Diferença de tempo de processamento da transação atual para com a anterior é maior que 2 minutos
                              ou seja, transação pode ser processada normalmente.

        """
        start_time = datetime.time(
            current_transaction_time.hour,
            current_transaction_time.minute,
            current_transaction_time.second
        )

        stop_time = datetime.time(
            self.__last_transaction_approved.time.hour,
            self.__last_transaction_approved.time.minute,
            self.__last_transaction_approved.time.second
        )

        date = datetime.date(1, 1, 1)

        first_datetime = datetime.datetime.combine(date, start_time)
        second_datetime = datetime.datetime.combine(date, stop_time)

        time_elapsed = first_datetime - second_datetime

        if time_elapsed.seconds <= MINIMUM_TRANSACTION_INTERVAL_PERMITTED_SECONDS:
            return True

        return False
