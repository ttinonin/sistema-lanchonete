from abc import ABC, abstractmethod
from models.funcionario import Funcionario

class IFuncionariosRepository(ABC):
    """
    Repositorio abstrato para gerenciamento de funcionarios.

    Define operações essenciais de CRUD que devem ser implementadas.
    """
    @abstractmethod
    def criar(self, funcionario: Funcionario) -> Funcionario:
        """
        Adiciona um novo funcionário ao repositório.

        Parameters:
            funcionario: instancia do modelo Funcionário.

        Returns:
            O funcionário criado com ID persistido.
        """
        pass

    @abstractmethod
    def buscar_por_id(self, id) -> Funcionario:
        """
        Retorna o funcionário correspondente ao ID informado.

        Parameters:
            id: id do funcionario a ser retornado

        Returns:
            O funcionário solicitado se existir o ID.

        Raises:
            UnmappedInstanceError se o ID não existir.
        """
        pass

    @abstractmethod
    def listar(self):
        """
        Retorna todos os funcionarios.

        Returns:
            Lista de funcionarios completa.
        """
        pass

    @abstractmethod
    def atualizar(self, funcionario: Funcionario) -> Funcionario:
        """
        Atualiza campos de um funcionario especifico.

        Parameters:
            funcionario: Funcionario a ser atualizado

        Returns:
            Funcionario atualizado.
        """
        pass

    @abstractmethod
    def deletar(self, id) -> Funcionario:
        """
        Deleta um funcionario especifico.

        Parameters:
            id: id do funcionario a ser deletado

        Returns:
            Funcionario deletado.

        Raises:
            UnmappedInstanceError se o ID não existir.
        """
        pass