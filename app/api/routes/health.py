# health information

import os

import chromadb
from fastapi import APIRouter
from openai import OpenAI

from app.models import BMIRequest, BMIResponse


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
    weight = bmi_request.weight
    height = bmi_request.height
    bmi = round(weight / ((height / 100) ** 2), 2)
    return BMIResponse(bmi=bmi)
