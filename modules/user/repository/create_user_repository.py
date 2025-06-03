from models.models import User
from modules.user import CreateUserDTO
from db import SessionLocal

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
        self.session.refresh(user)
        return user