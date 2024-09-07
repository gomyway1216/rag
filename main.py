import os

import chromadb
from fastapi import FastAPI
from pydantic import BaseModel, Field
from openai import OpenAI

openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
chromadb_client = chromadb.HttpClient(
    host="chromadb",
    port=8000,
    ssl=False,
    headers=None,
    settings=chromadb.config.Settings(),
    tenant=chromadb.config.DEFAULT_TENANT,
    database=chromadb.config.DEFAULT_DATABASE,
)
collection = chromadb_client.get_or_create_collection(
    name="learn",
)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


class ChatRequest(BaseModel):
    message: str = Field(description="The message to be sent to the chatbot")


class ChatResponse(BaseModel):
    message: str = Field(description="The message to be sent to the chatbot")


@app.post("/query", response_model=ChatResponse, status_code=200)
def query(chat_request: ChatRequest):
    # TODO: perform similarity search on the message (RAG)
    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": chat_request.message}],
    )
    return ChatResponse(message=response.choices[0].message.content)


class LearnRequest(BaseModel):
    text: str = Field(description="The text to be learned by the chatbot")


@app.post("/learn", response_model=ChatResponse, status_code=200)
def learn(learn_request: LearnRequest):
    # 1. generate embeddings for the text: OpenAI
    embeddings = (
        openai_client.embeddings.create(
            input=[learn_request.text], model="text-embedding-3-large"
        )
        .data[0]
        .embedding
    )
    # 2. store the embeddings in the vector database: ChromaDB
    res = collection.add(
        # FIXME: add `ids`
        embeddings=[embeddings],
    )
    return ChatResponse(message=str(res))
