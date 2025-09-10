from fastapi import APIRouter, HTTPException
from typing import List
from schemas import Convite, ConviteBase

router = APIRouter()
convites_db: List[Convite] = []

@router.get("/", response_model=List[Convite])
def listar_convites():
    return convites_db

@router.patch("/{id}", response_model=Convite)
def responder_convite(id: str, status: dict):
    for c in convites_db:
        if c.id == id:
            c.status = status["status"]
            return c
    raise HTTPException(status_code=404, detail="Convite não encontrado")