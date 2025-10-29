from abc import ABC, abstractmethod
from models.bebida import Bebida

class IBebidasRepository(ABC):
    """
    Repositorio abstrato para gerenciamento de bebidas.

    Define operações essenciais de CRUD que devem ser implementadas.
    """
    @abstractmethod
    def criar(self, bebida: Bebida) -> Bebida:
        """
        Adiciona uma nova bebida ao repositório.

        Parameters:
            bebida: instancia do modelo bebida.

        Returns:
            A bebida criado com ID persistido.
        """
        pass

    @abstractmethod
    def buscar_por_id(self, id) -> Bebida:
        """
        Retorna a bebida correspondente ao ID informado.

        Parameters:
            id: id da bebida a ser retornado

        Returns:
            A bebida solicitado se existir o ID.

        Raises:
            UnmappedInstanceError se o ID não existir.
        """
        pass

    @abstractmethod
    def listar(self):
        """
        Retorna todos as bebidas.

        Returns:
            Lista de bebidas completa.
        """
        pass

    @abstractmethod
    def atualizar(self, bebida: Bebida) -> Bebida:
        """
        Atualiza campos de uma bebida especifico.

        Parameters:
            bebida: bebida a ser atualizada.

        Returns:
            Bebida atualizada.
        """
        pass

    @abstractmethod
    def deletar(self, id) -> Bebida:
        """
        Deleta uma bebida especifico.

        Parameters:
            id: id da bebida a ser deletado

        Returns:
            Bebida deletada.

        Raises:
            UnmappedInstanceError se o ID não existir.
        """
        pass