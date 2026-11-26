from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime


# Data received when creating a category
class AdminCategoryCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: Optional[str] = None
    color: Optional[str] = "indigo"
    imageUrl: Optional[str] = None


# Data received when updating a category
class AdminCategoryUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=100)
    description: Optional[str] = None
    color: Optional[str] = None


# Data returned to the admin frontend
class AdminCategoryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    description: Optional[str] = None
    color: Optional[str] = None
    imageUrl: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

    productCount: int = 0
    totalUnits: int = 0
    stockValue: float = 0