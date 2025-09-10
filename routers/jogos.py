from fastapi import APIRouter, HTTPException
from typing import List
from schemas import Jogo, JogoBase, Jogador

router = APIRouter()
jogos_db: List[Jogo] = []

@router.get("/", response_model=List[Jogo])
def listar_jogos():
    return jogos_db

@router.post("/", response_model=Jogo, status_code=201)
def criar_jogo(jogo: JogoBase):
    novo = Jogo(id=str(len(jogos_db)+1), status="ativo", jogadores=[], avaliacoes=[], **jogo.dict())
    jogos_db.append(novo)
    return novo

@router.post("/{id}/convidar")
def convidar_jogadores(id: str, ids: List[str]):
    for j in jogos_db:
        if j.id == id:
            return {"msg": "Jogadores convidados", "jogo": j.id, "convidados": ids}
    raise HTTPException(status_code=404, detail="Jogo não encontrado")

@router.post("/{id}/cancelar")
def cancelar_jogo(id: str):
    for j in jogos_db:
        if j.id == id:
            j.status = "cancelado"
            return {"msg": "Jogo cancelado"}
    raise HTTPException(status_code=404, detail="Jogo não encontrado")

@router.post("/{id}/ingressar", response_model=Jogo)
def ingressar_jogo(id: str, jogador: Jogador):
    for j in jogos_db:
        if j.id == id:
            j.jogadores.append(jogador)
            return j
    raise HTTPException(status_code=404, detail="Jogo não encontrado")

@router.post("/{id}/desistir")
def desistir_jogo(id: str, jogador: Jogador):
    for j in jogos_db:
        if j.id == id:
            j.jogadores = [x for x in j.jogadores if x.id != jogador.id]
            return {"msg": f"{jogador.nome} desistiu do jogo"}
    raise HTTPException(status_code=404, detail="Jogo não encontrado")

@router.post("/{id}/avaliar")
def avaliar_jogo(id: str, avaliacao: dict):
    for j in jogos_db:
        if j.id == id:
            j.avaliacoes.append(avaliacao)
            return {"msg": "Avaliação registrada"}
    raise HTTPException(status_code=404, detail="Jogo não encontrado")

@router.get("/{id}", response_model=Jogo)
def detalhar_jogo(id: str):
    for j in jogos_db:
        if j.id == id:
            return j
    raise HTTPException(status_code=404, detail="Jogo não encontrado")