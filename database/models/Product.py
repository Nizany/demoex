from sqlalchemy import Column, Integer, String, Float, ForeignKey

from database.connection import Base


# Модель для таблицы "Products".
class ProductModel(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Уникальный идентификатор продукта
    article = Column(String(10), nullable=False)  # Артикул продукта
    name = Column(String(200), nullable=False)  # Название продукта
    min_cost = Column(Float, nullable=False)  # Минимальная стоимость продукта
    fk_type = Column(Integer, ForeignKey('product_type.id'), nullable=False)  # Внешний ключ на тип продукта

    def __repr__(self):
        return (
            f"<Product(id={self.id}, article='{self.article}', name='{self.name}', "
            f"min_cost={self.min_cost}, fk_type={self.fk_type})>"
        )
