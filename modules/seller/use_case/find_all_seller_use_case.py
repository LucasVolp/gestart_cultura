from modules.seller import FindAllSellersRepository

class FindAllSellerUseCase:
    def __init__(self, repository=None):
        self.repository = repository or FindAllSellersRepository()

    def execute(self):
        """        Executes the use case to find all sellers.

        Raises:
            e: Exception if an error occurs during the operation.

        Returns:
            _type_: List of Seller model instances.
        """
        try: 
            sellers = self.repository.findAll()
            if not sellers:
                print("Nenhum vendedor encontrado.")
                return []
            return sellers
        except Exception as e:
            print(f"Erro ao buscar vendedores: {e}")
            raise e
        finally:
            self.repository.session.close()
