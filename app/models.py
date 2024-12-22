from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(description="The message to be sent to the chatbot")


class ChatResponse(BaseModel):
    message: str = Field(description="The message to be responded by the chatbot")


class LearnRequest(BaseModel):
    text: str = Field(min_length=4, description="The text to be learned by the chatbot")


class BMIRequest(BaseModel):
    weight: float = Field(
        ge=0, description="Weight value [kg] requested to calculate BMI."
    )
    height: float = Field(
        ge=0, description="Height value [cm] requested to calculate BMI."
    )


class BMIResponse(BaseModel):
    bmi: float = Field(description="BMI value to be responded by the chatbot")
