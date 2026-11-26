
from sqlalchemy import (
    Column,
    String,
    Text,
    Integer,
    Numeric,
    DateTime,
    ForeignKey
)
from sqlalchemy.sql import func
from database import Base


class Product(Base):
    __tablename__ = "products"

    # Basic product information
    id = Column(String(50), primary_key=True, index=True)
    sku = Column(String(100), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    slug = Column(String(255), unique=True, nullable=False)
    description = Column(Text, nullable=True)

    # Category relationship
    category_id = Column(
        String(50),
        ForeignKey("categories.id"),
        nullable=True
    )

    supplier_id = Column(String(50), nullable=True)

    # Pricing information
    unit = Column(String(50), nullable=True)
    cost_price = Column(Numeric(12, 2), nullable=False, default=0)
    price = Column(Numeric(12, 2), nullable=False, default=0)
    compare_at_price = Column(Numeric(12, 2), nullable=True)

    # Inventory information
    stock = Column(Integer, nullable=False, default=0)
    reorder_level = Column(Integer, nullable=False, default=0)
    reorder_qty = Column(Integer, nullable=False, default=0)
    location = Column(String(100), nullable=True)
    barcode = Column(String(100), nullable=True)

    # Product display information
    image_url = Column(String(1000), nullable=True)
    status = Column(String(30), nullable=False, default="active")

    # Product statistics
    rating = Column(Numeric(3, 2), nullable=False, default=0)
    review_count = Column(Integer, nullable=False, default=0)
    sold_count = Column(Integer, nullable=False, default=0)

    # Timestamps
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
