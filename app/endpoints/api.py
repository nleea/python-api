from typing import Any, List, Dict, Tuple
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends
from ..utils import get
from ..enviroment import API_KEY
from ..schemas import ZipCodeSchema, ZipCodeBD
from fastapi.responses import JSONResponse
from .deps import get_db
from ..crud import api_crud

router = APIRouter()


@router.get("", response_model=Dict[str, List[ZipCodeSchema]])
def get_data_external(
    state: str = "OR",
) -> Dict[str, List[Dict[Any, Any]] | Any]:
    try:
        rep = get(f"zipcode?state={state}", API_KEY)
        return JSONResponse({"response": rep}, 200)
    except HTTPException as e:
        raise HTTPException(status_code=404, detail=e)


@router.get("/all", response_model=Dict[str, List[ZipCodeBD]])
def get_data(
    db: Session = Depends(get_db),
) -> Dict[str, List[Dict[Any, Any]] | Any]:
    try:
        rep = api_crud.get_all(db=db)
        return {"response": rep}
    except Exception as e:
        return e.args


@router.post("", response_model=ZipCodeBD | Tuple)
def save_data(
    *,
    db: Session = Depends(get_db),
    data: ZipCodeSchema,
):
    exist = api_crud.get_zip_code(db=db, zip_code=data.zip_code)

    if exist:
        raise HTTPException(
            status_code=400,
            detail="Info con this zip_code already exist.",
        )
    try:
        rep = api_crud.create(db, obj_in=data)
        return rep
    except Exception as e:
        return e.args


@router.get("/{id}", response_model=Dict[str, ZipCodeBD | str])
def get_data_id(
    *,
    db: Session = Depends(get_db),
    id: int,
):
    item = api_crud.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"response": item}
