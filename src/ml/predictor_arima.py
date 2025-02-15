import pandas as pd
import numpy as np
from datetime import datetime
from statsmodels.tsa.arima.model import ARIMA
from sqlalchemy.orm import Session
from ..models.database import SessionLocal
from ..models.pengeluaran import Pengeluaran

def train_model():
    # Ambil data dari database
    db: Session = SessionLocal()
    data = db.query(Pengeluaran).all()
    db.close()

    if not data or len(data) < 7:  # Minimal 7 hari data
        return None

    # Convert ke DataFrame
    df = pd.DataFrame([{
        "jml_pengeluaran": d.jml_pengeluaran,
        "tgl": d.tgl
    } for d in data])

    # Sort berdasarkan tanggal
    df = df.sort_values('tgl')
    
    # Set index ke tanggal
    df.set_index('tgl', inplace=True)
    
    # Resample ke frekuensi harian dan isi missing values dengan 0
    daily_expenses = df['jml_pengeluaran'].resample('D').sum().fillna(0)
    
    try:
        # Train model ARIMA (p,d,q) = (1,1,1) sebagai default parameter
        model = ARIMA(daily_expenses, order=(1, 1, 1))
        fitted_model = model.fit()
        return fitted_model
    except:
        return None

def predict_expense(date):
    model = train_model()
    if model is None:
        return {"message": "Data pengeluaran tidak cukup untuk prediksi"}

    today = datetime.now()
    days_ahead = (date - today).days

    if days_ahead < 1:
        return {"message": "Tanggal harus di masa depan untuk prediksi"}

    try:
        # Prediksi untuk n hari ke depan
        forecast = model.forecast(steps=days_ahead)
        predicted_value = max(0, float(forecast.iloc[-1]))  # Ambil prediksi hari terakhir
        
        # Hitung confidence interval
        confidence_interval = model.get_forecast(days_ahead).conf_int().iloc[-1]
        
        return {
            "predicted_expense": predicted_value,
            "confidence_interval": {
                "lower": max(0, float(confidence_interval[0])),
                "upper": float(confidence_interval[1])
            }
        }
    except Exception as e:
        return {"message": f"Error dalam prediksi: {str(e)}"}