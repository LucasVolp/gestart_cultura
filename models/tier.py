import logging
from uuid import UUID
from enums.status import Status

class Tier:
    def __init__(self, id: UUID, amount: int, nome: str, price: float, startDate: str, endDate: str, status: str, tickets: list = None) -> None:
        self.__id = id
        self.__amount = amount
        self.__nome = nome
        self.__price = price
        self.__startDate = startDate
        self.__endDate = endDate
        self.__status = status
        self.__tickets = tickets if tickets is not None else []

    def __str__(self):
        tipo = self.__class__.__name__
        return f"[{tipo}] Nome: {self.__nome} | Preço: {self.__price} | Início: {self.__startDate} | Fim: {self.__endDate} | Status: {self.__status.name}"

    @property
    def _id(self):
        return self.__id
    
    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _amount(self):
        return self.__amount
    
    @_amount.setter
    def _amount(self, value):
        self.__amount = value

    @property
    def _nome(self):
        return self.__nome
    
    @_nome.setter
    def _nome(self, value):
        self.__nome = value

    @property
    def _price(self):
        return self.__price
    
    @_price.setter
    def _price(self, value):
        self.__price = value

    @property
    def _startDate(self):
        return self.__startDate
    
    @_startDate.setter
    def _startDate(self, value):
        self.__startDate = value

    @property
    def _endDate(self):
        return self.__endDate
    
    @_endDate.setter
    def _endDate(self, value):
        self.__endDate = value

    @property
    def _status(self):
        return self.__status
    
    @_status.setter
    def _status(self, value):
        self.__status = value

    
    def openTier(self) -> None:
        """_summary_

        Raises:
            ValueError: _description_
        """
        try:
            if self.__status == Status.CLOSED or self.getDisponibility() <= 0:
                raise ValueError("Não é possível abrir um tier que já está fechado ou sem ingressos disponiveis.")
            self.__status = Status.OPEN
        except ValueError as e:
            logging.error(f"Erro ao abrir o tier {self.__nome}: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao abrir o tier {self.__nome}: {str(e)}")
            raise

    def closeTier(self) -> None:
        """_summary_

        Raises:
            ValueError: _description_
        """
        try: 
            if self.__status == Status.CLOSED:
                raise ValueError("Não é possível fechar um tier que já está fechado.")
            self.__status = Status.CLOSED
        except ValueError as e:
            logging.error(f"Erro ao fechar o tier {self.__nome}: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao fechar o tier {self.__nome}: {str(e)}")
            raise

    def getDisponibility(self) -> int:
        """_summary_

        Raises:
            ValueError: _description_

        Returns:
            int: _description_
        """
        try:
            if self.__status == Status.CLOSED:
                raise ValueError("Não é possível obter a disponibilidade de um tier fechado.")
            return self.__amount - len(self.__tickets)
        except ValueError as e:
            logging.error(f"Erro ao obter a disponibilidade do tier {self.__nome}: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao obter a disponibilidade do tier {self.__nome}: {str(e)}")
            raise
    
    def addTicket(self, ticket) -> None:
        """_summary_

        Args:
            ticket (_type_): _description_

        Raises:
            ValueError: _description_
            ValueError: _description_
        """
        try:
            if self.__status != Status.OPEN:
                raise ValueError("Não é possível adicionar ingressos a um tier fechado.")
            if self.getDisponibility() <= 0:
                raise ValueError("Não há ingressos disponíveis neste tier.")
            self.__tickets.append(ticket)
        except ValueError as e:
            logging.error(f"Erro ao adicionar ticket ao tier {self.__nome}: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao adicionar ticket ao tier {self.__nome}: {str(e)}")
            raise