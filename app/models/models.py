from sqlalchemy import Column, Integer, String, Boolean, JSON, DECIMAL
from .base import Base


class ZipCode(Base):
    __tablename__ = "zip_codes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    zip_code = Column(String(5), nullable=False, unique=True)
    valid = Column(Boolean, nullable=False)
    city = Column(String(255), nullable=False)
    state = Column(String(2), nullable=False)
    county = Column(String(255), nullable=False)
    timezone = Column(String(255), nullable=False)
    area_codes = Column(JSON, nullable=False)
    country = Column(String(2), nullable=False)
    lat = Column(DECIMAL, nullable=False)
    lon = Column(DECIMAL, nullable=False)
