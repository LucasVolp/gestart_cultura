from db import SessionLocal
from models.models import PurchaseItem
from modules.purchaseItems import CreatePurchaseItemDTO

class CreatePurchaseItemRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def create(self, data: CreatePurchaseItemDTO):
        """
        Creates a new purchase item in the database.
        Args:
            data (CreatePurchaseItemDTO): Data of the purchase item to be created.
        Returns:
            PurchaseItem: Created PurchaseItem model instance.
        Raises:
            Exception: If an integrity error occurs while creating the purchase item.
        """
        try:
            data = data.model_dump()
            purchase_item = PurchaseItem(**data)
            self.session.add(purchase_item)
            self.session.commit()
            self.session.refresh(purchase_item)
            return purchase_item
        except Exception as e:
            self.session.rollback()
            raise Exception("Erro ao criar Itens de compra") from e
