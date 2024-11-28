import os
import uuid

import chromadb
from fastapi import APIRouter
from openai import OpenAI


#This is a copy-paste for now

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

#Norify when the collection does not exist.
try:
    learn_collection = chromadb_client.get_collection(name="learn")
except ValueError:
    print("There is no collection. I will make one for you!")
    learn_collection = chromadb_client.create_collection(name="learn")


router = APIRouter()

#Read questions' text file
f = open("../data/RAG_chunk_evaluation_questions.txt", "r")
my_queries = f.read().split("\n")
print(my_queries)

"""
@router.post("/query", response_model=ChatResponse, status_code=200)
def query(chat_request: ChatRequest):
    # FIXME: This operation raises an error when the collection is empty
    # no need to ask the user for question for this.
    rag_result = learn_collection.query(
        query_texts=[chat_request.message],
        n_results=1,
    )["documents"][0][0]

    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a therapist."},
            {"role": "system", "content": rag_result},
            {"role": "user", "content": chat_request.message}, #Ask one question here.
            #How to ask all questions? Make it into one prompt or ask one by one. Let's ask one by one for my training.
        ],
    )
    return ChatResponse(message=response.choices[0].message.content)

#We don't need those functions. let them just run.

#I guess we don't need this?
@router.post("/learn", status_code=204)
def learn(learn_request: LearnRequest):
    learn_collection.add(
        documents=[learn_request.text],
        ids=[uuid.uuid4().hex],
    )
    return
"""