# health information

import os
import uuid

import chromadb
from fastapi import APIRouter
from openai import OpenAI

from app.models import LearnRequest, BMIRequest, BMIResponse


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
learn_collection = chromadb_client.get_or_create_collection(
    name="learn",
)


router = APIRouter()


@router.post("/bmi", response_model=BMIResponse, status_code=200)
def bmi(bmi_request: BMIRequest):
    print("request received")
    weight = bmi_request.weight
    height = bmi_request.height
    bmi = round(weight / ((height / 100) ** 2), 2)
    print(bmi)
    bmi_result_message = "Your BMI is " + str(bmi) + "."
    return BMIResponse(message=bmi_result_message)


@router.post("/learn", status_code=204)
def learn(learn_request: LearnRequest):
    learn_collection.add(
        documents=[learn_request.text],
        ids=[uuid.uuid4().hex],
    )
    return
