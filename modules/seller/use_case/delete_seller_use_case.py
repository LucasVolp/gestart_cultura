from modules.seller import DeleteSellerRepository, FindSellerByIdRepository

class DeleteSellerUseCase:
    def __init__(self, repository=None, findSellerByID=None):
        self.repository = repository or DeleteSellerRepository()
        self.findSellerByID = findSellerByID or FindSellerByIdRepository()
    def execute(self, id: int):
        try:
            seller = self.findSellerByID.findById(id)
            if not seller:
                raise ValueError("Seller not found")
            return self.repository.delete(id)
        except Exception as e:
            print(f"Error deleting seller: {e}")
            raise e
        finally:
            self.repository.session.close()
