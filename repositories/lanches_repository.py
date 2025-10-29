from interfaces.lanches import ILanchesRepository
from models.lanche import Lanche
from models import db

class LanchesRepository(ILanchesRepository):
    def criar(self, lanche: Lanche) -> Lanche:
        db.session.add(lanche)
        db.session.commit()
        return lanche

    def buscar_por_id(self, id) -> Lanche:
        return db.session.get(Lanche, id)
    
    def listar(self):
        return db.session.query(Lanche).all()

    def atualizar(self, lanche: Lanche) -> Lanche:
        db.session.merge(lanche)
        db.session.commit()
        db.session.refresh(lanche)
        return lanche

    def deletar(self, id) -> Lanche:
        lanche = self.buscar_por_id(id)
        db.session.delete(lanche)
        db.session.commit()
        return lanche