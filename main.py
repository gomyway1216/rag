import os
import uuid

import chromadb
from fastapi import FastAPI
from pydantic import BaseModel, Field
from openai import OpenAI

openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
chromadb_client = chromadb.HttpClient(
    host=os.getenv("CHROMADB_HOST", "chromadb"),
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
    message: str = Field(description="The message to be responded by the chatbot")


@app.post("/query", response_model=ChatResponse, status_code=200)
def query(chat_request: ChatRequest):
    # Perform similarity search and fetch relevant information
    rag_result = collection.query(
        query_texts=[chat_request.message],
        n_results=1,
    )["documents"][0][0]

    # Perform chat completion using the retrieved information
    # TODO: Clean up the query text
    # TODO: Add integration tests
    query_text = f"Use this information: {rag_result}\n"
    query_text += "=" * 80 + "\n"
    query_text += "Reply 'I don't know' if you don't find the answer in the given context.\n"
    query_text += "=" * 80 + "\n"
    query_text += chat_request.message

    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": query_text}],
    )
    return ChatResponse(message=response.choices[0].message.content)


class LearnRequest(BaseModel):
    text: str = Field(description="The text to be learned by the chatbot")


@app.post("/learn", status_code=204)
def learn(learn_request: LearnRequest):
    collection.add(
        documents=[learn_request.text],
        ids=[uuid.uuid4().hex],
    )
    return
