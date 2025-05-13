import pytest
from src.app.entities.conta_bancaria import ContaBancaria
from src.app.repo.conta_repository_mock import ContaRepositoryMock

class Test_ContaRepositoryMock:
    def test_get_all_contas(self):
        repo = ContaRepositoryMock()
        assert all([conta_expect == conta for conta_expect, conta in zip(repo.contas.values(), repo.get_all_contas())])

    def test_get_conta(self):
        repo = ContaRepositoryMock()
        conta = repo.get_conta(numero_conta="101")
        assert conta == repo.contas.get("101")

    def test_get_conta_not_found(self):
        repo = ContaRepositoryMock()
        conta = repo.get_conta(numero_conta="999")
        assert conta is None
        
    def test_create_conta(self):
        repo = ContaRepositoryMock()
        len_before = len(repo.contas)
        conta = ContaBancaria(nome="test", agencia="0001", numero_conta="101", saldo=1500.00)
        repo.create_conta(conta=conta)
        len_after = len(repo.contas)
        assert len_after == len_before + 1
        assert repo.contas.get(0) == conta
        
    def test_delete_conta(self):
        repo = ContaRepositoryMock()
        conta_expected_to_be_deleted = repo.contas.get("101")
        len_before = len(repo.contas)
        conta = repo.delete_conta(numero_conta="101")
        len_after = len(repo.contas)
        assert len_after == len_before - 1
        assert conta == conta_expected_to_be_deleted
        
    def test_delete_conta_not_found(self):
        repo = ContaRepositoryMock()
        conta = repo.delete_conta(numero_conta="999")
        assert conta is None

    def test_update_conta(self):
        repo = ContaRepositoryMock()
        nova_conta = ContaBancaria(nome="test", agencia="0001", numero_conta="101", saldo=1500.00)
        conta_atualizada = repo.update_conta(
            numero_conta="101", 
            nome=nova_conta.nome, 
            agencia=nova_conta.agencia, 
            saldo=nova_conta.saldo
        )

        assert conta_atualizada == nova_conta
        assert repo.contas.get("101") == nova_conta

    def test_update_conta_partial_nome(self):
        repo = ContaRepositoryMock()
        nome = "Nome Partial"
        conta_atualizada = repo.update_conta(
            numero_conta="101",
            nome=nome
        )

        assert conta_atualizada.nome == nome
        assert repo.contas.get("101").nome == nome

    def test_update_conta_partial_saldo(self):
        repo = ContaRepositoryMock()
        saldo = 2000.00
        conta_atualizada = repo.update_conta(
            numero_conta="101",
            saldo=saldo
        )

        assert conta_atualizada.saldo == saldo
        assert repo.contas.get("101").saldo == saldo