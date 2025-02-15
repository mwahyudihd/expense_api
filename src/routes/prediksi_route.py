from fastapi import APIRouter
from datetime import datetime
from ..ml.predictor_arima import predict_expense as arima_predict_expense
from ..ml.predictor_linier import predict_expense as reg_predict_expense

router = APIRouter()

@router.get("/predict/regresi/")
def get_reg_prediction(date: str):
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        return reg_predict_expense(date_obj)
    except ValueError:
        return {"error": "Format tanggal harus YYYY-MM-DD"}

@router.get("/predict/arima/")
def get_arima_prediction(date: str):
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        return arima_predict_expense(date_obj)
    except ValueError:
        return {"error": "Format tanggal harus YYYY-MM-DD"}