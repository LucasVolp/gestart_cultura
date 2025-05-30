from modules.seller import FindSellerByIdRepository

class FindSellerByIdUseCase:
    def __init__(self, repository=None):
        self.repository = repository or FindSellerByIdRepository()

    def execute(self, id: int):
        try:
            seller = self.repository.findById(id)
            if not seller:
                raise ValueError(f"Vendedor com ID {id} não encontrado.")
            return seller
        except Exception as e:
            print(f"Erro ao buscar vendedor: {e}")
            raise e
        finally:
            self.repository.session.close()
