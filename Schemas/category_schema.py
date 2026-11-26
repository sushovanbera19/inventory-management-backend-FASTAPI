from pydantic import BaseModel


class CategoryResponse(BaseModel):
    id: str
    name: str
    slug: str
    description: str | None = None
    color: str | None = None
    imageUrl: str | None = None
    productCount: int = 0
    startingPrice: float = 0

    class Config:
        from_attributes = True