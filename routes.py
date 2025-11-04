from fastapi import APIRouter
from services import search_mercado_livre
from models import Product
from pymongo import MongoClient
from datetime import datetime

router = APIRouter()
client = MongoClient("mongodb://localhost:27017/")
db = client.detector

@router.get("/search")
def search_product(q: str):
    return search_mercado_livre(q)

@router.post("/track")
def track_product(product: Product):
    prod_id = db.products.insert_one(product.dict()).inserted_id
    db.price_history.insert_one({
        "product_id": str(prod_id),
        "price": product.current_price,
        "date": datetime.utcnow()
    })
    return {"message": "Produto adicionado ao monitoramento", "id": str(prod_id)}

@router.get("/history/{product_id}")
def get_history(product_id: str):
    history = list(db.price_history.find({"product_id": product_id}))
    for h in history:
        h["_id"] = str(h["_id"])
    return history