from modules.seller import FindSellerByIdRepository

class FindSellerByIdUseCase:
    def __init__(self, repository=None):
        self.repository = repository or FindSellerByIdRepository()

    def execute(self, id: str):
        """        Executes the use case to find a seller by ID.

        Args:
            id (str): ID of the seller to be found.

        Raises:
            ValueError: If the seller with the given ID does not exist.
            e: Exception raised during the search process.

        Returns:
            _type_: Seller model instance if found, None if not found.
        """
        try:
            seller = self.repository.findById(id)
            if not seller:
                raise ValueError(f"Vendedor não encontrado.")
            return seller
        except Exception as e:
            print(f"Erro ao buscar vendedor: {e}")
            raise e
        finally:
            self.repository.session.close()
