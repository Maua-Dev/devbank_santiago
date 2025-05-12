from abc import ABC, abstractmethod
from typing import List, Optional

from ..entities.conta_bancaria import ContaBancaria


class IContaRepository(ABC):
    
    
    @abstractmethod
    def get_all_contas(self) -> List[ContaBancaria]:
        '''
        Retorna todas as contas bancárias cadastradas no banco de dados
        '''
        pass
    
    @abstractmethod
    def get_conta(self, numero_conta: int) -> Optional[ContaBancaria]:
        '''
        Retorna a conta bancária com o número especificado.
        Se não existir, retorna None.
        '''
        pass
    
    @abstractmethod
    def create_conta(self, conta: ContaBancaria) -> ContaBancaria:
        '''
        Cria uma nova conta bancária.
        '''
        pass
    
    @abstractmethod
    def delete_conta(self, numero_conta: int) -> Optional[ContaBancaria]:
        '''
        Remove a conta bancária com o número especificado.
        Se não existir, retorna None.
        '''
        pass

    @abstractmethod
    def update_conta(self, numero_conta: int, nome: str=None, agencia: str=None, saldo: float=None) -> Optional[ContaBancaria]:
        '''
        Atualiza os dados de uma conta bancária existente.
        Se não existir, retorna None.
        '''
        pass

    