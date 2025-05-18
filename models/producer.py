import logging
import re
from uuid import uuid4, UUID
from models.person import Person
from models.event import Event
from enums.typeEvent import TypeEvent
from enums.status import Status
from datetime import date

class Producer(Person):
    producers = []

    def __init__(self, id: UUID, name: str, cpf: str, birth: str, email: str, password: str, phone: str, status: Status, cnpj: str, enterprise: str):
        super().__init__(id, name, cpf, birth, email, password, phone, status)
        self.__cnpj = cnpj if self._validate_cnpj(cnpj) else None
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
                print("Email inválido.")
                return
            # Simula envio de email
            logging.info(f"Notificação enviada para {recipient}: {message}")
        except Exception as e:
            print(f"Erro inesperado ao enviar notificação para {recipient}: {str(e)}")

    def scheduleNotification(self, recipient: str, message: str, datetime: date) -> None:
        try:
            if not self._validate_email(recipient):
                print("Email inválido.")
                return
            if datetime < date.today():
                print("A data de agendamento deve ser futura.")
                return
            # Simula agendamento de email
            logging.info(f"Notificação agendada para {recipient} em {datetime}: {message}")
        except Exception as e:
            print(f"Erro inesperado ao agendar notificação para {recipient}: {str(e)}")

    def createEvent(self, name: str, description: str, date: date, local: str, size: int, typeEvent: TypeEvent, status: Status, tiers: list = None) -> Event:
        """Cria um novo evento e adiciona à lista do produtor. Retorna o evento criado ou None em caso de erro."""
        if not name or not description or not local or size <= 0 or not typeEvent or date < date.today():
            print("Todos os campos são obrigatórios, tamanho deve ser maior que zero e a data deve estar no futuro.")
            return None
        event = Event(id=uuid4(), name=name, description=description, date=date, local=local, size=size, typeEvent=typeEvent, status=Status.OPEN)
        if tiers:
            for tier_data in tiers:
                event.createTier(**tier_data)
        self.events.append(event)
        return event

    def updateEvent(self, event: Event, name: str, description: str, date: date, local: str, size: int, typeEvent: TypeEvent) -> bool:
        """Atualiza os dados de um evento do produtor. Retorna True se sucesso, False se falha."""
        if event not in self.events:
            print("O evento não pertence a este produtor.")
            return False
        if name:
            event.name = name
        if description:
            event.description = description
        if date:
            event.date = date
        if local:
            event.local = local
        if size:
            event.size = size
        if typeEvent:
            event.typeEvent = typeEvent
        return True

    def deleteEvent(self, event: Event) -> bool:
        """Tenta remover um evento do produtor. Retorna True se sucesso, False se falha."""
        try:
            if event not in self.events:
                print("O evento não pertence a este produtor.")
                return False
            if any(tier.getDisponibility() < tier._amount for tier in event.getTiers()):
                print("Não é possível excluir um evento com ingressos já emitidos.")
                return False
            self.events.remove(event)
            return True
        except Exception as e:
            logging.error(f"Erro inesperado ao excluir evento: {str(e)}")
            print("Erro inesperado ao excluir evento.")
            return False
    
    def listEvents(self) -> bool:
        """Lista os eventos do produtor. Retorna True se houver eventos, False se não houver."""
        if not self.events:
            print("Nenhum evento encontrado.")
            return False
        for idx, event in enumerate(self.events, start=1):
            print(f"{idx} - {event}")
        return True