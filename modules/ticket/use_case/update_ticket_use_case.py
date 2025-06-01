from modules.ticket.repository import UpdateTicketRepository, FindTicketByIdRepository
from modules.ticket.dto import UpdateTicketDTO
from fastapi import HTTPException

class UpdateTicketUseCase:
    def __init__(self, repository=None, findTicketByIdRepo=None):
        self.repository = repository or UpdateTicketRepository()
        self.findTicketByIdRepo = findTicketByIdRepo or FindTicketByIdRepository()

    def execute(self, id, data: UpdateTicketDTO):
        """Executes the use case to update an existing ticket.

        Args:
            id (str): ID of the ticket to be updated.
            data (UpdateTicketDTO): Data Transfer Object containing the updated ticket information.

        Raises:
            HTTPException: If the ticket with the given ID does not exist or if an error occurs.

        Returns:
            Ticket: Updated Ticket model instance.
        """
        try:
            ticketExists = self.findTicketByIdRepo.findById(id)
            if not ticketExists:
                raise HTTPException(status_code=404, detail="Ingresso não encontrado.")
            
            ticket = self.repository.update(ticketExists, data)
            print(f"Ingresso atualizado com sucesso.")
            return ticket
        except HTTPException as e:
            print(f"Erro ao atualizar ingresso: {e.detail}")
            raise e
        except Exception as e:
            print(f"Erro ao atualizar ingresso: {e}")
            raise HTTPException(status_code=500, detail="Erro ao atualizar ingresso.")
        finally:
            self.repository.session.close()
