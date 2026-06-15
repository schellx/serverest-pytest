# Plano de Testes - Desafio Técnico | Sprint 2

## Objetivo

Garantir que os principais fluxos da API ServeRest funcionem corretamente através de testes automatizados utilizando Python e Pytest.

A suíte busca validar operações críticas relacionadas a usuários, autenticação e produtos, verificando respostas, códigos HTTP e regras de negócio

---

## Estratégia de Testes

### Tipo de teste

Testes funcionais de API.

### Camada testada

Camada de serviços (REST API).

### Ferramentas utilizadas

* Python
* Pytest
* Requests
* Git
* GitHub
* Visual Studio Code

---

## Escopo

### Em escopo

#### Usuários

* Listar usuários
* Cadastrar usuário
* Validar e-mail duplicado
* Validar campos obrigatórios
* Buscar usuário por ID
* Atualizar usuário
* Excluir usuário

#### Login

* Login com credenciais válidas
* Login com senha incorreta
* Login com e-mail inexistente
* Login com campos vazios

#### Produtos

* Listar produtos
* Cadastrar produto
* Cadastrar produto sem autenticação
* Buscar produto por ID
* Atualizar produto
* Excluir produto

---

## Fora de escopo

* Testes de performance
* Testes de carga
* Testes de segurança avançados
* Testes de interface gráfica
* Testes de banco de dados

---

## Cenários Planejados

### Endpoint Usuários

* Cadastro válido
* Cadastro com e-mail duplicado
* Cadastro sem nome
* Cadastro sem e-mail
* Cadastro sem senha
* Listagem de usuários
* Busca por ID válido
* Busca por ID inexistente
* Atualização de usuário
* Exclusão de usuário

### Endpoint Login

* Login válido
* Login com senha inválida
* Login com e-mail inexistente
* Login sem e-mail
* Login sem senha

### Endpoint Produtos

* Listar produtos
* Cadastrar produto com token válido
* Cadastrar produto sem token
* Buscar produto por ID
* Atualizar produto
* Excluir produto

---

## Critérios de Qualidade

Um teste será considerado concluído quando:

* Executar sem falhas
* Possuir asserts para código HTTP
* Validar informações relevantes da resposta
* Ser independente dos demais testes
* Utilizar dados dinâmicos quando necessário
* Possuir nome descritivo
* Estiver versionado no GitHub
