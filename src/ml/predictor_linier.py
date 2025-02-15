import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sqlalchemy.orm import Session
from ..models.database import SessionLocal
from ..models.pengeluaran import Pengeluaran

def train_model():
    db: Session = SessionLocal()
    data = db.query(Pengeluaran).all()
    db.close()

    if not data:
        return None

    df = pd.DataFrame([{
        "jml_pengeluaran": d.jml_pengeluaran,
        "tgl": d.tgl.timestamp()  # Konversi datetime ke timestamp
    } for d in data])

    X = df["tgl"].values.reshape(-1, 1)
    y = df["jml_pengeluaran"].values

    model = LinearRegression()
    model.fit(X, y)

    return model

def predict_expense(date):
    model = train_model()
    if model is None:
        return {"message": "Data pengeluaran tidak cukup untuk prediksi"}

    date_timestamp = date.timestamp()
    prediction = model.predict(np.array([[date_timestamp]]))
    
    return {"predicted_expense": prediction[0]}