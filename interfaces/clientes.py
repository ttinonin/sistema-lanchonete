from abc import ABC, abstractmethod
from models.cliente import Cliente

class IClientesRepository(ABC):
    """
    Repositorio abstrato para gerenciamento de clientes.

    Define operações essenciais de CRUD que devem ser implementadas.
    """
    @abstractmethod
    def criar(self, cliente: Cliente) -> Cliente:
        """
        Adiciona um novo cliente ao repositório.

        Parameters:
            cliente: instancia do modelo cliente.

        Returns:
            O cliente criado com ID persistido.
        """
        pass

    @abstractmethod
    def buscar_por_id(self, id) -> Cliente:
        """
        Retorna o cliente correspondente ao ID informado.

        Parameters:
            id: id do cliente a ser retornado

        Returns:
            O cliente solicitado se existir o ID.

        Raises:
            UnmappedInstanceError se o ID não existir.
        """
        pass

    @abstractmethod
    def listar(self):
        """
        Retorna todos os clientes.

        Returns:
            Lista de clientes completa.
        """
        pass

    @abstractmethod
    def atualizar(self, cliente: Cliente) -> Cliente:
        """
        Atualiza campos de um cliente especifico.

        Parameters:
            cliente: cliente a ser atualizado.

        Returns:
            Cliente atualizado.
        """
        pass

    @abstractmethod
    def deletar(self, id) -> Cliente:
        """
        Deleta um cliente especifico.

        Parameters:
            id: id do cliente a ser deletado

        Returns:
            Cliente deletado.

        Raises:
            UnmappedInstanceError se o ID não existir.
        """
        pass