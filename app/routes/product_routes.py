from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import ProductCreateSchema, ProductSchema
from app.crud import crud_product as crud
from app.core.database import get_db

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

@router.post("/", response_model=ProductSchema)
def create_product(product: ProductCreateSchema, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@router.get("/", response_model=list[ProductSchema])
def list_products(db: Session = Depends(get_db)):
    return crud.get_products(db)