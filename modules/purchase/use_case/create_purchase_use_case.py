from models.models import Status
from modules.purchase.repository import CreatePurchaseRepository
from modules.purchase.dto import CreatePurchaseDTO
from modules.user.repository import FindUserByIdRepository
from modules.tier.repository import FindTierByIdRepository
from modules.event.repository import FindEventByTierRepository
from fastapi import HTTPException


class CreatePurchaseUseCase:
    def __init__(self, repository=None, findUserByIdRepo=None, findTierByIdRepo=None, findEventByTierRepo=None):
        self.repository = repository or CreatePurchaseRepository()
        self.findUserByIdRepo = findUserByIdRepo or FindUserByIdRepository()
        self.findTierByIdRepo = findTierByIdRepo or FindTierByIdRepository()
        self.findEventByTierRepo = findEventByTierRepo or FindEventByTierRepository()

    def execute(self, data: CreatePurchaseDTO):
        """Executa o caso de uso para criar uma nova compra com seus itens.

        Args:
            data (CreatePurchaseDTO): DTO contendo dados da compra e itens.

        Raises:
            HTTPException: Se comprador, vendedor ou tier não existir, ou se houver erro.

        Returns:
            Purchase: Instância da Purchase criada com seus itens.
        """
        try:

            buyer = self.findUserByIdRepo.findById(data.buyerId)
            seller = self.findUserByIdRepo.findById(data.sellerId)
            processedItems = []

            if not buyer:
                raise HTTPException(status_code=404, detail=f"Comprador com ID {data.buyerId} não encontrado.")

            if not seller:
                raise HTTPException(status_code=404, detail=f"Vendedor com ID {data.sellerId} não encontrado.")

            for itemData in data.items:
                tier = self.findTierByIdRepo.findById(itemData.tierId)
                if not tier:
                    raise HTTPException(status_code=404, detail=f"Tier com ID {itemData.tierId} não encontrado.")
                
                event = self.findEventByTierRepo.findByTier(itemData.tierId)
                
                if event.status != Status.ACTIVE:
                    raise HTTPException(status_code=400, detail=f"Evento associado ao tier '{tier.name}' não está ativo: {event.name}.")
                
                if tier.amount < itemData.quantity:
                    raise HTTPException(
                        status_code=400, 
                        detail=f"Quantidade indisponível para o tier '{tier.name}'. Solicitado: {itemData.quantity}, Disponível: {tier.amount}"
                    )
                
                unitPrice = tier.price
                itemTotalPrice = unitPrice * itemData.quantity
                
                processedItems.append({
                    'tierId': itemData.tierId,
                    'quantity': itemData.quantity,
                    'unitPrice': unitPrice,
                    'totalPrice': itemTotalPrice,
                    'tier': tier
                })

            purchaseData = {
                'buyerId': data.buyerId,
                'sellerId': data.sellerId,
                'paymentMethod': data.paymentMethod,
                'status': data.status
            }

            itemsData = [
                {
                    'tierId': item['tierId'],
                    'quantity': item['quantity'],
                    'unitPrice': item['unitPrice'],
                    'totalPrice': item['totalPrice']
                }
                for item in processedItems
            ]

            createdPurchase = self.repository.createPurchaseWithItems(purchaseData, itemsData)

            print(f"Compra '{createdPurchase.id}' criada com status PENDING. Aguardando pagamento entre {buyer.name} e {seller.name}.")
            return createdPurchase
            
        except HTTPException as e:
            print(f"Erro ao registrar compra: {e.detail}")
            raise e
        except Exception as e:
            print(f"Erro ao registrar compra: {e}")
            raise HTTPException(status_code=500, detail="Erro interno do servidor ao criar compra.")
        finally:
            # Fechar sessões dos repositórios
            if hasattr(self.findUserByIdRepo, 'session'):
                self.findUserByIdRepo.session.close()
            if hasattr(self.findTierByIdRepo, 'session'):
                self.findTierByIdRepo.session.close()
