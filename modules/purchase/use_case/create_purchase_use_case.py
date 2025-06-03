from modules.purchase.repository import CreatePurchaseRepository
from modules.purchase.dto import CreatePurchaseDTO
from modules.user.repository import FindUserByIdRepository
from fastapi import HTTPException


class CreatePurchaseUseCase:
    def __init__(self, repository=None, findUserById=None):
        self.repository = repository or CreatePurchaseRepository()
        self.findUserById = findUserById or FindUserByIdRepository()

    def execute(self, data: CreatePurchaseDTO):
        """Executes the use case to create a new purchase.

        Args:
            data (CreatePurchaseDTO): Data Transfer Object containing the purchase information to be created.

        Raises:
            HTTPException: If buyer or seller doesn't exist, or if an error occurs during creation.

        Returns:
            Purchase: Created Purchase model instance.
        """
        try:
            buyer = self.findUserById.findById(data.buyerId)
            if not buyer:
                raise HTTPException(status_code=404, detail=f"Comprador com ID {data.buyerId} não encontrado.")

            seller = self.findUserById.findById(data.sellerId)
            if not seller:
                raise HTTPException(status_code=404, detail=f"Vendedor com ID {data.sellerId} não encontrado.")
            if seller.role != "SELLER":
                raise HTTPException(status_code=400, detail="O Vendedor selecionado não é um vendedor válido.")
            purchase = self.repository.create(data)
            print(f"Compra '{purchase.id}' realizada com sucesso entre {buyer.name} e {seller.name}.")
            return purchase
            
        except HTTPException as e:
            print(f"Erro ao registrar compra: {e.detail}")
            raise e
        except Exception as e:
            print(f"Erro ao registrar compra: {e}")
            raise HTTPException(status_code=500, detail="Erro interno do servidor ao criar compra.")
        finally:
            self.repository.session.close()
            if hasattr(self.findUserById, 'session'):
                self.findUserById.session.close()
