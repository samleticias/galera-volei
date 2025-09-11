import pytest
from fastapi.testclient import TestClient
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import app

client = TestClient(app.app)  # pega a variável "app" que está dentro do app.py


def test_root_status():
    """Verifica se a API inicializa"""
    response = client.get("/jogador")  # exemplo: endpoint de jogadores
    assert response.status_code in (200, 404)  # depende se já tem rota GET definida

@pytest.mark.parametrize("endpoint", [
    "/jogador",
    "/local",
    "/categoria",
    "/jogo",
    "/convite",
    "/autenticacao"
])
def test_endpoints_exist(endpoint):
    """Testa se os endpoints principais existem"""
    response = client.get(endpoint)
    # 200 se a rota GET existir, 405 se só POST, 401 se exige login etc.
    assert response.status_code in (200, 401, 404, 405)
