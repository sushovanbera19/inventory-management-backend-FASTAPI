from sqlalchemy.orm import Session

from Models.category_model import Category


def get_all_categories(db: Session):

    categories = db.query(Category).all()

    result = []

    for category in categories:

        # Generate slug from category name
        slug = category.name.lower()
        slug = slug.replace("&", "and")
        slug = slug.replace(" ", "-")

        result.append({
            "id": category.id,
            "name": category.name,
            "slug": slug,
            "description": category.description,
            "color": category.color,
            "imageUrl": category.image_url,
            "productCount": 0,
            "startingPrice": 0
        })

    return result