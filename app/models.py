from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(description="The message to be sent to the chatbot")


class ChatResponse(BaseModel):
    message: str = Field(description="The message to be responded by the chatbot")


class LearnRequest(BaseModel):
    text: str = Field(description="The text to be learned by the chatbot")


class BMIRequest(BaseModel):
    # FIXME: Add min and max values to the fields
    # FIXME: Add a description about units (cm, kg)
    weight: float = Field(description="Weight value requested to calculate BMI.")
    height: float = Field(description="Height value requested to calculate BMI.")


class BMIResponse(BaseModel):
    bmi: float = Field(description="BMI value to be responded by the chatbot")
