from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from ..models.database import SessionLocal
from ..models.pengeluaran import Pengeluaran
from .pengeluaran_schema import PengeluaranSchema

router = APIRouter()

# Dependency untuk mendapatkan session database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/pengeluaran/", response_model=PengeluaranSchema)
def create_pengeluaran(data: PengeluaranSchema, db: Session = Depends(get_db)):
    pengeluaran = Pengeluaran(**data.dict())
    db.add(pengeluaran)
    db.commit()
    db.refresh(pengeluaran)
    return pengeluaran

@router.get("/pengeluaran/{pengeluaran_id}", response_model=PengeluaranSchema)
def read_pengeluaran(pengeluaran_id: int, db: Session = Depends(get_db)):
    pengeluaran = db.query(Pengeluaran).filter(Pengeluaran.id == pengeluaran_id).first()
    if pengeluaran is None:
        raise HTTPException(status_code=404, detail="Pengeluaran tidak ditemukan")
    return pengeluaran

@router.get("/pengeluaran/", response_model=list[PengeluaranSchema])
def read_all_pengeluaran(db: Session = Depends(get_db)):
    return db.query(Pengeluaran).all()

@router.put("/pengeluaran/{pengeluaran_id}", response_model=PengeluaranSchema)
def update_pengeluaran(pengeluaran_id: int, data: PengeluaranSchema, db: Session = Depends(get_db)):
    pengeluaran = db.query(Pengeluaran).filter(Pengeluaran.id == pengeluaran_id).first()
    if pengeluaran is None:
        raise HTTPException(status_code=404, detail="Pengeluaran tidak ditemukan")

    for key, value in data.dict().items():
        setattr(pengeluaran, key, value)

    db.commit()
    db.refresh(pengeluaran)
    return pengeluaran

@router.delete("/pengeluaran/{pengeluaran_id}")
def delete_pengeluaran(pengeluaran_id: int, db: Session = Depends(get_db)):
    pengeluaran = db.query(Pengeluaran).filter(Pengeluaran.id == pengeluaran_id).first()
    if pengeluaran is None:
        raise HTTPException(status_code=404, detail="Pengeluaran tidak ditemukan")

    db.delete(pengeluaran)
    db.commit()
    return {"message": "Pengeluaran berhasil dihapus"}