from pydantic import BaseModel
from typing import Optional, List, Dict

# ---------------------- Jogador ----------------------
class JogadorBase(BaseModel):
    nome: str
    sexo: str
    idade: str
    nivel_habilidade: str
    avatar: str
    email: Optional[str] = None

class Jogador(JogadorBase):
    id: str

# ---------------------- Local ----------------------
class LocalBase(BaseModel):
    nome: str
    descricao: str
    endereco: str
    valor_hora: str

class Local(LocalBase):
    id: str

# ---------------------- Categoria ----------------------
class CategoriaBase(BaseModel):
    nome: str
    descricao: str
    faixa_etaria: str
    genero: str
    nivel_habilidade: str
    numero_jogadores: Dict[str, int]

class Categoria(CategoriaBase):
    id: str

# ---------------------- Jogo ----------------------
class JogoBase(BaseModel):
    id_local: str
    data: str
    id_categoria: str
    quantidade_horas: int
    acesso: str

class Jogo(JogoBase):
    id: str
    status: str
    jogadores: List[Jogador] = []
    nota: Optional[int] = 0
    avaliacoes: Optional[List[Dict[str, str]]] = []

# ---------------------- Convite ----------------------
class ConviteBase(BaseModel):
    jogo: str
    convidado: str
    anfitriao: str
    status: str
    data: str

class Convite(ConviteBase):
    id: str

# ---------------------- Autenticação ----------------------
class Login(BaseModel):
    email: str
    senha: str

class Registrar(JogadorBase):
    senha: str