import os

from fastapi import FastAPI
from pydantic import BaseModel, Field
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY)

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
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": chat_request.message}],
    )
    return ChatResponse(message=response.choices[0].message.content)
