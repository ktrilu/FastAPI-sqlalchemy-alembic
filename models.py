from sqlalchemy import String, Integer
from sqlalchemy import Column
from sqlalchemy.sql.traversals import COMPARE_FAILED
from database import Base

class Producto(Base):
    __tablename__ = 'Productos'
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = True)
    description = Column(String, nullable = True)

class Empresa(Base):
    __tablename__ = 'Empresas'
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = True)

