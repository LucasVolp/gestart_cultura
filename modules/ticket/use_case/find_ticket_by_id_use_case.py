from modules.ticket.repository import FindTicketByIdRepository
from fastapi import HTTPException

class FindTicketByIdUseCase:
    def __init__(self, repository=None):
        self.repository = repository or FindTicketByIdRepository()
        
    def execute(self, id: str):
        """Finds a ticket by ID in the database.

        Args:
            id (str): ID of the ticket to be found.

        Raises:
            HTTPException: If the ticket with the given ID does not exist or if an error occurs.

        Returns:
            Ticket: Ticket model instance if found.
        """
        try:
            ticket = self.repository.findById(id)
            if not ticket:
                raise HTTPException(status_code=404, detail="Ingresso não encontrado.")
            return ticket
        except HTTPException as e:
            print(f"Erro ao buscar ingresso: {e.detail}")
            raise e
        except Exception as e:
            print(f"Erro ao buscar ingresso: {e}")
            raise HTTPException(status_code=500, detail="Erro ao buscar ingresso.")
        finally:
            self.repository.session.close()
