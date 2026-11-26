from sqlalchemy.orm import Session
from sqlalchemy import func
import uuid

from Models.category_model import Category
from Models.product_model import Product



def get_all_admin_categories(db: Session):

    categories = db.query(Category).all()

    result = []

    for category in categories:

        # Count products belonging to this category
        product_count = (
            db.query(func.count(Product.id))
            .filter(Product.category_id == category.id)
            .scalar()
        )

        # Calculate total stock units
        total_units = (
            db.query(func.coalesce(func.sum(Product.stock), 0))
            .filter(Product.category_id == category.id)
            .scalar()
        )

        # Calculate total stock value using cost price
        stock_value = (
            db.query(
                func.coalesce(
                    func.sum(Product.stock * Product.cost_price), 0
                )
            )
            .filter(Product.category_id == category.id)
            .scalar()
        )

        result.append({
            "id": category.id,
            "name": category.name,
            "description": category.description,
            "color": category.color,
            "imageUrl": category.image_url,
            "createdAt": category.created_at,
            "updatedAt": category.updated_at,
            "productCount": product_count,
            "totalUnits": total_units,
            "stockValue": float(stock_value)
        })

    return result


# POST: Create a new category
def create_admin_category(db: Session, category_data):

    new_category = Category(
        id=f"cat_{uuid.uuid4().hex[:8]}",
        name=category_data.name,
        description=category_data.description,
        color=category_data.color,
        image_url=category_data.imageUrl
    )

    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category