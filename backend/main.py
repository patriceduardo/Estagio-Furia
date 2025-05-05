from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import base64
import openai
import uvicorn

# Configuração OpenAI Azure
AZURE_OPENAI_API_KEY = ""
AZURE_OPENAI_ENDPOINT = ""
DEPLOYMENT_NAME = "GPT-4o-mini"

openai.api_type = "azure"
openai.api_base = AZURE_OPENAI_ENDPOINT
openai.api_version = "2023-12-01-preview"
openai.api_key = AZURE_OPENAI_API_KEY

app = FastAPI()

# Permitir requisições do frontend
app.add_middleware(a
    CORSMiddleware,a
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rota para receber pergunta e imagem
@app.post("/perguntar")
async def perguntar(pergunta: str = Form(...), imagem: UploadFile = File(None)):
    messages = [
    {
        "role": "system",
        "content": "Você é um assistente muito divertido do time da furia uma empresa e E-Sports, direto e bem-informado. Responda de forma clara e objetiva e sempre bem humorado., seu nome é Furioso assistente do site da Furia"
    },
    {
        "role": "user",
        "content": pergunta
    }
]

    if imagem:
        img_bytes = await imagem.read()
        img_base64 = base64.b64encode(img_bytes).decode("utf-8")
        img_message = {
            "role": "user",
            "content": f"![image](data:image/jpeg;base64,{img_base64})"
        }
        messages.append(img_message)

    try:
        response = openai.ChatCompletion.create(
            engine=DEPLOYMENT_NAME,
            messages=messages,
            max_tokens=1000
        )
        resposta = response.choices[0].message.content
        return {"resposta": resposta}
    except Exception as e:
        return {"erro": str(e)}

# Para rodar: uvicorn main:app --reload
