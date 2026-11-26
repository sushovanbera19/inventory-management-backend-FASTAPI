from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from Services.admin_category_service import (
    get_all_admin_categories,
    create_admin_category
)

from Schemas.admin_category_schema import (
    AdminCategoryCreate,
    AdminCategoryResponse
)

router = APIRouter(
    prefix="/categories",
    tags=["Admin Categories"]
)


# GET: Fetch all categories
@router.get("/", response_model=list[AdminCategoryResponse])
def get_admin_categories(db: Session = Depends(get_db)):

    return get_all_admin_categories(db)


# POST: Create a new category
@router.post("/", response_model=AdminCategoryResponse, status_code=201)
def create_category(
    category_data: AdminCategoryCreate,
    db: Session = Depends(get_db)
):

    return create_admin_category(db, category_data)