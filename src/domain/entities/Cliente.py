#Ramses Polese Xavier Dos Santos
from pydantic import BaseModel

class Cliente(BaseModel):
    id_cliente: int = None
    nome: str
    cpf: str
    telefone: str