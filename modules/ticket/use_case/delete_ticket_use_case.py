from modules.ticket.repository import DeleteTicketRepository, FindTicketByIdRepository
from fastapi import HTTPException

class DeleteTicketUseCase:
    def __init__(self, repository=None, findTicketByIdRepo=None):
        self.repository = repository or DeleteTicketRepository()
        self.findTicketByIdRepo = findTicketByIdRepo or FindTicketByIdRepository()
    
    def execute(self, id: str):
        """Deletes a ticket by its ID.

        Args:
            id (str): ID of the ticket to be deleted.

        Raises:
            HTTPException: If the ticket with the given ID does not exist or if an error occurs.

        Returns:
            bool: True if deletion was successful.
        """
        try:
            ticketExists = self.findTicketByIdRepo.findById(id)
            if not ticketExists:
                raise HTTPException(status_code=404, detail="Ingresso não encontrado.")
            ticket = self.repository.delete(ticketExists)
            if ticket:
                print(f"Ingresso deletado com sucesso.")
            return ticket
        except HTTPException as e:
            print(f"Erro ao deletar ingresso: {e.detail}")
            raise e
        except Exception as e:
            print(f"Erro ao deletar ingresso: {e}")
            raise HTTPException(status_code=500, detail="Erro ao deletar ingresso.")
        finally:
            self.repository.session.close()
