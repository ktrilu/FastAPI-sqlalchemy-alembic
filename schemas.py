from database import Base
from alembic.op import create_table
from pydantic import BaseModel

class ingresar_producto(BaseModel):
    name: str
    description: str

class ingresar_empresa(BaseModel):
    name: str