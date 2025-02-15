from sqlalchemy import Column, Integer, Float, String, DateTime
from .database import Base

class Pengeluaran(Base):
    __tablename__ = "pengeluaran"

    id = Column(Integer, primary_key=True, index=True)
    jml_pengeluaran = Column(Float, nullable=False)
    kategori = Column(String, index=True)
    catatan = Column(String, nullable=True)
    tgl = Column(DateTime, nullable=False)