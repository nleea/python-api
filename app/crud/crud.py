from sqlalchemy.orm import Session
from ..models.models import ZipCode
from .base import CRUDBase
from ..schemas.schemas import ZipCodeSchema


class CRUDAPI(CRUDBase[ZipCode, ZipCodeSchema]):
    def create(self, db: Session, *, obj_in: ZipCodeSchema) -> ZipCode:
        """
        The create() method creates a new ZipCode object in the database. It takes the following arguments:

            db: A SQLAlchemy session object.
            obj_in: A ZipCodeSchema object representing the ZipCode object to create.

        return ZipCode
        """
        db_obj = ZipCode(
            zip_code=obj_in.zip_code,
            valid=obj_in.valid,
            city=obj_in.city,
            state=obj_in.state,
            county=obj_in.county,
            timezone=obj_in.timezone,
            area_codes=obj_in.area_codes,
            country=obj_in.country,
            lat=obj_in.lat,
            lon=obj_in.lon,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


api_crud = CRUDAPI(ZipCode)
