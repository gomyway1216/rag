from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(description="The message to be sent to the chatbot")


class ChatResponse(BaseModel):
    message: str = Field(description="The message to be responded by the chatbot")


class LearnRequest(BaseModel):
    text: str = Field(description="The text to be learned by the chatbot")
