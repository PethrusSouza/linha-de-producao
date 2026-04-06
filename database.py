from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Substitua com seus dados: usuario:senha@localhost/nome_do_banco
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:senha@localhost/sistema_os"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()