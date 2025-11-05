from sqlalchemy.orm import Session
from datetime import datetime
from app.models import Product, PriceHistory
from app.schemas import ProductCreateSchema

def create_product(db: Session, product: ProductCreateSchema):
    db_product = Product(
        title=product.title,
        link=product.link,
        image=product.image,
        current_price=product.current_price,
        target_price=product.target_price
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Product).offset(skip).limit(limit).all()

def add_price_history(db: Session, product_id: int, price: float):
    history = PriceHistory(
        product_id=product_id,
        price=price,
        date=datetime.utcnow()
    )
    db.add(history)
    db.commit()
    db.refresh(history)
    return history
