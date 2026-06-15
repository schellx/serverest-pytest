# Automação de Testes da API ServeRest com Python e Pytest

## Sobre o projeto

Este projeto foi desenvolvido com o objetivo de praticar automação de testes de API utilizando Python e Pytest.

Os testes foram implementados nos endpoints de usuários, login e produtos da API ServeRest, contemplando os principais cenários de cadastro, autenticação, consulta, atualização e exclusão

API utilizada:

https://compassuol.serverest.dev/

---

## Tecnologias utilizadas

* Python 3
* Pytest
* Requests
* Pytest-cov (Análise de cobertura)
* Git
* GitHub
* Visual Studio Code

---

## Estrutura do projeto

```text
TesteAPI
│
├── tests
│   ├── test_login.py
│   ├── test_produtos.py
│   └── test_usuarios.py
│
├── utils
│   ├── autenticacao.py
│   └── gera_dados.py
│
│
├── .gitignore
├── PLANO-DE-TESTES.md
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Cenários automatizados

### Usuários

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

### Login

* Login com credenciais válidas
* Login com senha incorreta
* Login com e-mail inexistente
* Login sem e-mail
* Login sem senha

### Produtos

* Listar produtos cadastrados
* Cadastrar produto com token de administrador
* Validar cadastro de produto sem token
* Buscar produto por ID
* Atualizar produto
* Excluir produto

**Total de testes automatizados: 21**


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

## Executando os testes

Para executar todos os testes:

```bash
pytest -v
```

Exemplo de saída:

```text

============================= test session starts =============================
collected 21 items

tests/test_login.py .....                                                [ 23%]
tests/test_produtos.py ......                                            [ 52%]
tests/test_usuarios.py ..........                                        [100%]

============================= 21 passed in 18.62s =============================
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

## Cobertura de Testes

A cobertura de testes foi medida utilizando a biblioteca **pytest-cov**, executando o comando:

```bash
pytest --cov=tests --cov-report=term-missing
```

### Resultado Obtido

| Arquivo          | Cobertura |
| ---------------- | --------- |
| test_usuarios.py | 100%      |
| test_login.py    | 100%      |
| test_produtos.py | 100%      |

### Cobertura Total

**100% de cobertura** dos arquivos de teste analisados.

Resultado apresentado pelo pytest-cov:

```text
Name                    Stmts   Miss  Cover
-------------------------------------------
test_login.py              41      0   100%
test_produtos.py           52      0   100%
test_usuarios.py           77      0   100%
-------------------------------------------
TOTAL                     170      0   100%
```

--

## Autor

schellx
