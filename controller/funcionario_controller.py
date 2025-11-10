from repositories.funcionarios_repository import FuncionariosRepository
from models.funcionario import Funcionario
from werkzeug.security import generate_password_hash, check_password_hash

class FuncionarioController:
    def __init__(self):
        self.repo = FuncionariosRepository()
    
    def criar(self, nome: str, email: str, senha: str, senha_confirm: str):
        if senha != senha_confirm:
            raise ValueError("Senhas nao coincidem!")
        if len(senha) < 3:
            raise ValueError("Senha deve possuir 3 caracteres!")
        if not nome or not email or not senha:
            raise ValueError("Preencher todos os campos!")
        
        senha_hash = generate_password_hash(senha)
        funcionario = Funcionario(nome=nome, email=email, senha=senha_hash)
        self.repo.criar(funcionario)

    def listar(self):
        return self.repo.listar()
    
    def deletar(self, id: int):
        return self.repo.deletar(id)
    
    def login(self, email: str, senha: str):
        funcionario = self.repo.buscar_por_email(email)

        if not funcionario:
            raise ValueError("Usuario não encontrado!")
        
        if not check_password_hash(funcionario.senha, senha):
            raise ValueError("Email ou senha incorretos!")
        
        return funcionario