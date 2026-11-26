from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from Services.product_service import get_all_products
from Schemas.product_schema import ProductResponse

router = APIRouter(
    prefix="/store/products",
    tags=["Products"]
)


@router.get("/", response_model=list[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return get_all_products(db)