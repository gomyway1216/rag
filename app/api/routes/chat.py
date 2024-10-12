import os
import uuid

import chromadb
from fastapi import APIRouter
from openai import OpenAI

from app.models import (
    ChatRequest,
    ChatResponse,
    LearnRequest,
)


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
learn_collection = chromadb_client.get_or_create_collection(
    name="learn",
)


router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.post("/query", response_model=ChatResponse, status_code=200)
def query(chat_request: ChatRequest):
    # FIXME: This operation raises an error when the collection is empty
    rag_result = learn_collection.query(
        query_texts=[chat_request.message],
        n_results=1,
    )["documents"][0][0]

    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a therapist."},
            {"role": "system", "content": rag_result},
            {"role": "user", "content": chat_request.message},
        ],
    )
    return ChatResponse(message=response.choices[0].message.content)


@router.post("/learn", status_code=204)
def learn(learn_request: LearnRequest):
    learn_collection.add(
        documents=[learn_request.text],
        ids=[uuid.uuid4().hex],
    )
    return
