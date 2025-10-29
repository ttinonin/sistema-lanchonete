from interfaces.bebidas import IBebidasRepository
from models.bebida import Bebida
from models import db

class BebidasRepository(IBebidasRepository):
    def criar(self, bebida: Bebida) -> Bebida:
        db.session.add(bebida)
        db.session.commit()
        return bebida

    def buscar_por_id(self, id) -> Bebida:
        return db.session.get(Bebida, id)
    
    def listar(self):
        return db.session.query(Bebida).all()

    def atualizar(self, bebida: Bebida) -> Bebida:
        db.session.merge(bebida)
        db.session.commit()
        db.session.refresh(bebida)
        return bebida

    def deletar(self, id) -> Bebida:
        bebida = self.buscar_por_id(id)
        db.session.delete(bebida)
        db.session.commit()
        return bebida