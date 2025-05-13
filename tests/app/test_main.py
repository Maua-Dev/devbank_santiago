from fastapi.exceptions import HTTPException
import pytest
from src.app.entities.conta_bancaria import ContaBancaria
from src.app.main import get_all_contas, get_conta, create_conta, delete_conta, update_conta
from src.app.repo.conta_repository_mock import ContaRepositoryMock

class Test_Main:
    def test_get_all_contas(self):
        repo = ContaRepositoryMock()
        response = get_all_contas()
        assert all([conta_expect.to_dict() == conta for conta_expect, conta in zip(repo.contas.values(), response.get("contas"))])

    def test_get_conta(self):
        repo = ContaRepositoryMock()
        numero_conta = "101"
        response = get_conta(numero_conta=numero_conta)
        assert response == {
            'conta_id' : numero_conta,
            'conta': repo.contas.get(numero_conta).to_dict()
        }

    def test_get_conta_id_is_none(self):

        numero_conta = None
        with pytest.raises(HTTPException) as err:
            get_conta(numero_conta=numero_conta)

    def test_get_conta_id_is_not_int(self):
        numero_conta = '1'
        with pytest.raises(HTTPException) as err:
            get_conta(numero_conta=numero_conta)

    def test_get_conta_id_is_not_positive(self):
        numero_conta = '-1'
        with pytest.raises(HTTPException) as err:
            get_conta(numero_conta=numero_conta)

    def test_create_conta(self):
        repo = ContaRepositoryMock()

        body = {
            'numero_conta': '101',
            'nome': 'test',
            'saldo': 1000.0,
            'agencia': '0001',
        }
        response = create_conta(request=body)
        assert response == {'conta_id': 0,'conta': {'nome': 'test', 'saldo': 1000.0, 'agencia': '0001'}}

    def test_create_conta_conflict(self):
        repo = ContaRepositoryMock()

        body = {
            'numero_conta': '101',
            'nome': 'test',
            'saldo': 1000.0,
            'agencia': '0001',
        }
        response = create_conta(request=body)
        assert response == {'numero_conta': '101','conta': {'nome': 'test', 'saldo': 1000.0, 'agencia': '0001'}}

    def test_create_conta_conflict(self):
        repo = ContaRepositoryMock()

        body = {
            'numero_conta': '101',
            'nome': 'test',
            'saldo': 1000.0,
            'agencia': '0001',
        }
        response = create_conta(request=body)
        assert response == {'numero_conta': '101','conta': {'nome': 'test', 'saldo': 1000.0, 'agencia': '0001'}}

    def test_create_conta_conflict(self):
        repo = ContaRepositoryMock()

        body = {
            'numero_conta': '101',
            'nome': 'test',
            'saldo': 1000.0,
            'agencia': '0001',
        }
        with pytest.raises(HTTPException) as err:
            create_conta(request=body)
    
    def test_create_conta_missing_id(self):
        body = {
            'nome': 'test',
            'saldo': 1000.0,
            'agencia': '0001',
        }
        with pytest.raises(HTTPException) as err:
            create_conta(request=body)

    def test_create_conta_id_is_not_int(self):
        body = {
            'numero_conta': '0',
            'nome': 'test',
            'saldo': 1000.0,
            'agencia': '0001',
        }
        with pytest.raises(HTTPException) as err:
            create_conta(request=body)

    def test_create_numero_conta_is_not_positive(self):
        body = {
            'numero_conta': '-1',
            'nome': 'test',
            'saldo': 1000.0,
            'agencia': '0001',
        }
        with pytest.raises(HTTPException) as err:
            create_conta(request=body)

    def test_create_agencia_missing_type(self):
        body = {
            'numero_conta': '101',
            'nome': 'test',
            'saldo': 1000.0,
            'agencia': '0001',
        }
        with pytest.raises(HTTPException) as err:
            create_conta(request=body)

    def test_create_conta_id_is_not_string(self):
        body = {
            'numero_conta': 1,
            'nome': 'test',
            'saldo': 1000.0,
            'agencia': '0001',
        }
        with pytest.raises(HTTPException) as err:
            create_conta(request=body)

    def test_create_conta_agencia_is_not_valid(self):
        body = {
            'numero_conta': '101',
            'nome': 'test',
            'saldo': 1000.0,
            'agencia': '0001',
        }
        with pytest.raises(HTTPException) as err:
            create_conta(request=body)

    def test_create_conta_param_not_validated(self):
        body = {
            'numero_conta': '101',
            'nome': '',
            'saldo': 1000.0,
            'agencia': '0001',
        }
        with pytest.raises(HTTPException) as err:
            create_conta(request=body)

    def test_delete_conta(self):
        body = {
            "numero_conta": '101'
        }
        response = delete_conta(request=body)
        assert response == {'numero_conta': '101', 'conta': {'nome': 'Barbie', 'saldo': 48.9, 'agencia': '0001'}}

    def test_delete_conta_missing_id(self):
        with pytest.raises(HTTPException) as err:
            delete_conta(request={})

    def test_delete_conta_id_is_not_int(self):
        body = {
            "numero_conta": '1'
        }
        with pytest.raises(HTTPException) as err:
            delete_conta(request=body)

    def test_delete_conta_id_not_found(self):
        body = {
            "numero_conta": '100'
        }
        with pytest.raises(HTTPException) as err:
            delete_conta(request=body)

    def test_delete_conta_id_not_positive(self):
        body = {
            "numero_conta": '-100'
        }
        with pytest.raises(HTTPException) as err:
            delete_conta(request=body)

    def test_delete_conta_id_not_found(self):
        body = {
            "numero_conta": '4'
        }
        with pytest.raises(HTTPException) as err:
            delete_conta(request=body)

    def test_update_conta(self):
        body = {
            "numero_conta": '101',
            "nome": "test",
            "saldo": 1000.0,
            "agencia": "0001"
        }
        response = update_conta(request=body)
        assert response == {'numero_conta': '101', 'conta': {'nome': 'test', 'saldo': 1000.0, 'agencia': '0001'}}

    def test_update_conta_missing_id(self):
        body = {
            "nome": "test",
            "saldo": 1000.0,
            "agencia": "0001"
        }
        with pytest.raises(HTTPException) as err:
            update_conta(request=body)

    def test_update_conta_id_is_not_int(self):
        body = {
            "numero_conta": "1",
            "nome": "test",
            "saldo": 1000.0,
            "agencia": "0001"
        }
        with pytest.raises(HTTPException) as err:
            update_conta(request=body)

    def test_update_conta_not_positive(self):
        body = {
            "numero_conta": "1",
            "nome": "test",
            "saldo": -1000.0,
            "agencia": "0001"
        }
        with pytest.raises(HTTPException) as err:
            update_conta(request=body)

    def test_update_conta_not_positive(self):
        body = {
            "numero_conta": "1",
            "nome": "test",
            "saldo": -1000.0,
            "agencia": "0001"
        }
        with pytest.raises(HTTPException) as err:
            update_conta(request=body)

    def test_update_conta_without_admin_permission(self):
        body = {
            "numero_conta": "4",
            "nome": "test",
            "saldo": 1000.0,
            "agencia": "0001"
        }
        with pytest.raises(HTTPException) as err:
            update_conta(request=body)

    def test_update_conta_without_admin_permission(self):
        body = {
            "numero_conta": "4",
            "nome": "test",
            "saldo": 1000.0,
            "agencia": "0001"
        }
        with pytest.raises(HTTPException) as err:
            update_conta(request=body)

    def test_update_conta_without_admin_permission(self):
        body = {
            "numero_conta": "4",
            "nome": "test",
            "saldo": 1000.0,
            "agencia": "0001"
        }
        with pytest.raises(HTTPException) as err:
            update_conta(request=body)

    def test_update_conta_type_not_valid(self):

        body = {
            "numero_conta": "4",
            "nome": "test",
            "saldo": 1000.0,
            "agencia": "0001"
        }
        with pytest.raises(HTTPException) as err:
            update_conta(request=body)
            