# Automação de Testes da API ServeRest com Python e Pytest

## Sobre o projeto

Este projeto foi desenvolvido com o objetivo de praticar automação de testes de API utilizando Python e Pytest.

Os testes foram implementados no endpoint de usuários da API ServeRest, contemplando os principais cenários de cadastro, consulta, atualização e exclusão de usuários

API utilizada:

https://compassuol.serverest.dev/

---

## Tecnologias utilizadas

* Python 3
* Pytest
* Requests
* Git
* GitHub
* Visual Studio Code

---

## Estrutura do projeto

```text
TesteAPI
│
├── tests
│   └── test_usuarios.py
│
├── utils
│   └── gera_dados.py
│
├── venv
│
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Cenários automatizados

Os seguintes cenários foram implementados:

* Listar usuários cadastrados
* Cadastrar usuário com dados válidos
* Validar cadastro com e-mail duplicado
* Validar cadastro sem nome
* Validar cadastro sem e-mail
* Validar cadastro sem senha
* Buscar usuário por ID
* Buscar usuário inexistente
* Atualizar usuário
* Excluir usuário

Total de testes automatizados: **10**

---

## Pré-requisitos

Antes de executar os testes, é necessário ter instalado:

* Python 3
* Git

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/schellx/serverest-pytest
```

Acesse a pasta do projeto:

```bash
cd TesteAPI
```

Crie o ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual:

### Windows

```bash
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Executando os testes

Para executar todos os testes:

```bash
pytest -v
```

Exemplo de saída:

```text
============================= test session starts =============================

collected 10 items

tests/test_usuarios.py::test_listar_usuarios PASSED
tests/test_usuarios.py::test_cadastrar_usuario_valido PASSED
tests/test_usuarios.py::test_nao_permitir_email_duplicado PASSED
tests/test_usuarios.py::test_cadastro_sem_nome PASSED
tests/test_usuarios.py::test_cadastro_sem_email PASSED
tests/test_usuarios.py::test_cadastro_sem_senha PASSED
tests/test_usuarios.py::test_buscar_usuario_por_id PASSED
tests/test_usuarios.py::test_buscar_usuario_inexistente PASSED
tests/test_usuarios.py::test_atualizar_usuario PASSED
tests/test_usuarios.py::test_excluir_usuario PASSED
```

---

## Objetivo de aprendizado

Este projeto foi desenvolvido para praticar conceitos de:

* Automação de testes de API
* Criação e execução de testes com Pytest
* Consumo de APIs utilizando Requests
* Validação de respostas HTTP
* Organização de projetos Python
* Controle de versão com Git e GitHub

---

## Autor

schellx
