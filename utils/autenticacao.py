import requests
from utils.gera_dados import gerar_email

BASE_URL = "https://compassuol.serverest.dev"

#cria um administrador, faz login, obtém o token e retorna o token.

def gerar_token_admin():

    email = gerar_email()

    usuario = {
        "nome": "Administrador",
        "email": email,
        "password": "admin123",
        "administrador": "true"
    }

    requests.post(
        f"{BASE_URL}/usuarios",
        json=usuario
    )

    login = requests.post(
        f"{BASE_URL}/login",
        json={
            "email": email,
            "password": "admin123"
        }
    )

    token = login.json()["authorization"]

    return token