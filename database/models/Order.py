from sqlalchemy import Column, Integer, Date, func, ForeignKey

from database.connection import Base


# Модель для таблицы "Orders".
class OrderModel(Base):
    __tablename__ = 'orders'

    # Внешние ключи на таблицы продуктов и партнеров
    fk_product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    fk_company_id = Column(Integer, ForeignKey('partners.id'), primary_key=True)

    # Поле для хранения количества товаров в заказе
    quantity_of_products = Column(Integer, nullable=False)

    # Поле для хранения даты создания заказа с автоматическим заполнением текущей датой
    date_of_create = Column(Date, default=func.current_date(), nullable=False)

    def __repr__(self):
        return (
            f"<Order(fk_product_name={self.fk_product_id}, fk_company_name='{self.fk_company_id}', "
            f"quantity_of_products={self.quantity_of_products}, date_of_create={self.date_of_create})>"
        )
