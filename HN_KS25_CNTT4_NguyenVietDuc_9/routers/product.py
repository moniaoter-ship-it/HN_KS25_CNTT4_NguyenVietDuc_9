from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.product import ProductCreate
from services.products_service import (
    create_product,
    delete_product,
    get_products,
)

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("")
def read_products(db: Session = Depends(get_db)):
    return get_products(db)


@router.post("")
def add_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
):
    return create_product(db, product)


@router.delete("/{product_id}")
def remove_product(
    product_id: int,
    db: Session = Depends(get_db),
):
    return delete_product(db, product_id)
