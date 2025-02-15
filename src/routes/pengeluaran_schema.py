from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PengeluaranSchema(BaseModel):
    jml_pengeluaran: float
    kategori: str
    catatan: Optional[str] = None
    tgl: datetime

    class Config:
        orm_mode = True