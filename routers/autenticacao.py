from fastapi import APIRouter, HTTPException
from schemas import Login, Registrar, Jogador
from typing import List

router = APIRouter()
usuarios_db: List[Registrar] = []

@router.post("/registrar", response_model=Jogador, status_code=201)
def registrar(user: Registrar):
    novo = Jogador(id=str(len(usuarios_db)+1), **user.dict())
    usuarios_db.append(user)
    return novo

@router.post("/entrar")
def login(login: Login):
    for u in usuarios_db:
        if u.email == login.email and u.senha == login.senha:
            return {"msg": "Login realizado com sucesso"}
    raise HTTPException(status_code=401, detail="Credenciais inválidas")