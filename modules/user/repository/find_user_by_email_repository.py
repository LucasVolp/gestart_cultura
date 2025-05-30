from models import User
from db import SessionLocal

class FindUserByEmailRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findByEmail(self, email: str):
        return self.session.query(User).filter(User.email == email).first()
