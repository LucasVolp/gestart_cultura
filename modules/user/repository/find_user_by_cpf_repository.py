from models import User
from db import SessionLocal

class FindUserByCpfRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def findByCpf(self, cpf: str):
        return self.session.query(User).filter(User.cpf == cpf).first()
