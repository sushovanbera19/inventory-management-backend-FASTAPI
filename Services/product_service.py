from sqlalchemy.orm import Session
from Models.product_model import Product


def get_all_products(db: Session):
    products = (
        db.query(Product)
        .filter(Product.status == "active")
        .all()
    )

    return products