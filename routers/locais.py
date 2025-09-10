from fastapi import APIRouter, HTTPException
from typing import List
from schemas import Local, LocalBase

router = APIRouter()
locais_db: List[Local] = []

@router.get("/", response_model=List[Local])
def listar_locais():
    return locais_db

@router.post("/", response_model=Local, status_code=201)
def criar_local(local: LocalBase):
    novo = Local(id=str(len(locais_db)+1), **local.dict())
    locais_db.append(novo)
    return novo

@router.patch("/{id}", response_model=Local)
def editar_local(id: str, local: LocalBase):
    for l in locais_db:
        if l.id == id:
            l.nome = local.nome
            l.descricao = local.descricao
            l.endereco = local.endereco
            l.valor_hora = local.valor_hora
            return l
    raise HTTPException(status_code=404, detail="Local não encontrado")

@router.get("/{id}", response_model=Local)
def detalhar_local(id: str):
    for l in locais_db:
        if l.id == id:
            return l
    raise HTTPException(status_code=404, detail="Local não encontrado")