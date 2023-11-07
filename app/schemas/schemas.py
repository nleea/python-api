from typing import List, Optional
from pydantic import BaseModel, Field


class ZipCodeSchema(BaseModel):
    zip_code: str = Field(default=None, title="Zip Code", max_length=5, min_length=5)
    valid: bool = Field(
        default=True,
        title="Valid",
    )
    city: str = Field(default=None, title="County", max_length=255)
    state: str = Field(default=None, title="State", max_length=2)
    county: str = Field(default=None, title="County", max_length=255)
    timezone: str = Field(default=None, title="Timezone", max_length=255)
    area_codes: List[str]
    country: str = Field(default=None, title="Zip Code", max_length=2)
    lat: float
    lon: float


class ZipCodeBD(ZipCodeSchema):
    id: int
