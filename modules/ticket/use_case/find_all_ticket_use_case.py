from modules.ticket.repository import FindAllTicketsRepository
from fastapi import HTTPException

class FindAllTicketUseCase:
    def __init__(self, repository=None):
        self.repository = repository or FindAllTicketsRepository()
        
    def execute(self):
        """Executes the use case to find all tickets.

        Raises:
            HTTPException: If an error occurs during the operation.

        Returns:
            list: List of Ticket model instances or an empty list if no tickets are found.
        """
        try:
            tickets = self.repository.findAll()
            if not tickets:
                print("Nenhum ingresso encontrado.")
                return []
            print(f"{len(tickets)} ingressos encontrados.")
            return tickets
        except Exception as e:
            print(f"Erro ao buscar ingressos: {e}")
            raise HTTPException(status_code=500, detail="Erro ao buscar ingressos.")
        finally:
            self.repository.session.close()
