# 🤖 Furioso: Assistente Virtual da FURIA

Este projeto permite interagir com um assistente virtual divertido chamado **Furioso**, criado com FastAPI no back-end e uma interface em HTML com Bootstrap no front-end.

---

## 📸 O que ele faz?

- Recebe uma **pergunta escrita** e uma **imagem opcional**.
- Envia essas informações para a API do **Azure OpenAI (modelo GPT)**.
- Retorna uma resposta clara, direta e bem-humorada.
- Possui interface visual com chat simulando conversa entre usuário e bot.

---

## 🌐 Link do Repositório

👉 [https://github.com/patriceduardo/Estagio-Furia.git](https://github.com/patriceduardo/Estagio-Furia.git)

---

## 🗂 Estrutura do Projeto

```
Estagio-Furia/
├── backend/
│ ├── main.py # Código backend com FastAPI
│ └── requirements.txt # Dependências do projeto backend
│
├── frontend/
│ └── index.html # Interface web do chat
│
└── README.md # Este arquivo
```

---

## 🚀 Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/patriceduardo/Estagio-Furia.git
cd Estagio-Furia
```

### 2. Crie um ambiente virtual (recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o `main.py`

Edite o arquivo `main.py` e coloque suas credenciais do Azure OpenAI:

```python
AZURE_OPENAI_API_KEY = "sua-chave"
AZURE_OPENAI_ENDPOINT = "https://seu-endpoint.openai.azure.com/"
DEPLOYMENT_NAME = "nome-do-modelo"
```

---

### 5. Execute o servidor

```bash
uvicorn main:app --reload
```

O backend estará disponível em: [http://localhost:8000](http://localhost:8000)

---

### 6. Execute a interface HTML

Abra o arquivo `index.html` no seu navegador (clique duas vezes ou arraste para o Chrome/Edge).

> Obs: A interface envia requisições para `http://localhost:8000/perguntar`. Garanta que o backend esteja rodando.

---

## 🧪 Teste rápido com CURL

```bash
curl -X POST http://localhost:8000/perguntar -F "pergunta=Qual é o próximo jogo da FURIA?"
```

---

## 🧠 Tecnologias usadas

- FastAPI
- HTML + Bootstrap 
- JavaScript
- Azure OpenAI (GPT-4o-mini)
- Python 3.8+
- Uvicorn
- Github Copilot para documentação do Projeto (@workspace /explain)

---
## 📬 Contato

Em caso de dúvidas ou sugestões, abra uma issue no repositório. 😄