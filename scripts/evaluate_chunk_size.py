import os
import uuid
import time

import chromadb
from openai import OpenAI


EMBEDDING_COLLECTION_NAME = "learn"
chunk_sizes = ["paragraph", "half_a_paragraph", "quarter_a_paragraph", "sentence"]

chromadb_client = chromadb.HttpClient(
    host=os.getenv("CHROMADB_HOST", "chromadb"),
    port=8000,
    ssl=False,
    headers=None,
    settings=chromadb.config.Settings(),
    tenant=chromadb.config.DEFAULT_TENANT,
    database=chromadb.config.DEFAULT_DATABASE,
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

# Questions to ask about the text
f_query = open("../data/RAG_chunk_evaluation_questions.txt", "r")
my_queries = f_query.read().split("\n")
f_query.close()

unique_file_id = str(int(time.time()))

for chunk_size_desc in chunk_sizes:

    print(chunk_size_desc)

    # a file to store responses
    save_path = "evaluate_chunk_size_results"
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    f_response = open(
        save_path + "/response_" + unique_file_id + "_" + chunk_size_desc + ".txt", "w"
    )
    f_response.writelines([chunk_size_desc, "\n"])

    # read and chunk the text
    f = open("../data/chapterXX.txt", "r")
    chunk_sizes = ["paragraph", "half_a_paragraph", "quarter_a_paragraph", "sentence"]
    if chunk_size_desc == "paragraph":
        my_documents = f.read().split("\n")
        my_ids = [f"{uuid.uuid4().hex}" for _ in range(len(my_documents))]
    elif chunk_size_desc == "half_a_paragraph":
        my_documents_tmp = f.read().split("\n")
        my_documents = []
        for i in range(
            len(my_documents_tmp)
        ):  # Computationally heavy. Let's look for a python library.
            for c in range(2):
                half = len(my_documents_tmp[i]) // 2
                my_documents.append(my_documents_tmp[i][c * half : (c + 1) * half])
        my_ids = [f"{uuid.uuid4().hex}" for _ in range(len(my_documents))]
    elif chunk_size_desc == "quarter_a_paragraph":
        my_documents_tmp = f.read().split("\n")
        my_documents = []
        for i in range(
            len(my_documents_tmp)
        ):  # Computationally heavy. Let's look for a python library.
            for c in range(4):
                quarter = len(my_documents_tmp[i]) // 4
                my_documents.append(
                    my_documents_tmp[i][c * quarter : (c + 1) * quarter]
                )
        my_ids = [f"{uuid.uuid4().hex}" for _ in range(len(my_documents))]
    elif chunk_size_desc == "sentence":
        my_documents = f.read().split(".")
        my_ids = [f"{uuid.uuid4().hex}" for _ in range(len(my_documents))]
    else:  # split by space if nothing is specified. Just in case.
        my_documents = f.read().split(" ")
        my_ids = [f"{uuid.uuid4().hex}" for _ in range(len(my_documents))]
    f.close()

    # store in the database
    try:
        chromadb_client.get_collection(name=EMBEDDING_COLLECTION_NAME)
        chromadb_client.delete_collection(name=EMBEDDING_COLLECTION_NAME)
    except ValueError:
        pass

    learn_collection = chromadb_client.create_collection(
        name="learn",
    )

    learn_collection.add(
        documents=my_documents,
        ids=my_ids,
    )

    # ask questions
    my_queries_index = [i for i in range(len(my_queries))]
    for q, i in zip(my_queries, my_queries_index):

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
                    "content": "Please answer the question, with the following context as a hint.",
                },
                {"role": "system", "content": rag_result},
                {"role": "user", "content": q},  # Ask one question here.
            ],
        )

        # write answer responses to the file
        f_response.writelines(
            ["#############################################################", "\n"]
        )
        f_response.writelines(
            ["---------- Qeuestion " + str(i + 1) + " ----------", "\n"]
        )
        f_response.writelines([q, "\n"])
        f_response.writelines(
            ["---------- Retrieved text from the database ----------", "\n"]
        )
        f_response.writelines([rag_result, "\n"])
        f_response.writelines(["---------- Answer to the question ----------", "\n"])
        f_response.writelines([response.choices[0].message.content, "\n"])

        # show progress
        print(str(i + 1) + "/" + str(len(my_queries)))

    f_response.close()

print("done!")
