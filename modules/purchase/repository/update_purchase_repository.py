from dataclasses import asdict
from db import SessionLocal
from modules.purchase import UpdatePurchaseDTO

class UpdatePurchaseRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def update(self, purchase, data: UpdatePurchaseDTO):
        """
        Updates an existing purchase in the database.

        Args:
            purchase (Purchase): Purchase model instance to be updated.
            data (UpdatePurchaseDTO): Data Transfer Object containing the updated purchase information.
        Returns:
            Purchase: Updated Purchase instance.
        """
        data = data.model_dump(exclude_unset=True)
        if purchase not in self.session:
            purchase = self.session.merge(purchase)
        for key, value in data.items():
            if value is not None:
                setattr(purchase, key, value)
        self.session.commit()
        self.session.refresh(purchase)
        return purchase
