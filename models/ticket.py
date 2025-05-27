from uuid import UUID
from enums.status import Status
from models.tier import Tier
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.user import User
    from models.seller import Seller

class Ticket:
    def __init__(self, id: UUID, owner: "User", tier: Tier, seller: "Seller", status: Status, code: str) -> None:
        self.__id = id
        self.__owner = owner
        self.__tier = tier
        self.__seller = seller
        self.__status = status
        self.__code = code

    def __str__(self):
        tipo = self.__class__.__name__
        seller = self.__seller.name
        return f"[{tipo}] ID: {self.__id} | Proprietário: {self.__owner} | Tier: {self.__tier} | Vendedor: {seller} | Status: {self.__status.name} | Código: {self.__code}"
    
    @property
    def owner(self):
        return self.__owner
    
    @owner.setter
    def owner(self, value):
        self.__owner = value

    @property
    def tier(self):
        return self.__tier
    
    @tier.setter
    def tier(self, value):
        self.__tier = value

    @property
    def seller(self):
        return self.__seller
    
    @seller.setter
    def seller(self, value):
        self.__seller = value

    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def code(self):
        return self.__code
    
    @code.setter
    def code(self, value):
        self.__code = value

    def validateTicket(self) -> bool:
        """_summary_

        Raises:
            ValueError: _description_
            ValueError: _description_

        Returns:
            bool: _description_
        """
        try:
            if self.__status == Status.VALID:
                return True
            elif self.__tier.event.status == Status.CANCELLED:
                raise ValueError("O evento foi cancelado.")
            elif self.__tier.event.status == Status.CLOSED:
                raise ValueError("O evento está fechado.")
        except ValueError as e:
            print(f"Erro: {str(e)}")
            return False
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")
            return False
        
    def getQRCode(self) -> str:
        """_summary_

        Raises:
            ValueError: _description_

        Returns:
            str: _description_
        """
        try:
            if not self.__code:
                raise ValueError("Código QR não gerado.")
            return f"QR Code: {self.__code}"
        except ValueError as e:
            print(f"Erro: {str(e)}")
            raise
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")
            raise