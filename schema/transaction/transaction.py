from marshmallow import Schema, fields, post_load

from model.transaction import Transaction


class TransactionSchema(Schema):
    """
    Classe schema que representa um payload de contrato de uma transação
    onde que após o carregamento retorna uma instancia de uma objeto dataclass representando uma transação
    """
    id = fields.Integer(required=True)
    consumer_id = fields.Integer(required=True)
    score = fields.Integer(required=True)
    income = fields.Integer(required=True)
    requested_value = fields.Integer(required=True)
    installments = fields.Integer(required=True)
    time = fields.DateTime()

    class Meta:
        fields = [
            'id',
            'consumer_id',
            'score',
            'income',
            'requested_value',
            'installments',
            'time'
        ]

    @post_load
    def make_transaction(self, data: dict) -> Transaction:
        """
        Método disparado quando efetuado a chamada de um .load(object).data onde efetua o retorno
        de uma instancia de um dataclass de uma transação
        :param data: payload que irá ser transformado
        :return: Instancia dataclass de umma transação.
        """
        return Transaction(**data)
