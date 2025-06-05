from models.models import User
from modules.user.dto.update_user_dto import UpdateUserDTO
from db import SessionLocal

class UpdateUserRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def update(self, user, data: UpdateUserDTO) -> User:
        """
        Updates an existing user in the database.

        Args:
            user (_type_): User model instance to be updated.
            data (UpdateUserDTO): Data Transfer Object containing the updated user information.

        Returns:
            User: Updated User model instance.
        """
        if user not in self.session:
            user = self.session.merge(user)
        data = data.model_dump(exclude_unset=True)                
        for key, value in data.items():
            if value is not None:
                setattr(user, key, value)
        self.session.commit()
        self.session.refresh(user)
        return user