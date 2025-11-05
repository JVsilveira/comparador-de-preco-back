from fastapi import FastAPI
from app.core.database import Base, engine
from app.routes import product_routes

import app.models  

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Comparador de Preços",
    version="1.0.0"
)

app.include_router(product_routes.router)