from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import Base, engine
from app.routes import product_routes
import app.models

# Cria a instância principal do FastAPI
app = FastAPI(
    title="Comparador de Preços",
    version="1.0.0"
)

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cria as tabelas do banco (caso ainda não existam)
Base.metadata.create_all(bind=engine)

# Inclui as rotas
app.include_router(product_routes.router)
