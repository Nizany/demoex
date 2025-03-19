from sqlalchemy import Column, Integer, String, Float

from database.connection import Base


class Material(Base):
    __tablename__ = 'materials'

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(50), nullable=False)
    percentage_of_defective_material = Column(Float, nullable=False)
