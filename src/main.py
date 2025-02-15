from fastapi import FastAPI
from src.routes.pengeluaran_routes import router as pengeluaran_router
from src.routes import prediksi_route

app = FastAPI()

app.include_router(pengeluaran_router)
app.include_router(prediksi_route.router)

@app.get("/")
def root():
    return {"message": "Welcome to Expense Tracker API"}