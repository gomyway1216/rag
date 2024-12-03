# RAG

## Overview

This project implements a Retrieval-Augmented Generation (RAG) system. It consists of an API server built with FastAPI and a vector database (ChromaDB) that stores embeddings and performs vector search.

## System Components

- **API Server (FastAPI)**
	- Serves API endpoints to clients for simple Q&A.
- **Vector Database (ChromaDB)**
	- Stores embeddings and performs vector-based searches for similarity matching.

## Running Locally

```bash
$ docker compose build  # build docker images
$ docker compose up  # run docker containers
```

### Accessing ChromaDB API

Once the server is up, you can visit [http://localhost:8001/docs](http://localhost:8001/docs) to check the ChromaDB API Documentation.

## Adding Dependencies

```bash
$ poetry add {library_name}
```

## RAG
One of the problems with state-of-the-art LLM models is hallucination; the model returns inaccurate/incorrect answers. 
RAG is a method that tries to avoid hallucination by using information that is pre-stored in a database. 

### How does RAG work?

0. Embeddings of context texts are loaded into the database. The texts are embedded for the similarity search in later steps.
1. A **user asks a question** (inputs a query).
2. **k most related contexts to the query are retrieved** from the database. The distance between the embedded query and the embedded context determines the similarity between the query and the contexts.
3. The k most related contexts(in text) are combined with the user's query(in text) to make a better prompt. It may simply be a **concatenation of the query and contexts with additional prompts**. Some works add prompts to respond "I don't know" if the information is not present in the context to minimize hallucinations.
4. The better prompt made in the last step is fed to the LLM model, and the **LLM model gives the user an answer** based on the better prompt. The user receives this answer.

<p align="center">
 	<img width="800" alt="Screenshot 2024-12-03 at 01 44 00" src="https://github.com/user-attachments/assets/e52de7cb-b8b5-4840-9f17-f5ef99f2a403">
</p>

<p align="center">
Figure 1. The RAG architecture
</p>
