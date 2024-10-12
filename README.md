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
RAG is a method that tries to avoid hallucination by using information pre-stored in a database. 

### How does RAG work?

0. Context texts are loaded into the database. They are embedded so that it is easier to search for the most relevant information.
1. A **user asks a question** (inputs a query)
2. The query is embedded and most related **contexts are retrieved** from the database. The distance between the embedded query and the embedded context determines the similarity between the query and the contexts.
3. The k most related contexts(in text) are combined with the user's query(in text) to **generate a better question** (query in text) to feed to an LLM. Better question: a question that includes the context and asks to say "I don't know" if the information is not present in the context.
4. The query generated from the last step is fed to an LLM model, and the **LLM model gives the user an answer based on the query** from the last step. The user receives this answer.

<p align="center">
<img width="1225" alt="Screenshot 2024-10-12 at 02 27 44" src="https://github.com/user-attachments/assets/bf6537c6-d50e-45cc-bb2f-caac0f3d90fe">
</p>

<p align="center">
Figure 1. Flow of how RAG works
</p>
