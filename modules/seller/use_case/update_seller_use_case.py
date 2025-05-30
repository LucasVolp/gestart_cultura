from modules.seller import UpdateSellerRepository, UpdateSellerDTO, FindSellerByIdRepository

class UpdateSellerUseCase:
    def __init__(self, repository=None, findSellerById=None):
        self.repository = repository or UpdateSellerRepository()
        self.findSellerById = findSellerById or FindSellerByIdRepository()

    def execute(self, id: str, data: UpdateSellerDTO):
        """        Executes the use case to update a seller's information by ID.

        Args:
            id (str): ID of the seller to be updated.
            data (UpdateSellerDTO): Data transfer object containing the updated seller information.

        Raises:
            ValueError: If the seller with the given ID does not exist.
            e: Exception raised during the update process.

        Returns:
            _type_: Updated Seller model instance if successful, None if not found.
        """
        try:
            sellerExists = self.findSellerById.findById(id)
            if not sellerExists:
                raise ValueError("Vendedor não encontrado.")
            seller = self.repository.update(sellerExists, data)
            print(f"Seller {seller.name} updated successfully.")
            return seller
        except Exception as e:
            print(f"Error updating seller: {e}")
            raise e
        finally:
            self.repository.session.close()
