from dataclasses import asdict
from db import SessionLocal
from modules.receipt import UpdateReceiptDTO

class UpdateReceiptRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def update(self, receipt, data: UpdateReceiptDTO):
        """
        Updates an existing receipt in the database.

        Args:
            receipt: Receipt model instance to be updated.
            data (UpdateReceiptDTO): Data Transfer Object containing the updated receipt information.
        Returns:
            Receipt: Updated Receipt instance.
        """
        data = asdict(data)
        for key, value in data.items():
            if value is not None:
                setattr(receipt, key, value)
        self.session.commit()
        self.session.refresh(receipt)
        return receipt
