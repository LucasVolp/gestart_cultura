from modules.purchase.repository import UpdatePurchaseRepository, FindPurchaseByIdRepository
from modules.purchase.dto import UpdatePurchaseDTO
from modules.user.repository import FindUserByIdRepository
from fastapi import HTTPException

class UpdatePurchaseUseCase:
    def __init__(self, repository=None, findPurchaseByIdRepo=None, findUserById=None):
        self.repository = repository or UpdatePurchaseRepository()
        self.findPurchaseByIdRepo = findPurchaseByIdRepo or FindPurchaseByIdRepository()
        self.findUserById = findUserById or FindUserByIdRepository()

    def execute(self, id: str, data: UpdatePurchaseDTO):
        """Updates a purchase using the provided DTO.

        Args:
            id (str): The ID of the purchase to update.
            data (UpdatePurchaseDTO): Data transfer object for updating a purchase.

        Returns:
            Purchase: The updated Purchase object.

        Raises:
            HTTPException: If the purchase is not found, users don't exist, or an error occurs.
        """
        try:
            purchaseExists = self.findPurchaseByIdRepo.findById(id)
            if not purchaseExists:
                raise HTTPException(status_code=404, detail=f"Compra com ID {id} não encontrada.")

            if data.buyerId is not None:
                buyer = self.findUserById.findById(data.buyerId)
                if not buyer:
                    raise HTTPException(status_code=404, detail=f"Comprador com ID {data.buyerId} não encontrado.")
             
            if data.sellerId is not None:
                seller = self.findUserById.findById(data.sellerId)
                if not seller:
                    raise HTTPException(status_code=404, detail=f"Vendedor com ID {data.sellerId} não encontrado.")

            if data.isEmpty():
                raise HTTPException(status_code=400, detail="Nenhum dado fornecido para atualização.")
            

            purchase = self.repository.update(purchaseExists, data)
            print(f"Compra {purchase.id} atualizada com sucesso.")
            return purchase
            
        except HTTPException as e:
            print(f"Erro ao atualizar compra: {e.detail}")
            raise e
        except Exception as e:
            print(f"Erro ao atualizar compra: {e}")
            raise HTTPException(status_code=500, detail="Erro interno do servidor ao atualizar compra.")
        finally:
            self.repository.session.close()
            self.findPurchaseByIdRepo.session.close()
            if hasattr(self.findUserById, 'session'):
                self.findUserById.session.close()
            self.findPurchaseByIdRepo.session.close()
