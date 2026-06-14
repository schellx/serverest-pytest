import requests
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


#tenta cadastrar duas vezes o mesmo e-mail
def test_nao_permitir_email_duplicado():
    email = gerar_email()

    payload = {
        "nome": "Usu1",
        "email": email,
        "password": "borboleta321",
        "administrador": "false"
    }

#primeiro cadastro
    requests.post(
        f"{BASE_URL}/usuarios",
        json=payload
    )

#tentativa de cadastro repetido
    response = requests.post(
        f"{BASE_URL}/usuarios",
        json=payload
    )

    body = response.json()

#valida que a API rejeitou a operacao
    assert response.status_code == 400

#valida a mensagem retornada
    assert body["message"] == "Este email já está sendo usado"


#verifica se o campo nome é obrigatorio
def test_cadastro_sem_nome():

    payload = {
        "email": gerar_email(),
        "password": "gato456",
        "administrador": "false"
    }

    response = requests.post(
        f"{BASE_URL}/usuarios",
        json=payload
    )

    body = response.json()

    assert response.status_code == 400

#valida que o campo nome e obrigatorio
    assert "nome" in body

#valida se a API nao permite cadastro sem e-mail
def test_cadastro_sem_email():
    payload = {
        "nome": "UsuTeste",
        "password": "0000",
        "administrador": "false"
    }

    response = requests.post(
        f"{BASE_URL}/usuarios",
        json=payload
    )

    body = response.json()

    assert response.status_code == 400
    assert "email" in body

#valida se a API não permite cadastro sem senha
def test_cadastro_sem_senha():
    payload = {
        "nome": "UsuTeste2",
        "email": gerar_email(),
        "administrador": "false"
    }

    response = requests.post(
        f"{BASE_URL}/usuarios",
        json=payload
    )

    body = response.json()

    assert response.status_code == 400
    assert "password" in body

#valida se e possível consultar um usuario existente utilizando seu id
def test_buscar_usuario_por_id():
    payload = {
        "nome": "UsuBusca",
        "email": gerar_email(),
        "password": "joaninha010",
        "administrador": "false"
    }

    cadastro = requests.post(
        f"{BASE_URL}/usuarios",
        json=payload
    )

    usuario_id = cadastro.json()["_id"]

    response = requests.get(
        f"{BASE_URL}/usuarios/{usuario_id}"
    )

    body = response.json()

    assert response.status_code == 200
    assert body["_id"] == usuario_id
    assert body["nome"] == payload["nome"]


 #verifica o comportamento da API ao buscar um usuário inexistente
def test_buscar_usuario_inexistente():
#correcao, com 16 caracteres
    usuario_id = "0000000000000000"

    response = requests.get(
        f"{BASE_URL}/usuarios/{usuario_id}"
    )

    body = response.json()

    assert response.status_code == 400
    assert body["message"] == "Usuário não encontrado"


#verifica se um usuário pode ser atualizado
def test_atualizar_usuario():
    payload = {
        "nome": "UsuOrigens",
        "email": gerar_email(),
        "password": "passarinho000",
        "administrador": "false"
    }

    cadastro = requests.post(
        f"{BASE_URL}/usuarios",
        json=payload
    )

    usuario_id = cadastro.json()["_id"]

    dados_atualizados = {
        "nome": "UsuAtualizado",
        "email": gerar_email(),
        "password": "centopeia11111",
        "administrador": "true"
    }

    response = requests.put(
        f"{BASE_URL}/usuarios/{usuario_id}",
        json=dados_atualizados
    )

    body = response.json()

    assert response.status_code == 200
    assert body["message"] == "Registro alterado com sucesso"

#confirma se a atualizacao foi realizada
    busca = requests.get(
        f"{BASE_URL}/usuarios/{usuario_id}"
    )

    usuario = busca.json()

    assert usuario["nome"] == "UsuAtualizado"

#verifica se um usuario pode ser excluido
def test_excluir_usuario():
    payload = {
        "nome": "UsuExcluir",
        "email": gerar_email(),
        "password": "formiga8",
        "administrador": "false"
    }

    cadastro = requests.post(
        f"{BASE_URL}/usuarios",
        json=payload
    )

    usuario_id = cadastro.json()["_id"]

    response = requests.delete(
        f"{BASE_URL}/usuarios/{usuario_id}"
    )

    body = response.json()

    assert response.status_code == 200
    assert body["message"] == "Registro excluído com sucesso"