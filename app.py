from fastapi import FastAPI
from routers import jogadores, locais, categorias, jogos, convites, autenticacao

app = FastAPI(title="API Vôlei")

app.include_router(jogadores.router, prefix="/jogador", tags=["Jogadores"])
app.include_router(locais.router, prefix="/local", tags=["Locais"])
app.include_router(categorias.router, prefix="/categoria", tags=["Categorias"])
app.include_router(jogos.router, prefix="/jogo", tags=["Jogos"])
app.include_router(convites.router, prefix="/convite", tags=["Convites"])
app.include_router(autenticacao.router, prefix="/autenticacao", tags=["Autenticação"])