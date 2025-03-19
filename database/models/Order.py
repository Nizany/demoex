from sqlalchemy import Column, Integer, Date, func, ForeignKey

from database.connection import Base


class Order(Base):
    __tablename__ = 'orders'

    fk_product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    fk_company_id = Column(Integer, ForeignKey('partners.id'), primary_key=True)
    amount_of_products = Column(Integer, nullable=False)
    date_of_create = Column(Date, default=func.current_date(), nullable=False)
