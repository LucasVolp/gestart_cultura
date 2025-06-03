from passlib.hash import bcrypt
from fastapi import HTTPException
from modules.user.repository import FindUserByEmailRepository
from modules.user.utils.jwt import createAccessToken

class AuthenthicateUser:
    def __init__(self, userRepository=None):
        self.repository = userRepository or FindUserByEmailRepository()

    def execute(self, email: str, password: str) -> dict:
        """Authenticates a user based on email and password.

        Raises:
            HTTPException: If authentication fails due to invalid credentials.

        Returns:
            str: A success message indicating the user has been authenticated.
        """
        user = self.repository.findByEmail(email)
        if not user or not bcrypt.verify(password, user.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        token = createAccessToken({"sub": str(user.id), "email": user.email, "role": user.role.value})
        return {"access_token": token, "token_type": "bearer"}