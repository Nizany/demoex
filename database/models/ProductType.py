from sqlalchemy import Column, Integer, String, Float

from database.connection import Base


# Модель для таблицы "ProductType".
class ProductTypeModel(Base):
    __tablename__ = 'product_type'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Уникальный идентификатор типа продукта
    type = Column(String(50), nullable=False)  # Название типа продукта
    coefficient_of_product_type = Column(Float, nullable=False)  # Коэффициент, связанный с типом продукта

    def __repr__(self):
        return (
            f"<ProductType(id={self.id}, type='{self.type}', "
            f"coefficient_of_product_type={self.coefficient_of_product_type})>"
        )
