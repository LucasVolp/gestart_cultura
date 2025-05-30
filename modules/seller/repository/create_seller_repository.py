from dataclasses import asdict
from models import Seller
from db import SessionLocal
from modules.seller import CreateSellerDTO
from sqlalchemy.exc import IntegrityError

class CreateSellerRepository:
    def __init__(self, session=None):
        self.session = session or SessionLocal()

    def create(self, data: CreateSellerDTO):
        try:
            data = asdict(data)
            seller = Seller(**data)
            self.session.add(seller)
            self.session.commit()
            self.session.refresh(seller)
            return seller
        except IntegrityError as e:
            self.session.rollback()
            raise ValueError("Usuário com CPF, email ou telefone já cadastrado.") from e
