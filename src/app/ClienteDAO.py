# Ramses Polese Xavier Dos Santos
from fastapi import APIRouter
from domain.entities.Cliente import Cliente
import db
from infra.orm.ClienteModel import ClienteDB

router = APIRouter()

# Criar as rotas/endpoints: GET, POST, PUT, DELETE

@router.get("/cliente/", tags=["Cliente"])
async def get_clientes():
    try:
        session = db.Session()
        # Busca todos os clientes
        dados = session.query(ClienteDB).all()
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.get("/cliente/{id}", tags=["Cliente"])
async def get_cliente(id: int):
    try:
        session = db.Session()
        # Busca um cliente pelo ID
        dados = session.query(ClienteDB).filter(ClienteDB.id_cliente == id).one_or_none()
        if dados is None:
            return {"erro": "Cliente não encontrado"}, 400
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.post("/cliente/", tags=["Cliente"])
async def post_cliente(corpo: Cliente):
    try:
        session = db.Session()
        # Cria um novo objeto ClienteDB SEM o ID
        dados = ClienteDB(
            nome=corpo.nome,
            cpf=corpo.cpf,
            telefone=corpo.telefone
        )
        session.add(dados)
        session.commit()
        return {"id": dados.id_cliente}, 200  # O ID gerado será retornado corretamente
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.put("/cliente/{id}", tags=["Cliente"])
async def put_cliente(id: int, corpo: Cliente):
    try:
        session = db.Session()
        # Busca o cliente pelo ID
        dados = session.query(ClienteDB).filter(ClienteDB.id_cliente == id).one_or_none()
        if dados is None:
            return {"erro": "Cliente não encontrado"}, 400
        # Atualiza os dados do cliente com base no corpo da requisição
        dados.nome = corpo.nome
        dados.cpf = corpo.cpf
        dados.telefone = corpo.telefone
        session.add(dados)
        session.commit()
        return {"id": dados.id_cliente}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.delete("/cliente/{id}", tags=["Cliente"])
async def delete_cliente(id: int):
    try:
        session = db.Session()
        # Busca o cliente pelo ID
        dados = session.query(ClienteDB).filter(ClienteDB.id_cliente == id).one_or_none()
        if dados is None:
            return {"erro": "Cliente não encontrado"}, 400
        session.delete(dados)
        session.commit()
        return {"id": dados.id_cliente}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()
