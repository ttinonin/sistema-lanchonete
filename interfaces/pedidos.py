from abc import ABC, abstractmethod
from models.pedido import Pedido

class IPedidosRepository(ABC):
    """
    Repositorio abstrato para gerenciamento de pedidos.

    Define operações essenciais de CRUD que devem ser implementadas.
    """
    @abstractmethod
    def criar(self, pedido: Pedido) -> Pedido:
        """
        Adiciona um novo pedido ao repositório.

        Parameters:
            pedido: instancia do modelo pedido.

        Returns:
            O pedido criado com ID persistido.
        """
        pass

    @abstractmethod
    def buscar_por_id(self, id) -> Pedido:
        """
        Retorna o pedido correspondente ao ID informado.

        Parameters:
            id: id do pedido a ser retornado

        Returns:
            O pedido solicitado se existir o ID.

        Raises:
            UnmappedInstanceError se o ID não existir.
        """
        pass

    @abstractmethod
    def listar(self):
        """
        Retorna todos os pedidos.

        Returns:
            Lista de pedidos completa.
        """
        pass

    @abstractmethod
    def atualizar(self, pedido: Pedido) -> Pedido:
        """
        Atualiza campos de um pedido especifico.

        Parameters:
            pedido: pedido a ser atualizado.

        Returns:
            Pedido atualizado.
        """
        pass

    @abstractmethod
    def deletar(self, id) -> Pedido:
        """
        Deleta um pedido especifico.

        Parameters:
            id: id do pedido a ser deletado

        Returns:
            Pedido deletado.

        Raises:
            UnmappedInstanceError se o ID não existir.
        """
        pass