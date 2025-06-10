from modules.ticket.repository import CreateTicketRepository
from modules.ticket.dto import CreateTicketDTO
from fastapi import HTTPException

class CreateTicketUseCase:
    def __init__(self, repository=None):
        self.repository = repository or CreateTicketRepository()
        
    def execute(self, data: CreateTicketDTO):
        """Executes the use case to create a new ticket.

        Args:
            data (CreateTicketDTO): Data Transfer Object containing the ticket information to be created.

        Raises:
            HTTPException: If an error occurs during the operation.

        Returns:
            Ticket: Created Ticket model instance.
        """
        try:
            ticket = self.repository.create(data)
            print(f"Ingresso Cód. {ticket.code} criado com sucesso.")
            return ticket
        except Exception as e:
            print(f"Erro ao criar Ingresso: {e}")
            raise HTTPException(status_code=500, detail="Erro ao criar ingresso.")
        finally:
            self.repository.session.close()
