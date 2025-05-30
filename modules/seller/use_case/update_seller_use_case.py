from modules.seller import UpdateSellerRepository, UpdateSellerDTO, FindSellerByIdRepository

class UpdateSellerUseCase:
    def __init__(self, repository=None, findSellerById=None):
        self.repository = repository or UpdateSellerRepository()
        self.findSellerById = findSellerById or FindSellerByIdRepository()

    def execute(self, id: int, data: UpdateSellerDTO):
        try:
            sellerExists = self.findSellerById.findById(id)
            if not sellerExists:
                raise ValueError(f"Vendedor não encontrado.")
            seller = self.repository.update(id, data)
            print(f"Vendedor {seller.name} atualizado com sucesso.")
            return seller
        except Exception as e:
            print(f"erro ao atualizar vendedor {e}")
            raise e
        finally:
            self.repository.session.close()
