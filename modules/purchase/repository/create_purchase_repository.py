from db import SessionLocal
from models.models import Purchase, PurchaseItem
from modules.purchase.dto import CreatePurchaseDTO
from sqlalchemy.orm import joinedload

class CreatePurchaseRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def createPurchaseWithItems(self, purchaseData, itemsData):
        """
        Cria uma purchase com seus items em uma única transação atômica.
        
        Args:
            purchaseData (dict): Dados da Purchase (sem totalPrice, será calculado)
            itemsData (list): Lista de dicts com dados dos PurchaseItems
            
        Returns:
            Purchase: Instância da Purchase criada com items carregados
            
        Raises:
            Exception: Se ocorrer erro durante a criação
        """
        try:
            # 1. Criar Purchase com totalPrice inicial
            purchaseInstance = Purchase(**purchaseData, totalPrice=0.0)
            self.session.add(purchaseInstance)
            self.session.flush()
            
            totalPrice = 0.0
            purchaseItems = []

            for itemData in itemsData:
                itemInstance = PurchaseItem(
                    purchaseId=purchaseInstance.id,
                    **itemData
                )
                purchaseItems.append(itemInstance)
                totalPrice += itemData['totalPrice']
            
            self.session.add_all(purchaseItems)
            purchaseInstance.totalPrice = totalPrice

            self.session.commit()
            
            purchaseWithItems = (
                self.session.query(Purchase)
                .options(joinedload(Purchase.items))
                .filter(Purchase.id == purchaseInstance.id)
                .first()
            )
            
            return purchaseWithItems
            
        except Exception as e:
            self.session.rollback()
            raise e
        finally:
            self.session.close()

    def create(self, data: CreatePurchaseDTO):
        """
        Creates a new purchase in the database (método simples, sem items).

        Args:
            data (CreatePurchaseDTO): Data Transfer Object containing purchase details.

        Returns:
            Purchase: Created Purchase instance with items loaded.
        """
        try:
            dataDict = data.model_dump(exclude={'items'})  # Excluir items se existir
            purchase = Purchase(**dataDict)
            self.session.add(purchase)
            self.session.commit()
            
            purchaseWithItems = (
                self.session.query(Purchase)
                .options(joinedload(Purchase.items))
                .filter(Purchase.id == purchase.id)
                .first()
            )
            
            return purchaseWithItems
            
        except Exception as e:
            self.session.rollback()
            raise e
        finally:
            self.session.close()
