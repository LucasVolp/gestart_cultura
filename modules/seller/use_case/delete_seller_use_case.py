from modules.seller import DeleteSellerRepository, FindSellerByIdRepository

class DeleteSellerUseCase:
    def __init__(self, repository=None, findSellerByID=None):
        self.repository = repository or DeleteSellerRepository()
        self.findSellerByID = findSellerByID or FindSellerByIdRepository()
    def execute(self, id: str):
        """        Executes the use case to delete a seller by ID.

        Args:
            id (str): ID of the seller to be deleted.

        Raises:
            ValueError: If the seller with the given ID does not exist.
            e: Exception raised during the deletion process.

        Returns:
            _type_: Deleted Seller model instance if successful, None if not found.
        """
        try:
            sellerExists = self.findSellerByID.findById(id)
            if not sellerExists:
                raise ValueError("Vendedor não encontrado.")
            seller = self.repository.delete(sellerExists)
            if seller:
                print(f"Vendedor {sellerExists.name} deletado com sucesso.")
            return seller
        except Exception as e:
            print(f"Error deleting seller: {e}")
            raise e
        finally:
            self.repository.session.close()
