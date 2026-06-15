import uuid
import requests
from utils.autenticacao import gerar_token_admin

BASE_URL = "https://compassuol.serverest.dev"

#verifica se a API retorna a lista de produtos
def test_listar_produtos():

    response = requests.get(
        f"{BASE_URL}/produtos"
    )

    body = response.json()

    assert response.status_code == 200
    assert "produtos" in body
    assert isinstance(body["produtos"], list)


#verifica se um administrador pode cadastrar produto
def test_cadastrar_produto():

    token = gerar_token_admin()
    
    nome_dinamico = f"mouse gamer {uuid.uuid4().hex[:6]}" #nome unico para o produto não dar failed ao rodar pela segunda vez

    payload = {
        "nome": nome_dinamico,
        "preco": 100,
        "descricao": "mouse com rgb",
        "quantidade": 10
    }

    response = requests.post(
        f"{BASE_URL}/produtos",
        headers={"Authorization": token},
        json=payload
    )

    body = response.json()

    assert response.status_code == 201
    assert body["message"] == "Cadastro realizado com sucesso"
    assert "_id" in body

# verifica se a API bloqueia cadastro sem autenticação
def test_cadastrar_produto_sem_token():

    payload = {
        "nome": "teclado maquina de escrever",
        "preco": 200,
        "descricao": "teclado estilizado",
        "quantidade": 5
    }

    response = requests.post(
        f"{BASE_URL}/produtos",
        json=payload
    )

    body = response.json()

    assert response.status_code == 401
    assert body["message"] == "Token de acesso ausente, inválido, expirado ou usuário do token não existe mais"


#verifica se é possível buscar produto por id
def test_buscar_produto_por_id():

    token = gerar_token_admin()
    
    nome_dinamico = f"Headset com microfone {uuid.uuid4().hex[:6]}" #nome unico

    cadastro = requests.post(
        f"{BASE_URL}/produtos",
        headers={"Authorization": token},
        json={
            "nome": nome_dinamico,
            "preco": 300,
            "descricao": "Headset sem fio com microfone acoplado",
            "quantidade": 2
        }
    )

    produto_id = cadastro.json()["_id"]

    response = requests.get(
        f"{BASE_URL}/produtos/{produto_id}"
    )

    body = response.json()

    assert response.status_code == 200
    assert body["_id"] == produto_id

#verifica se um produto pode ser atualizado
def test_atualizar_produto():

    token = gerar_token_admin()
    
    nome_original = f"Monitor {uuid.uuid4().hex[:6]}" #nome unico
    nome_atualizado = f"Monitor atualizado {uuid.uuid4().hex[:6]}" #nome unico

    cadastro = requests.post(
        f"{BASE_URL}/produtos",
        headers={"Authorization": token},
        json={
            "nome": nome_original,
            "preco": 500,
            "descricao": "Monitor antigo",
            "quantidade": 3
        }
    )

    produto_id = cadastro.json()["_id"]

    response = requests.put(
        f"{BASE_URL}/produtos/{produto_id}",
        headers={"Authorization": token},
        json={
            "nome": nome_atualizado,
            "preco": 700,
            "descricao": "Monitor novo",
            "quantidade": 4
        }
    )

    body = response.json()

    assert response.status_code == 200
    assert body["message"] == "Registro alterado com sucesso"

# verifica se um produto pode ser removido
def test_excluir_produto():

    token = gerar_token_admin()

    cadastro = requests.post(
        f"{BASE_URL}/produtos",
        headers={"Authorization": token},
        json={
            "nome": "webcam",
            "preco": 150,
            "descricao": "Webcam full HD",
            "quantidade": 1
        }
    )

    produto_id = cadastro.json()["_id"]

    response = requests.delete(
        f"{BASE_URL}/produtos/{produto_id}",
        headers={"Authorization": token}
    )

    body = response.json()

    assert response.status_code == 200
    assert body["message"] == "Registro excluído com sucesso"