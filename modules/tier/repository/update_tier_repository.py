from db import SessionLocal
from models.models import Tier
from modules.tier.dto import UpdateTierDTO

class UpdateTierRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def update(self, tier, data: UpdateTierDTO):
        """
        Updates an existing tier in the database.

        Args:
            tier (Tier): Tier instance to be updated.
            data (UpdateTierDTO): Data Transfer Object containing the updated tier information.

        Returns:
            Tier: Updated Tier instance.
        """
        if not tier in self.session:
            tier = self.session.merge(tier)
        data = data.model_dump(exclude_unset=True)
        for key, value in data.items():
            if value is not None:
                setattr(tier, key, value)
        self.session.commit()
        self.session.refresh(tier)
        return tier