from sqlalchemy import Column, Integer, String

from database.connection import Base


# Модель для таблицы "Partners".
class PartnerModel(Base):
    __tablename__ = 'partners'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Уникальный идентификатор партнера
    type = Column(String(10), nullable=False)  # Тип партнера
    company_name = Column(String(100), nullable=False)  # Название компании
    address = Column(String(100), nullable=False)  # Адрес компании
    inn = Column(String, nullable=False)  # ИНН компании
    boss_name = Column(String(50), nullable=False)  # Имя руководителя
    phone_number = Column(String(30), nullable=True)  # Контактный номер телефона
    mail = Column(String(100), nullable=True)  # Электронная почта
    rank = Column(Integer, nullable=False)  # Рейтинг партнера

    def __repr__(self):
        return (
            f"<Partner(id={self.id}, type='{self.type}', company_name='{self.company_name}', address='{self.address}', "
            f"inn='{self.inn}', boss_name='{self.boss_name}', phone_number='{self.phone_number}', mail='{self.mail}', "
            f"rank='{self.rank}')>"
        )
