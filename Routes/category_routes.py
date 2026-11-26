from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from Services.category_service import get_all_categories
from Schemas.category_schema import CategoryResponse


router = APIRouter(
    prefix="/store/categories",
    tags=["Categories"]
)


@router.get("/", response_model=list[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):

    categories = get_all_categories(db)

    return categories