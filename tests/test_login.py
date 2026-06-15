import requests
from utils.gera_dados import gerar_email

BASE_URL = "https://compassuol.serverest.dev"


#cria um usuario e retorna suas credenciais
def criar_usuario():
    email = gerar_email()

    payload = {
        "nome": "Usuario Login",
        "email": email,
        "password": "senha123",
        "administrador": "true"
    }

    requests.post(
        f"{BASE_URL}/usuarios",
        json=payload
    )

    return email


#valida login com credenciais corretas
def test_login_valido():

    email = criar_usuario()

    payload = {
        "email": email,
        "password": "senha123"
    }

    response = requests.post(
        f"{BASE_URL}/login",
        json=payload
    )

    body = response.json()

    assert response.status_code == 200
    assert body["message"] == "Login realizado com sucesso"
    assert "authorization" in body


#valida login com senha incorreta
def test_login_senha_incorreta():

    email = criar_usuario()

    payload = {
        "email": email,
        "password": "senha_errada"
    }

    response = requests.post(
        f"{BASE_URL}/login",
        json=payload
    )

    body = response.json()

    assert response.status_code == 401
    assert body["message"] == "Email e/ou senha inválidos"


#valida login com email inexistente
def test_login_email_inexistente():

    payload = {
        "email": gerar_email(),
        "password": "senha123"
    }

    response = requests.post(
        f"{BASE_URL}/login",
        json=payload
    )

    body = response.json()

    assert response.status_code == 401
    assert body["message"] == "Email e/ou senha inválidos"


#valida login sem email
def test_login_sem_email():

    payload = {
        "password": "senha123"
    }

    response = requests.post(
        f"{BASE_URL}/login",
        json=payload
    )

    body = response.json()

    assert response.status_code == 400
    assert "email" in body


#valida login sem senha
def test_login_sem_senha():

    payload = {
        "email": "teste@teste.com"
    }

    response = requests.post(
        f"{BASE_URL}/login",
        json=payload
    )

    body = response.json()

    assert response.status_code == 400
    assert "password" in body