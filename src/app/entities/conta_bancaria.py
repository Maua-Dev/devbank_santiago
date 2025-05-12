from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.item_type_enum import ItemTypeEnum


class ContaBancaria:
    nome: str
    agencia: str
    numero_conta: str
    saldo: float

    def __init__(self, nome: str=None, agencia: str=None, numero_conta: str=None, saldo: float=0.0):
        validation_nome = self.validate_nome(nome)
        if validation_nome[0] is False:
            raise ParamNotValidated("nome", validation_nome[1])
        self.nome = nome

        validation_agencia = self.validate_agencia(agencia)
        if validation_agencia[0] is False:
            raise ParamNotValidated("agencia", validation_agencia[1])
        self.agencia = agencia

        validation_numero_conta = self.validate_numero_conta(numero_conta)
        if validation_numero_conta[0] is False:
            raise ParamNotValidated("numero_conta", validation_numero_conta[1])
        self.numero_conta = numero_conta

        validation_saldo = self.validate_saldo(saldo)
        if validation_saldo[0] is False:
            raise ParamNotValidated("saldo", validation_saldo[1])
        self.saldo = saldo

    @staticmethod
    def validate_nome(nome: str) -> Tuple[bool, str]:
        if nome is None:
            return (False, "Nome é obrigatório")
        if type(nome) != str:
            return (False, "Nome deve ser uma string")
        if len(nome) < 3:
            return (False, "Nome deve ter pelo menos 3 caracteres")
        return (True, "")
        
    @staticmethod
    def validate_agencia(agencia: str) -> Tuple[bool, str]:
        if agencia is None:
            return (False, "Agência é obrigatória")
        if type(agencia) != str:
            return (False, "Agência deve ser uma string")
        return (True, "")
    
    @staticmethod
    def validate_numero_conta(numero_conta: str) -> Tuple[bool, str]:
        if numero_conta is None:
            return (False, "Número da conta é obrigatório")
        if type(numero_conta) != str:
            return (False, "Número da conta deve ser uma string")
        return (True, "")

    @staticmethod
    def validate_saldo(saldo: float) -> Tuple[bool, str]:
        if saldo is None:
            return (False, "Saldo é obrigatório")
        if type(saldo) != float:
            return (False, "Saldo deve ser um número decimal")
        if saldo < 0:
            return (False, "Saldo não pode ser negativo")
        return (True, "")
            
    def to_dict(self):
        return {
            "nome": self.nome,
            "agencia": self.agencia,
            "numero_conta": self.numero_conta,
            "saldo": self.saldo
        }
    
    def __eq__(self,other):
        return (
            self.nome == other.nome and
            self.agencia == other.agencia and
            self.numero_conta == other.numero_conta and
            self.saldo == other.saldo
        )

    def __repr__(self):
        return (
            f"ContaBancaria(nome={self.nome}, agencia={self.agencia}, "
            f"numero_conta={self.numero_conta}, saldo={self.saldo})"
        )