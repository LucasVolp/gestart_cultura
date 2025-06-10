from uuid import UUID
from fastapi import HTTPException
from models.models import PaymentStatus, Status
from modules.event.repository.find_event_by_tier_repository import FindEventByTierRepository
from modules.purchase.repository import FindPurchaseByIdRepository, UpdatePurchaseRepository
from modules.receipt.repository.create_receipt_repository import CreateReceiptRepository
from modules.ticket.repository.create_ticket_repository import CreateTicketRepository
from modules.user.repository import FindUserByIdRepository
from modules.user.repository import UpdateUserRepository
from modules.user.dto.update_user_dto import UpdateUserDTO
from modules.purchase.dto import UpdatePurchaseDTO
from modules.receipt.dto import CreateReceiptDTO
from modules.ticket.dto import CreateTicketDTO
from db import SessionLocal

class ProcessPaymentUseCase:
    def __init__(self, PurchaseRepository=None, UserRepository=None, UpdateUserRepo=None, UpdatePurchaseRepo=None, CreateTicketRepo=None, CreateReceiptRepo=None, FindEventByTierRepo=None):
        self.sharedSession = SessionLocal()
        
        self.findPurchaseRepository = PurchaseRepository or FindPurchaseByIdRepository(self.sharedSession)
        self.userRepository = UserRepository or FindUserByIdRepository(self.sharedSession)
        self.updateUserRepository = UpdateUserRepo or UpdateUserRepository(self.sharedSession)
        self.updatePurchaseRepository = UpdatePurchaseRepo or UpdatePurchaseRepository(self.sharedSession)
        self.createTicketRepository = CreateTicketRepo or CreateTicketRepository(self.sharedSession)
        self.createReceiptRepository = CreateReceiptRepo or CreateReceiptRepository(self.sharedSession)
        self.findEventByTierRepository = FindEventByTierRepo or FindEventByTierRepository(self.sharedSession)
    
    def execute(self, purchaseId: UUID):
        """
        Processes the payment for a purchase by its ID.

        Args:
            purchaseId (UUID): The ID of the purchase to process payment for.

        Returns:
            bool: True if the payment was processed successfully, False otherwise.
        """
        try:

            purchase = self.findPurchaseRepository.findById(purchaseId)
            if not purchase:
                raise HTTPException(status_code=404, detail="Compra não encontrada.")
            
            buyer = self.userRepository.findById(purchase.buyerId)
            if not buyer:
                raise HTTPException(status_code=404, detail="Comprador não encontrado.")
            
            seller = self.userRepository.findById(purchase.sellerId)
            if not seller:
                raise HTTPException(status_code=404, detail="Vendedor não encontrado.")
            
            if purchase.status != PaymentStatus.PENDING:
                raise HTTPException(status_code=400, detail="Pagamento já processado ou compra não está pendente.")
            
            for item in purchase.items:
                event = self.findEventByTierRepository.findByTier(item.tierId)
                if event.status != Status.ACTIVE:
                    raise HTTPException(status_code=400, detail=f"Evento associado ao lote não está ativo: {event.name}.") 

            if buyer.balance < purchase.totalPrice:
                raise HTTPException(status_code=400, detail="Saldo insuficiente para processar o pagamento.")
            
            buyer.balance -= purchase.totalPrice
            seller.balance += purchase.totalPrice

            buyerUpdateData = UpdateUserDTO(balance=buyer.balance)
            sellerUpdateData = UpdateUserDTO(balance=seller.balance)
            
            buyerUpdated = self.updateUserRepository.update(buyer, buyerUpdateData)
            if not buyerUpdated:
                raise HTTPException(status_code=400, detail="Erro ao atualizar saldo do comprador.")
        
            sellerUpdated = self.updateUserRepository.update(seller, sellerUpdateData)

            if not sellerUpdated:
                raise HTTPException(status_code=400, detail="Erro ao atualizar saldo do vendedor.")

            # Atualizar status da compra
            purchase.status = PaymentStatus.PAID
            purchaseUpdateData = UpdatePurchaseDTO(status=PaymentStatus.PAID)
            purchase = self.updatePurchaseRepository.update(purchase, purchaseUpdateData)
            if not purchase:
                raise HTTPException(status_code=400, detail="Erro ao atualizar status da compra.")

            # Criar tickets
            for item in purchase.items:
                ticketDto = CreateTicketDTO(
                    ownerId=purchase.buyerId,
                    tierId=item.tierId,
                    sellerId=purchase.sellerId
                )
                ticket = self.createTicketRepository.create(ticketDto)
                if not ticket:
                    raise HTTPException(status_code=400, detail="Erro ao criar ticket para a compra.")

            receiptDto = CreateReceiptDTO(
                userId=purchase.buyerId,
                purchaseId=purchase.id,
                description=f"Pagamento da compra entre {buyer.name} e {seller.name} no valor de R${purchase.totalPrice:.2f}"
            )
            receipt = self.createReceiptRepository.create(receiptDto)
            if not receipt:
                raise HTTPException(status_code=400, detail="Erro ao criar recibo para a compra.")
            
            print(f"Pagamento processado com sucesso para a compra {purchase.id}.")
            self.sharedSession.commit()
            return True
        except HTTPException as e:
            print(f"Erro ao processar pagamento HTTPEXCP: {e.detail}")
            raise e
        except Exception as e:
            print(f"Erro ao processar pagamento: {e}")
            raise HTTPException(status_code=400, detail="Erro ao processar pagamento.")
        finally:
            for repo in [self.findPurchaseRepository, self.userRepository, self.updateUserRepository, 
                        self.updatePurchaseRepository, self.createTicketRepository, self.createReceiptRepository]:
                if hasattr(repo, 'session'):
                    repo.session.close()