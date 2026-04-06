from sqlalchemy import Column, Integer, String, Enum, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import relationship
from database import Base

# 1. Modelo para cad_usuarios
class Usuario(Base):
    __tablename__ = "cad_usuarios"
    
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    funcao = Column(String(50))
    nivel_acesso = Column(Enum('ADMIM', 'GERENTE', 'OPERADOR'), nullable=False)
    usuario = Column(String(50), unique=True, nullable=False)
    senha = Column(String(100), nullable=False)

# 2. Modelo para cad_clientes (Baseado no seu arquivo corrigido)
class Cliente(Base):
    __tablename__ = "cad_clientes"
    
    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    nome_cliente = Column(String(100), nullable=False, unique=True)
    cnpj = Column(String(20))
    endereco = Column(String(50))
    
    # Relacionamento: Um cliente pode ter várias ordens de serviço
    ordens = relationship("OrdemServico", back_populates="cliente")

# 3. Modelo para cad_itens
class Item(Base):
    __tablename__ = "cad_itens"
    
    id_item = Column(Integer, primary_key=True, autoincrement=True) # ID para facilitar busca
    nome = Column(String(100), nullable=False)
    P_12 = Column(Integer)
    descricao_item = Column(String(300), nullable=False)
    medidas = Column(Enum('BL', 'TL', 'M²', 'CM'))
    acabamento = Column(String(300), nullable=False)

# 4. Modelo para Ordem_servico
class OrdemServico(Base):
    __tablename__ = "Ordem_servico"
    
    num_pedido = Column(String(20), primary_key=True)
    nome_cliente = Column(String(100), ForeignKey("cad_clientes.nome_cliente"), nullable=False)
    status_geral = Column(
        Enum('EM_PRODUCAO', 'FINALIZADA', 'NF_EMITIDA', 'ENTREGUE'),
        server_default=text("'EM_PRODUCAO'")
    )
    data_criacao = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    
    # Relacionamento: A ordem pertence a um cliente específico
    cliente = relationship("Cliente", back_populates="ordens")