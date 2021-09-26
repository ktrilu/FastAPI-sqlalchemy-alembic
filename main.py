from fastapi import FastAPI, Depends
from schemas import ingresar_empresa, ingresar_producto
from sqlalchemy.orm import Session
from database import get_db
from models import Producto, Empresa

app = FastAPI()


@app.post("/a/{itemname}/{itemdesc}")
def create(itemname,itemdesc, db: Session = Depends(get_db)):
    to_create = Producto(
        name=itemname,
        description=itemdesc
    )
    db.add(to_create)
    db.commit()
    return{
        "success": True,
        "created_id": to_create.id
    }

@app.post("/b/{itemname}")
def create(itemname, db: Session = Depends(get_db)):
    to_create_empresa = Empresa(
        name=itemname
    )
    db.add(to_create_empresa)
    db.commit()
    return{
        "success": True,
        "created_id": to_create_empresa.id
    }