# Ramses Polese Xavier Dos Santos
from fastapi import APIRouter
from domain.entities.Produto import Produto
import db
from infra.orm.ProdutoModel import ProdutoDB

router = APIRouter()

# Criar as rotas/endpoints: GET, POST, PUT, DELETE

@router.get("/produto/", tags=["Produto"])
async def get_produtos():
    try:
        session = db.Session()
        # Busca todos os produtos
        dados = session.query(ProdutoDB).all()
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.get("/produto/{id}", tags=["Produto"])
async def get_produto(id: int):
    try:
        session = db.Session()
        # Busca um produto pelo ID
        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).one_or_none()
        if dados is None:
            return {"erro": "Produto não encontrado"}, 400
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.post("/produto/", tags=["Produto"])
async def post_produto(corpo: Produto):
    try:
        session = db.Session()

        # Criar um novo objeto corretamente
        dados = ProdutoDB(
            nome=corpo.nome,
            descricao=corpo.descricao,  # Adicionado o campo descricao
            valor_unitario=corpo.valor_unitario
        )

        session.add(dados)
        session.commit()
        session.refresh(dados)  # Garante que o ID gerado seja retornado corretamente

        
        return {"id": dados.id_produto}, 200
    
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()
        
@router.put("/produto/{id}", tags=["Produto"])
async def put_produto(id: int, corpo: Produto):
    try:
        session = db.Session()
        # busca os dados atuais pelo id
        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).one()
        # atualiza os dados com base no corpo da requisição
        dados.nome = corpo.nome
        dados.descricao = corpo.descricao
        dados.valor_unitario = corpo.valor_unitario
        session.add(dados)
        session.commit()
        
        return {"id": dados.id_produto}, 200
        
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()
        
@router.delete("/produto/{id}", tags=["Produto"])
async def delete_produto(id: int):
    try:
        session = db.Session()
        produto = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).first()

        if not produto:
            return {"erro": "Produto não encontrado"}, 404

        session.delete(produto)
        session.commit()
        return {"mensagem": "Produto deletado com sucesso"}, 200

    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()
