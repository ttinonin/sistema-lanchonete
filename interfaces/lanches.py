from abc import ABC, abstractmethod
from models.lanche import Lanche

class ILanchesRepository(ABC):
    """
    Repositorio abstrato para gerenciamento de lanches.

    Define operações essenciais de CRUD que devem ser implementadas.
    """
    @abstractmethod
    def criar(self, lanche: Lanche) -> Lanche:
        """
        Adiciona um novo lanche ao repositório.

        Parameters:
            lanche: instancia do modelo lanche.

        Returns:
            O lanche criado com ID persistido.
        """
        pass

    @abstractmethod
    def buscar_por_id(self, id) -> Lanche:
        """
        Retorna o lanche correspondente ao ID informado.

        Parameters:
            id: id do lanche a ser retornado

        Returns:
            O lanche solicitado se existir o ID.

        Raises:
            UnmappedInstanceError se o ID não existir.
        """
        pass

    @abstractmethod
    def listar(self):
        """
        Retorna todos os lanches.

        Returns:
            Lista de lanches completa.
        """
        pass

    @abstractmethod
    def atualizar(self, lanche: Lanche) -> Lanche:
        """
        Atualiza campos de um lanche especifico.

        Parameters:
            lanche: lanche a ser atualizado.

        Returns:
            Lanche atualizado.
        """
        pass

    @abstractmethod
    def deletar(self, id) -> Lanche:
        """
        Deleta um lanche especifico.

        Parameters:
            id: id do lanche a ser deletado

        Returns:
            Lanche deletado.

        Raises:
            UnmappedInstanceError se o ID não existir.
        """
        pass