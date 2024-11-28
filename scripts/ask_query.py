import os

import chromadb
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

try:
    learn_collection = chromadb_client.get_collection(name="learn")
except ValueError:
    print("There is no collection. I will make one for you!")
    learn_collection = chromadb_client.create_collection(name="learn")


f = open("../data/RAG_chunk_evaluation_questions.txt", "r")
my_queries = f.read().split("\n")
f.close()

for q in my_queries:
    rag_result = learn_collection.query(
        query_texts=[q],
        n_results=1,
    )["documents"][
        0
    ][0]

    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "Please answer the question, given the following context.",
            },
            {"role": "system", "content": rag_result},
            {"role": "user", "content": q},  # Ask one question here.
        ],
    )

    print(response.choices[0].message.content)
