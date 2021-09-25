from fastapi import FastAPI, Depends
from schemas import ingresar_empresa, ingresar_producto
from sqlalchemy.orm import Session
from database import get_db
from models import Producto, Empresa

app = FastAPI()


@app.post("/a/")
def create(details_product: ingresar_producto, db: Session = Depends(get_db)):
    to_create = Producto(
        name=details_product.name,
        description=details_product.description
    )
    db.add(to_create)
    db.commit()
    return{
        "success": True,
        "created_id": to_create.id
    }

@app.post("/b/")
def create(details_empresa: ingresar_empresa, db: Session = Depends(get_db)):
    to_create_empresa = Empresa(
        name=details_empresa.name
    )
    db.add(to_create_empresa)
    db.commit()
    return{
        "success": True,
        "created_id": to_create_empresa.id
    }