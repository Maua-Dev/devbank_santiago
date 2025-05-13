import pytest
from src.app.entities.conta_bancaria import ContaBancaria
from src.app.errors.entity_errors import ParamNotValidated


class Test_ContaBancaria:
    def test_conta_bancaria_valida(self):
        conta = ContaBancaria(nome = "João Silva", agencia = "0001", numero_conta = "101", saldo = 1500.00)
        assert conta.nome == "João Silva"
        assert conta.agencia == "0001"
        assert conta.numero_conta == "101"
        assert conta.saldo == 1500.00

    def test_conta_bancaria_to_dict(self):
        conta = ContaBancaria(nome = "Maria Souza", agencia = "0002", numero_conta = "102", saldo = 2539.75)
        assert conta.to_dict() == {
            'nome': 'Maria Souza',
            'agencia': '0002',
            'numero_conta': '102',
            'saldo': 2539.75
        }

    def test_nome_none(self):
        with pytest.raises(ParamNotValidated):
            ContaBancaria(nome=None, agencia="0001", numero_conta="101", saldo=1500.00)
            
    def test_nome_nao_string(self):
        with pytest.raises(ParamNotValidated):
            ContaBancaria(nome=123, agencia="0001", numero_conta="101", saldo=1500.00)
            
    def test_nome_muito_curto(self):
        with pytest.raises(ParamNotValidated):
            ContaBancaria(nome="Jo", agencia="0001", numero_conta="101", saldo=1500.00)
            
    def test_numero_conta_none(self):
        with pytest.raises(ParamNotValidated):
            ContaBancaria(nome="test", agencia="0001", numero_conta=None, saldo=1500.00)

    def test_numero_conta_nao_string(self):
        with pytest.raises(ParamNotValidated):
            ContaBancaria(nome="test", agencia="0001", numero_conta=123, saldo=1500.00)

    def test_numero_conta_com_tamanho_invalido(self):
        with pytest.raises(ParamNotValidated):
            ContaBancaria(nome="test", agencia="0001", numero_conta="10", saldo=1500.00)

    def test_saldo_none(self):
        with pytest.raises(ParamNotValidated):
            ContaBancaria(nome="test", agencia="0001", numero_conta="101", saldo=None)

    def test_saldo_nao_float(self):
        with pytest.raises(ParamNotValidated):
            ContaBancaria(nome="test", agencia="0001", numero_conta="101", saldo="1500.00")

    def test_saldo_negativo(self):
        with pytest.raises(ParamNotValidated):
            ContaBancaria(nome="test", agencia="0001", numero_conta="101", saldo=-1500.00)

    def test_agencia_none(self):
        with pytest.raises(ParamNotValidated):
            ContaBancaria(nome="test", agencia=None, numero_conta="101", saldo=1500.00)

    def test_agencia_nao_string(self):
        with pytest.raises(ParamNotValidated):
            ContaBancaria(nome="test", agencia=123, numero_conta="101", saldo=1500.00)

    def test_agencia_com_tamanho_invalido(self):
        with pytest.raises(ParamNotValidated):
            ContaBancaria(nome="test", agencia="00", numero_conta="101", saldo=1500.00)
