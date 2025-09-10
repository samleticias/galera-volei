from fastapi import APIRouter, HTTPException
from typing import List
from schemas import Jogador, JogadorBase

router = APIRouter()
jogadores_db: List[Jogador] = []

@router.get("/", response_model=List[Jogador])
def listar_jogadores():
    return jogadores_db

@router.post("/", response_model=Jogador, status_code=201)
def registrar_jogador(jogador: JogadorBase):
    novo = Jogador(id=str(len(jogadores_db)+1), **jogador.dict())
    jogadores_db.append(novo)
    return novo

@router.patch("/{id}", response_model=Jogador)
def editar_jogador(id: str, jogador: JogadorBase):
    for j in jogadores_db:
        if j.id == id:
            j.nome = jogador.nome
            j.sexo = jogador.sexo
            j.idade = jogador.idade
            j.nivel_habilidade = jogador.nivel_habilidade
            j.avatar = jogador.avatar
            j.email = jogador.email
            return j
    raise HTTPException(status_code=404, detail="Jogador não encontrado")