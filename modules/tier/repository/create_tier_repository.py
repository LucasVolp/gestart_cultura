from db import SessionLocal
from models.models import Tier
from sqlalchemy.exc import IntegrityError

class CreateTierRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def create(self, data):
        """
        Creates a new tier in the database.

        Args:
            data: Data of the tier to be created.

        Raises:
            ValueError: If an integrity error occurs while creating the tier.

        Returns:
            Tier: Created Tier model instance.
        """
        try:
            data_dict = data.model_dump()
            tier = Tier(**data_dict)
            self.session.add(tier)
            self.session.commit()
            self.session.refresh(tier)
            return tier
        except IntegrityError as e:
            self.session.rollback()
            raise ValueError("Já existe um Lote com este Nome") from e
