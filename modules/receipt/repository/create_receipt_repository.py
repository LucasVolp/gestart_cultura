from dataclasses import asdict
from db import SessionLocal
from models.models import Receipt
from modules.receipt import CreateReceiptDTO

class CreateReceiptRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def create(self, data: CreateReceiptDTO):
        """
        Creates a new receipt in the database.

        Args:
            data (CreateReceiptDTO): Data Transfer Object containing the receipt information to be created.
        Returns:
            Receipt: Created Receipt model instance.
        Raises:
            ValueError: If an integrity error occurs while creating the receipt.
        """
        data = asdict(data)
        receipt = Receipt(**data)
        self.session.add(receipt)
        self.session.commit()
        self.session.refresh(receipt)
        return receipt
