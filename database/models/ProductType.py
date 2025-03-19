from sqlalchemy import Column, Integer, String, Float

from database.connection import Base


class ProductType(Base):
    __tablename__ = 'product_type'

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(50), nullable=False)
    coefficient_of_product_type = Column(Float, nullable=False)