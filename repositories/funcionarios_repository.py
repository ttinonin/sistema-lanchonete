from interfaces.funcionarios import IFuncionariosRepository
from models.funcionario import Funcionario
from models import db

class FuncionariosRepository(IFuncionariosRepository):
    def criar(self, funcionario: Funcionario) -> Funcionario:
        db.session.add(funcionario)
        db.session.commit()
        return funcionario

    def buscar_por_id(self, id) -> Funcionario:
        return db.session.get(Funcionario, id)
    
    def listar(self):
        return db.session.query(Funcionario).all()

    def atualizar(self, funcionario: Funcionario) -> Funcionario:
        db.session.merge(funcionario)
        db.session.commit()
        db.session.refresh(funcionario)
        return funcionario

    def deletar(self, id) -> Funcionario:
        funcionario = self.buscar_por_id(id)
        db.session.delete(funcionario)
        db.session.commit()
        return funcionario