import logging
from uuid import UUID
from models.event import Event
from enums.status import Status
from models.tier import Tier
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.user import User

class Ticket:
    def __init__(self, id: UUID, owner: "User", tier: Tier, event: Event, status: Status, code: str) -> None:
        self.__id = id
        self.__owner = owner
        self.__tier = tier
        self.__event = event
        self.__status = status
        self.__code = code

    def __str__(self):
        tipo = self.__class__.__name__
        return f"[{tipo}] ID: {self.__id} | Proprietário: {self.__owner} | Tier: {self.__tier} | Evento: {self.__event} | Status: {self.__status.name} | Código: {self.__code}"
    
    @property
    def _owner(self):
        return self.__owner
    
    @_owner.setter
    def _owner(self, value):
        self.__owner = value

    @property
    def _tier(self):
        return self.__tier
    
    @_tier.setter
    def _tier(self, value):
        self.__tier = value

    @property
    def _event(self):
        return self.__event
    
    @_event.setter
    def _event(self, value):
        self.__event = value

    @property
    def _status(self):
        return self.__status
    
    @_status.setter
    def _status(self, value):
        self.__status = value

    @property
    def _code(self):
        return self.__code
    
    @_code.setter
    def _code(self, value):
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
            elif self.__event.__status == Status.CANCELLED:
                raise ValueError("O evento foi cancelado.")
            elif self.__event.__status == Status.CLOSED:
                raise ValueError("O evento está fechado.")
        except ValueError as e:
            logging.error(f"Erro: {str(e)}")
            return False
        except Exception as e:
            logging.error(f"Erro inesperado: {str(e)}")
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
            logging.error(f"Erro: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado: {str(e)}")
            raise