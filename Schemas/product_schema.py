from pydantic import BaseModel, ConfigDict
from typing import Optional
from decimal import Decimal
from datetime import datetime


class ProductResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    sku: str
    name: str
    slug: str
    description: Optional[str] = None
    category_id: Optional[str] = None
    unit: Optional[str] = None
    price: Decimal
    compare_at_price: Optional[Decimal] = None
    stock: int
    image_url: Optional[str] = None
    rating: Decimal
    review_count: int
    sold_count: int
    status: str
    created_at: Optional[datetime] = None