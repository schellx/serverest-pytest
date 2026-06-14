import requests
import pytest
from utils.gera_dados import gerar_email

BASE_URL = "https://compassuol.serverest.dev"


#verifica se a API retorna a lista de usuários cadastrados

def test_listar_usuarios():
    response = requests.get(
        f"{BASE_URL}/usuarios"
    )

    body = response.json()

#valida o código HTTP
    assert response.status_code == 200

#valida se existe a chave usuarios
    assert "usuarios" in body

#valida se o retorno é uma lista
    assert isinstance(body["usuarios"], list)


#cria um novo usuario utilizando um e-mail unico
def test_cadastrar_usuario_valido():

    payload = {
        "nome": "Edu Schell",
        "email": gerar_email(),
        "password": "cachorrinhos123",
        "administrador": "true"
    }

    response = requests.post(
        f"{BASE_URL}/usuarios",
        json=payload
    )

    body = response.json()

#valida que o cadastro foi realizado
    assert response.status_code == 201

#valida a mensagem retornada pela API
    assert body["message"] == "Cadastro realizado com sucesso"

#valida se foi gerado um identificador
    assert "_id" in body

