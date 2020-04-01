import logging
from typing import Optional, List

import inject

from model.transaction import Transaction

from schema.transaction.transaction import TransactionSchema

from service.exceptions import BusinessException
from service.transaction.transaction_service import TransactionService
from service._i18n import _


class TransactionFacade:
    """
    Classe de fachada provendo uma interface mais simplificada de negócio
    evitando alta dependencia das classes de negócio(service)
    """
    _logger = logging.getLogger(__name__)
    _transaction_service = inject.attr(TransactionService)
    _transaction_schema = inject.attr(TransactionSchema)

    def __init__(self):
        self.__unauthorized_transactions = []

    def authorize_transaction(self, payload: dict) -> Optional[dict]:
        """
        Autoriza uma transação efetuando algumas validações permitentes ao negócio
        verificando se o payload enviado não possui alguma inconsistência

        :param payload: Contrato para efetuar uma transação
        :return: Retorna a transação no formato de dicionário caso tenha ocorrido sem errors.
                 Caso contrário registra a transação na lista de transações não autorizadas.
        """
        transaction = self.__before_do_transaction(payload)

        if not transaction:
            return

        try:
            self._transaction_service.do_transaction(transaction)

            self._logger.info(_('logging.transaction_authorired', transaction=transaction))

            return self._transaction_schema.dump(transaction)

        except BusinessException as ex:
            self.__prepare_unauthorized_transaction(transaction, str(ex))

    def unauthorized_transactions(self) -> List[Transaction]:
        """
        Método responsável por retornar a lista de transações não autorizadas.
        :return:
        """
        return self.__unauthorized_transactions

    def __before_do_transaction(self, payload: dict) -> Optional[Transaction]:
        """
        Metodo responsável por validar se o payload de uma transação não possui alguma inconsistência a nivel de contrato.
        :param payload: contrato de uma transação
        :return: Retorna uma transação no formato de instância de uma dataclass transaction quando o payload não possui erros.
                 Caso contrário retorna None e adiciona o payload na lista de transações não autorizadas.
        """
        loaded = self._transaction_schema.load(payload, many=False)

        if loaded.errors:
            payload_error = self.__build_payload_violation_error(payload, _('messages.payload_error'))

            self.__unauthorized_transactions.append(payload_error)

            self._logger.error(_('logging.payload_error', payload=payload))

            return

        return loaded.data

    def __prepare_unauthorized_transaction(self, transaction: Transaction, message_exception: str = None) -> None:
        """
        Método responsável por preparar e adicionar uma transação não autorizada com um motivo pelo qual não foi autorizada
        :param transaction: Instância do objeto dataclass representando uma transação
        :param message_exception: mensagme pelo qual a transação não foi autorizada
        :return: Não possui, apenas adiciona a transação a lista de transações não autorizadas.
        """
        data = self._transaction_schema.dump(transaction).data

        payload_error = self.__build_payload_violation_error(data, message_exception)

        self.__unauthorized_transactions.append(payload_error)

        self._logger.error(_('logging.transaction_unauthorized', transaction=transaction, motive=message_exception))

    @staticmethod
    def __build_payload_violation_error(payload: dict, message: str) -> dict:
        """
        Metodo responsavel por retornar um dicionario simples com uma estrutura padrao para erros em um payload
        :param payload: contrato que possui o problema
        :param message: message para justificar o problema
        :return: dicicionario em um formato padrao
        """
        return {
            'id': payload['id'],
            'violations': [
                message
            ]
        }
