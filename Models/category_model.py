from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.sql import func

from database import Base


class Category(Base):

    __tablename__ = "categories"

    id = Column(String(50), primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    color = Column(String(30), nullable=True)
    image_url = Column(String(500), nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )