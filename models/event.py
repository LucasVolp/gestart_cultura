from datetime import date
import logging
from uuid import UUID, uuid4
from enums.status import Status
from enums.typeEvent import TypeEvent
from models.tier import Tier
from models.rating import Rating


class Event():
    def __init__(self, id: UUID, name: str, description: str, date: str, local: str, size: int, typeEvent: TypeEvent, status: Status, tiers: list = None, ratings: list = None) -> None:
        self.__id = id
        self.__name = name
        self.__description = description
        self.__date = date
        self.__local = local
        self.__size = size
        self.__typeEvent = typeEvent
        self.__status = status
        self.__tiers = []
        self.__ratings = []


    def __str__(self):
        tipo = self.__class__.__name__
        typeEvent = self.__typeEvent.name
        status = self.__status.name
        return f"[{tipo}] Nome: {self.__name} | Descrição: {self.__description} | Data: {self.__date} | Local: {self.__local} | Tamanho: {self.__size} | Tipo de Evento: {typeEvent} | Status: {status}"

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _name(self):
        return self.__name
    
    @_name.setter
    def _name(self, value):
        self.__name = value

    @property
    def _description(self):
        return self.__description
    
    @_description.setter
    def _description(self, value):
        self.__description = value

    @property
    def _date(self):
        return self.__date
    
    @_date.setter
    def _date(self, value):
        self.__date = value

    @property
    def _local(self):
        return self.__local
    
    @_local.setter
    def _local(self, value):
        self.__local = value

    @property
    def _size(self):
        return self.__size
    
    @_size.setter
    def _size(self, value):
        self.__size = value

    @property
    def _typeEvent(self):
        return self.__typeEvent
    
    @_typeEvent.setter
    def _typeEvent(self, value):
        self.__typeEvent = value


    def getTiers(self):
        """_summary_

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        try:
            if not self.__tiers:
                raise ValueError("Nenhum tier encontrado.")
            return list(self.__tiers)
        except ValueError as e:
            logging.error(f"Erro ao obter tiers: {e}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao obter tiers: {e}")
            raise

    def createTier(self, amount: int, nome: str, price: float, startDate: str, endDate: str, status: Status) -> Tier:
        """_summary_

        Args:
            amount (int): _description_
            nome (str): _description_
            price (float): _description_
            startDate (str): _description_
            endDate (str): _description_
            status (Status): _description_

        Raises:
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_

        Returns:
            Tier: _description_
        """
        try:
            if self.__status != Status.OPEN:
                raise ValueError("Não é possível criar tiers para um evento que não está aberto.")
            if amount > self.__size:
                raise ValueError("A quantidade de ingressos no tier excede o tamanho do evento.")
            if price < 0:
                raise ValueError("O preço não pode ser negativo.")
            if startDate >= endDate:
                raise ValueError("A data de início deve ser anterior à data de término.")
            tier = Tier(id=uuid4(), amount=amount, nome=nome, price=price, startDate=startDate, endDate=endDate, status=status)
            self.__tiers.append(tier)
            return tier
        except ValueError as e:
            logging.error(f"Erro ao criar o tier: {e}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao criar o tier: {e}")
            raise

    def updateTier(self, tier: Tier, amount: int = None, nome: str = None, price: float = None, startDate: str = None, endDate: str = None, status: Status = None) -> None:
        """_summary_

        Args:
            tier (Tier): _description_
            amount (int, optional): _description_. Defaults to None.
            nome (str, optional): _description_. Defaults to None.
            price (float, optional): _description_. Defaults to None.
            startDate (str, optional): _description_. Defaults to None.
            endDate (str, optional): _description_. Defaults to None.
            status (Status, optional): _description_. Defaults to None.

        Raises:
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        try:
            if tier not in self.__tiers:
                raise ValueError("O tier não pertence a este evento.")
            tier._amount = amount if amount else tier._amount
            tier._nome = nome if nome else tier._nome
            tier._price = price if price else tier._price
            tier._startDate = startDate if startDate else tier._startDate
            tier._endDate = endDate if endDate else tier._endDate
            tier._status = status if status else tier._status
            if amount and amount > self.__size:
                raise ValueError("A quantidade de ingressos no tier excede o tamanho do evento.")
            if price and price < 0:
                raise ValueError("O preço não pode ser negativo.")
            if startDate and endDate and startDate >= endDate:
                raise ValueError("A data de início deve ser anterior à data de término.")
            if status and status not in [Status.OPEN, Status.CLOSED]:
                raise ValueError("Status inválido. Deve ser OPEN ou CLOSED.")
            return tier
        except ValueError as e:
            logging.error(f"Erro ao atualizar o tier: {e}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao atualizar o tier: {e}")
            raise
    
    def deleteTier(self, tier: Tier) -> bool:
        try:
            if tier not in self.__tiers:
                raise ValueError("O tier não pertence a este evento.")
            if tier.getDisponibility() < tier._amount:
                raise ValueError("Não é possível excluir um tier com ingressos já emitidos.")
            self.__tiers.remove(tier)
            return True
        except ValueError as e:
            logging.error(f"Erro ao excluir o tier: {e}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao excluir o tier: {e}")
            raise

    def getRatings(self):
        """_summary_

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        try:
            if not self.__ratings:
                raise ValueError("Nenhuma avaliação encontrada.")
            return list(self.__ratings)
        except ValueError as e:
            logging.error(f"Erro ao obter avaliações: {e}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao obter avaliações: {e}")
            raise
    
    def addRating(self, rating: Rating) -> None:
        """_summary_

        Args:
            rating (Rating): _description_

        Raises:
            ValueError: _description_
        """
        try:
            if rating in self.__ratings:
                raise ValueError("A avaliação já existe.")
            self.__ratings.append(rating)
        except ValueError as e:
            logging.error(f"Erro ao adicionar avaliação: {e}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao adicionar avaliação: {e}")
            raise

    def deleteRating(self, rating: Rating) -> bool:
        """_summary_

        Args:
            rating (Rating): _description_

        Raises:
            ValueError: _description_

        Returns:
            bool: _description_
        """
        try:
            if rating not in self.__ratings:
                raise ValueError("A avaliação não pertence a este evento.")
            self.__ratings.remove(rating)
            return True
        except ValueError as e:
            logging.error(f"Erro ao excluir avaliação: {e}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao excluir avaliação: {e}")
            raise

    def availability(self) -> Status:
        """_summary_

        Returns:
            Status: _description_
        """
        try:
            return self.__status
        except Exception as e:
            logging.error(f"Erro ao verificar a disponibilidade do evento: {e}")
            raise

        