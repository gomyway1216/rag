import os
import uuid

import chromadb


EMBEDDING_COLLECTION_NAME = "learn"


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
    chromadb_client.get_collection(name=EMBEDDING_COLLECTION_NAME)
    chromadb_client.delete_collection(name=EMBEDDING_COLLECTION_NAME)
except ValueError:
    pass

learn_collection = chromadb_client.create_collection(
    name="learn",
)

f = open("../data/chapterXX.txt", "r")
my_documents = f.read().split("\n")
my_ids = [f"{uuid.uuid4().hex}" for _ in range(len(my_documents))]


learn_collection.add(
    documents=my_documents,
    ids=my_ids,
)
