from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .environments import Environments
from .repo.conta_repository_mock import ContaRepositoryMock
from .errors.entity_errors import ParamNotValidated
from .entities.conta_bancaria import ContaBancaria


app = FastAPI()
repo = Environments.get_conta_repo()() #Retorna o repositório de contas mockado

@app.get("/contas/get_all")
def get_all_contas():
    contas = repo.get_all_contas()
    return {
        "contas": [conta.to_dict() for conta in contas]
    }

@app.get("/contas/{numero_conta}")
def get_conta(numero_conta: int):
    conta = repo.get_conta(numero_conta)
    if conta is None:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    return {
        "numero_conta": numero_conta,
        "conta": conta.to_dict()
    }

@app.post("/contas/create", status_code=201)
def create_conta(request: dict):
    numero_conta = request.get("numero_conta")
    if repo.get_conta(numero_conta):
        raise HTTPException(status_code=409, detail="Conta já existe")

    try:
        conta = ContaBancaria(
            nome=request.get("nome"),
            agencia=request.get("agencia"),
            numero_conta=numero_conta,
            saldo=request.get("saldo")
        )
    except ParamNotValidated as err:
        raise HTTPException(status_code=400, detail=err.message)

    conta_criada = repo.create_conta(conta)
    return {
        "numero_conta": numero_conta,
        "conta": conta_criada.to_dict()
    }
    
@app.delete("/contas/delete")
def delete_conta(request: dict):
    numero_conta = request.get("numero_conta")
    conta = repo.get_conta(numero_conta)
    if conta is None:
        raise HTTPException(status_code=404, detail="Conta não encontrada")

    conta_excluida = repo.delete_conta(numero_conta)
    return {
        "numero_conta": numero_conta,
        "conta": conta_excluida.to_dict()
    }
    
@app.put("/contas/update")
def update_conta(request: dict):
    numero_conta = request.get("numero_conta")
    conta = repo.get_conta(numero_conta)
    if conta is None:
        raise HTTPException(status_code=404, detail="Conta não encontrada")

    nome = request.get("nome")
    agencia = request.get("agencia")
    saldo = request.get("saldo")

    conta_atualizada = repo.update_conta(numero_conta, nome, agencia, saldo)

    return {
        "numero_conta": numero_conta,
        "conta": conta_atualizada.to_dict()
    }
    


handler = Mangum(app, lifespan="off")
