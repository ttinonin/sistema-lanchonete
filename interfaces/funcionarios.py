from abc import ABC, abstractmethod
from models.funcionario import Funcionario

class IFuncionariosRepository(ABC):
    """
    Repositorio abstrato para gerenciamento de funcionarios.

    Define operações essenciais de CRUD que devem ser implementadas.
    """
    @abstractmethod
    def criar(funcionario: Funcionario) -> Funcionario:
        """
        Adiciona um novo funcionário ao repositório.

        Parameters:
            funcionario: instancia do modelo Funcionário.

        Returns:
            O funcionário criado com ID persistido.
        """
        pass

    @abstractmethod
    def buscar_por_id(id) -> Funcionario:
        """
        Retorna o funcionário correspondente ao ID informado.

        Parameters:
            id: id do funcionario a ser retornado

        Returns:
            O funcionário solicitado se existir o ID.

        Raises:
            ValueError se o ID não existir.
        """
        pass

    @abstractmethod
    def listar():
        """
        Retorna todos os funcionarios.

        Returns:
            Lista de funcionarios completa.
        """
        pass

    @abstractmethod
    def atualizar(funcionario: Funcionario) -> Funcionario:
        """
        Atualiza campos de um funcionario especifico.

        Returns:
            Funcionario atualizado.
        """
        pass

    @abstractmethod
    def deletar(id) -> Funcionario:
        """
        Deleta um funcionario especifico.

        Returns:
            Funcionario deletado.

        Raises:
            ValueError se o ID não existir.
        """
        pass