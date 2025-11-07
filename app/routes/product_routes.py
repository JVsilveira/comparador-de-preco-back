from fastapi import APIRouter, Query
from app.services.services_product import search_mercado_livre

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/")
def get_products(query: str = Query(...)):
    produtos = search_mercado_livre(query)
    return {"count": len(produtos), "results": produtos}