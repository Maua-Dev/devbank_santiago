from typing import Dict, Optional, List

from ..entities.conta_bancaria import ContaBancaria
from .conta_repository_interface import IContaRepository


class ContaRepositoryMock(IContaRepository):
    contas: Dict[int, ContaBancaria]

    def __init__(self):
        self.contas = {
            101: ContaBancaria(nome="João Silva", agencia="0001", numero_conta="101", saldo=1500.00),
            102: ContaBancaria(nome="Maria Souza", agencia="0002", numero_conta="102", saldo=2539.75),
            103: ContaBancaria(nome="Pedro Oliveira", agencia="0003", numero_conta="103", saldo=918.10),
            104: ContaBancaria(nome="Ana Albuquerque", agencia="0004", numero_conta="104", saldo=4710.95)
        }
        
    def get_all_contas(self) -> List[ContaBancaria]:
        return list(self.contas.values())
    
    def get_conta(self, numero_conta: int) -> Optional[ContaBancaria]:
        return self.contas.get(numero_conta)
    
    def create_conta(self, conta: ContaBancaria) -> ContaBancaria:
        self.conta[conta.numero_conta] = conta
        return conta
    
    def delete_conta(self, numero_conta: int) -> Optional[ContaBancaria]:
        return self.contas.pop(numero_conta, None)

    def update_conta(self, numero_conta: int, nome: str=None, agencia: str=None, saldo: float=None) -> Optional[ContaBancaria]:
        conta = self.contas.get(numero_conta)
        if conta is None:
            return None
        
        if nome is not None:
            conta.nome = nome
        if agencia is not None:
            conta.agencia = agencia
        if saldo is not None:
            conta.saldo = saldo
        self.contas[numero_conta] = conta

        return conta
        
    
    