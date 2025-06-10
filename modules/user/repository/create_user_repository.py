from models.models import User
from modules.user.dto.create_user_dto import CreateUserDTO
from db import SessionLocal
from sqlalchemy.orm import joinedload

class CreateUserRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def create(self, data: CreateUserDTO) -> User:
        """        Creates a new user in the database.

        Args:
            data (CreateUserDTO): Data Transfer Object containing the user information to be created.

        Returns:
            User: Created User model instance.
        """
        data = data.model_dump()
        user = User(**data)
        self.session.add(user)
        self.session.commit()
        user = self.session.query(User).options(
            joinedload(User.events),
            joinedload(User.purchases),
            joinedload(User.ratings),
            joinedload(User.tickets),
            joinedload(User.receipts)
        )
        self.session.refresh(user)
        return user