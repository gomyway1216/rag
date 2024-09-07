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
