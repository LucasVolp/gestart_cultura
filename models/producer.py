import logging
import re
from uuid import uuid4
from models.person import Person
from models.event import Event
from enums.typeEvent import TypeEvent
from enums.status import Status
from datetime import date

class Producer(Person):
    producers = []

    def __init__(self, id, name, cpf, birth, email, password, phone, status, cnpj:str, enterprise):
      super().__init__(id, name, cpf, birth, email, password, phone, status)
      self.__cnpj = cnpj
      self.__enterprise = enterprise
      self.events = []

    @staticmethod
    def _validate_cnpj(cnpj: str) -> bool:
        """_summary_

        Args:
            cnpj (str): _description_

        Returns:
            bool: _description_
        """
        pattern = r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$"
        return bool(re.match(pattern, cnpj))

    @property
    def cnpj(self) -> str:
        return self.__cnpj

    @property
    def enterprise(self) -> str:
        return self.__enterprise

    def __str__(self):
        tipo = self.__class__.__name__
        return f"[{tipo}] Nome: {self.name} | Email: {self.email} | CNPJ: {self.__cnpj} | Empresa: {self.__enterprise}"
    
    @classmethod
    def getProducers(cls):
        """_summary_

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        try:
            if not cls.producers:
                raise ValueError("Nenhum produtor encontrado.")
            return list(cls.producers)
        except ValueError as e:
            logging.error(f"Erro ao obter produtores: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao obter produtores: {str(e)}")
            raise

    def updateProfile(self, name: str = None, birth: date = None, email: str = None, password: str = None, cnpj: str = None, enterprise: str = None) -> None:
        """_summary_

        Args:
            name (str, optional): _description_. Defaults to None.
            birth (date, optional): _description_. Defaults to None.
            email (str, optional): _description_. Defaults to None.
            password (str, optional): _description_. Defaults to None.
            cnpj (str, optional): _description_. Defaults to None.
            enterprise (str, optional): _description_. Defaults to None.

        Raises:
            ValueError: _description_
            ValueError: _description_
        """
        try:
            if cnpj and not self._validate_cnpj(cnpj):
                raise ValueError("CNPJ inválido.")
            if enterprise and not enterprise.strip():
                raise ValueError("O nome da empresa não pode ser vazio.")
            super().updateProfile(name, birth, email, password)
            # Atualizar campos específicos
            self.__cnpj = cnpj if cnpj else self.__cnpj
            self.__enterprise = enterprise if enterprise else self.__enterprise
        except ValueError as e:
            logging.error(f"Erro ao atualizar perfil do produtor {self.email}: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao atualizar perfil do produtor {self.email}: {str(e)}")
            raise
    
    def sendNotification(self, recipient: str, message: str) -> None:

        try:
            if not self._validate_email(recipient):
                raise ValueError("Email inválido.")
            # Simula envio de email em massa
            logging.info(f"Email em massa enviado para {recipient}: {message}")
        except ValueError as e:
            logging.error(f"Erro ao enviar notificação para {recipient}: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao enviar notificação para {recipient}: {str(e)}")
            raise

    def scheduleNotification(self, recipient: str, message: str, datetime: date) -> None:
        try:
            if not self._validate_email(recipient):
                raise ValueError("Email inválido.")
            if datetime < date.today():
                raise ValueError("A data de agendamento deve ser futura.")
            # Simula agendamento de email em massa
            logging.info(f"Email agendado para {recipient} em {datetime}: {message}")
        except ValueError as e:
            logging.error(f"Erro ao agendar notificação para {recipient}: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao agendar notificação para {recipient}: {str(e)}")
            raise

    def createEvent(self, name: str, description: str, date: date, local: str, size: int, typeEvent: TypeEvent, status: Status, tiers: list = None) -> Event:
        """_summary_

        Args:
            name (str): _description_
            description (str): _description_
            date (date): _description_
            local (str): _description_
            size (int): _description_
            typeEvent (TypeEvent): _description_
            status (Status): _description_
            tiers (list, optional): _description_. Defaults to None.

        Raises:
            ValueError: _description_

        Returns:
            Event: _description_
        """
        try:
            if not name or not description or not local or size <= 0 or not typeEvent and date < date.today():
                raise ValueError("Todos os campos são obrigatórios, tamanho deve ser maior que zero e a data deve estar no futuro.")
            event = Event(id=uuid4(), name=name, description=description, date=date, local=local, size=size, typeEvent=typeEvent, status=Status.OPEN)
            if tiers:
                for tier_data in tiers:
                    event.createTier(**tier_data)
            self.events.append(event)
            return event
        except ValueError as e:
            logging.error(f"Erro ao criar evento: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao criar evento: {str(e)}")
            raise

    def updateEvent(self, event:Event, name:str, description:str, date:date, local:str, size:int, typeEvent: TypeEvent) -> None:
        """_summary_

        Args:
            event (Event): _description_
            name (str): _description_
            description (str): _description_
            date (date): _description_
            local (str): _description_
            size (int): _description_
            typeEvent (TypeEvent): _description_

        Raises:
            ValueError: _description_
        """
        try:
            if event not in self.events:
                raise ValueError("O evento não pertence a este produtor.")
            event._name = name if name else event._name
            event._description = description if description else event._description
            event._date = date if date else event._date
            event._local = local if local else event._local
            event._size = size if size else event._size
            event._typeEvent = typeEvent if typeEvent else event._typeEvent
        except ValueError as e:
            logging.error(f"Erro ao atualizar evento: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao atualizar evento: {str(e)}")
            raise

    def deleteEvent(self, event: Event) -> None:
        """_summary_

        Args:
            event (Event): _description_

        Raises:
            ValueError: _description_
            ValueError: _description_
        """
        try:
            if event not in self.events:
                raise ValueError("O evento não pertence a este produtor.")
            if any(tier.getDisponibility() < tier._amount for tier in event.getTiers()):
                raise ValueError("Não é possível excluir um evento com ingressos já emitidos.")
            self.events.remove(event)
        except ValueError as e:
            logging.error(f"Erro ao excluir evento: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao excluir evento: {str(e)}")
            raise

    def getEvent(self) -> list[Event]:
        """_summary_

        Raises:
            ValueError: _description_

        Returns:
            list[Event]: _description_
        """
        try:
            if not self.events:
                raise ValueError("Nenhum evento encontrado.")
            return list(self.events)
        except ValueError as e:
            logging.error(f"Erro ao obter eventos: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Erro inesperado ao obter eventos: {str(e)}")
            raise