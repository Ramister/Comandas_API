#Ramses Polese Xavier Dos Santos

import db
from sqlalchemy import Column, VARCHAR, DECIMAL, Integer,BLOB
#ORM
class ProdutoDB(db.Base):
    __tablename__='tb_produto'
    id_produto=Column(Integer,primary_key=True,autoincrement=True,index=True)
    nome=Column(VARCHAR(100),nullable=False,index=True)
    descricao=Column(VARCHAR(200),nullable=False)
    foto=Column(BLOB,nullable=True)
    valor_unitario=Column(DECIMAL(11,2),nullable=False)

    def __init__(self,nome,descricao,valor_unitario,foto=None):
        self.nome=nome
        self.descricao=descricao
        self.valor_unitario=valor_unitario
        self.foto=foto