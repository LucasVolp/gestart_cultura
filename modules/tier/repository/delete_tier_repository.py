from db import SessionLocal
from models.models import Tier


class DeleteTierRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def delete(self, id) -> bool:
        """
        Deletes a tier from the database by ID.

        Args:
            id (str): Tier ID to be deleted.

        Returns:
            bool: True if the tier was deleted successfully, False otherwise.
        """
        try:
            tier = self.session.query(Tier).filter(Tier.id == id).first()
            if not tier:
                return False
            self.session.delete(tier)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            return False
