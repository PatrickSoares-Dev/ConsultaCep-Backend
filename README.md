# 📦 Consulta de CEP - API Backend

API desenvolvida em **Python (FastAPI)** que permite a consulta de CEPs via [API ViaCEP](https://viacep.com.br/), com autenticação de usuários, controle de crédito por consulta e geração de histórico individualizado.

---

## 📌 Funcionalidades

- 🔐 Autenticação JWT (login, cadastro de usuários);
- 🔎 Consulta de endereços pelo CEP;
- 💰 Cobrança por uso de créditos a cada consulta;
- 📈 Visualização de saldo, total de consultas e crédito utilizado;
- 📜 Histórico completo de consultas realizadas;
- 🧾 Documentação automática via Swagger/OpenAPI (`/docs`).

---

## 🖼️ Arquitetura da Aplicação

A aplicação segue o modelo representado no **Cenário 1.1**:

![Arquitetura da Aplicação](/image.png)

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.11**
- **FastAPI**
- **SQLAlchemy (ORM)**
- **SQLite (ambiente local) / PostgreSQL (produção)**
- **JWT para autenticação**
- **Docker**

---

## 🧪 Instalação Local

### 1. Clone o projeto

```bash
git clone https://github.com/seu-usuario/consulta-cep-backend.git
cd consulta-cep-backend
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação localmente

```bash
uvicorn main:app --reload
```

A API estará disponível em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🐳 Rodando com Docker

### Build da imagem

```bash
docker build -t consulta-cep-backend .
```

### Executando o container

```bash
docker run -d -p 8000:8000 --name cep-backend consulta-cep-backend
```

---

## 🔐 Rotas Principais

| Rota                        | Método | Descrição                                |
|----------------------------|--------|-------------------------------------------|
| `/auth/login`              | POST   | Login do usuário e geração de token JWT  |
| `/auth/register`           | POST   | Cadastro de novo usuário                 |
| `/cep/{cep}`               | GET    | Consulta endereço usando API ViaCEP      |
| `/cep/historico`           | GET    | Lista o histórico de consultas do usuário|
| `/billing`                 | GET    | Consulta dados de crédito                |
| `/billing/alterar`         | PUT    | Atualiza o saldo                         |
| `/billing/remover`         | PUT    | Remove parte do saldo (cobra)            |

---

## 📝 Licença e Créditos

Este projeto utiliza a **API pública do [ViaCEP](https://viacep.com.br/)** para realizar as consultas de CEP. Certifique-se de respeitar os limites de uso da API e atribuir os devidos créditos.

---

## ✍️ Autor

Patrick Soares de Oliveira  
Analista de Sistemas | Desenvolvedor Fullstack
