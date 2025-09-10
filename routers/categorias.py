from fastapi import APIRouter, HTTPException
from typing import List
from schemas import Categoria, CategoriaBase

router = APIRouter()
categorias_db: List[Categoria] = []

@router.get("/", response_model=List[Categoria])
def listar_categorias():
    return categorias_db

@router.post("/", response_model=Categoria, status_code=201)
def criar_categoria(cat: CategoriaBase):
    nova = Categoria(id=str(len(categorias_db)+1), **cat.dict())
    categorias_db.append(nova)
    return nova

@router.patch("/{id}", response_model=Categoria)
def editar_categoria(id: str, cat: CategoriaBase):
    for c in categorias_db:
        if c.id == id:
            c.nome = cat.nome
            c.descricao = cat.descricao
            c.faixa_etaria = cat.faixa_etaria
            c.genero = cat.genero
            c.nivel_habilidade = cat.nivel_habilidade
            c.numero_jogadores = cat.numero_jogadores
            return c
    raise HTTPException(status_code=404, detail="Categoria não encontrada")