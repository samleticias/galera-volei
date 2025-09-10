# API Galera do Vôlei - FastAPI

## Documentação da API: [docs](https://github.com/samleticias/galera-volei/blob/main/tabela-api-volei.pdf)

## Endpoints

### Jogadores

- GET /jogador → Listar jogadores

- POST /jogador → Registrar jogador

- PATCH /jogador/{id} → Editar jogador

### Locais

- GET /local → Listar locais
- POST /local → Criar local
- PATCH /local/{id} → Editar local
- GET /local/{id} → Detalhar local

### Categorias

- GET /categoria → Listar categorias
- POST /categoria → Criar categoria
- PATCH /categoria/{id} → Editar categoria

### Jogos

- GET /jogo → Listar jogos
- POST /jogo → Criar jogo
- POST /jogo/{id}/convidar → Convidar jogadores
- POST /jogo/{id}/cancelar → Cancelar jogo
- POST /jogo/{id}/ingressar → Jogador ingressar em jogo
- POST /jogo/{id}/desistir → Jogador desistir do jogo
- POST /jogo/{id}/avaliar → Avaliar jogo
- PATCH /jogo/{id} → Editar jogo
- GET /jogo/{id} → Detalhar jogo

### Convites

- GET /convite → Obter convites
- PATCH /convite/{id} → Responder convite

### Autenticação

- POST /autenticacao/registrar → Registrar usuário
- POST /autenticacao/entrar → Entrar com email e senha
