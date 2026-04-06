from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, database
from pydantic import BaseModel

app = FastAPI()

# Cria as tabelas no banco de dados automaticamente se não existirem
models.Base.metadata.create_all(bind=database.engine)

# Dependência para obter a conexão com o banco
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Modelo para receber dados do Frontend (Pydantic)
class ItemCreate(BaseModel):
    nome: str
    P_12: int
    descricao_item: str
    medidas: str
    acabamento: str

@app.post("/itens/")
def cadastrar_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {"status": "sucesso", "item_id": db_item.id}

@app.get("/itens/")
def listar_itens(db: Session = Depends(get_db)):
    return db.query(models.Item).all()