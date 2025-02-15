# Expense Prediction API

A backend application using FastAPI and machine learning to predict expenses and manage expense data.

## Features

- **Machine Learning Predictions**: Predicts future expenses based on historical data
- **CRUD Operations**: Complete expense data management
    - Create new expense records
    - Read existing expense data
    - Update expense information
    - Delete expense records

## Tech Stack

- FastAPI
- Python
- Machine Learning (Scikit-learn)
- SQLAlchemy
- SQLite

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
uvicorn main:app --reload
```
## API Documentation

Visit the API documentation at:
- Swagger UI: `http://localhost:8000/docs`

## API Endpoints

- `POST /pengeluaran/` - Create new expense
- `GET /pengeluaran/` - Get all expenses
- `GET /pengeluaran/{id}` - Get specific expense
- `PUT /pengeluaran/{id}` - Update expense
- `DELETE /pengeluaran/{id}` - Delete expense
- `POST /predict/regresi/` - Get expense prediction with regresi linier model
- `POST /predict/arima/` - Get expense prediction with arima model

## Project Structure

```
expense_predict/
├── env/
├── db/
|   └── expense_app.db
├── src/
│   ├── models/
│   ├── routes/
|   ├── ml/
│   └── main.py
└── README.md
```