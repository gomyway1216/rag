from fastapi import APIRouter

from app.models import BMIRequest, BMIResponse


router = APIRouter()


@router.post("/bmi", response_model=BMIResponse, status_code=200)
def bmi(bmi_request: BMIRequest):
    weight = bmi_request.weight
    height = bmi_request.height
    bmi = round(weight / ((height / 100) ** 2), 2)
    return BMIResponse(bmi=bmi)
