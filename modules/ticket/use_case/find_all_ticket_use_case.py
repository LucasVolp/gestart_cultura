from modules.ticket import FindAllTicketsRepository

class FindAllTicketUseCase:
    def __init__(self, repository=None):
        self.repository = repository or FindAllTicketsRepository()
    def execute(self):
        """Executes the use case to find all tickets.

        Raises:
            e: Exception if an error occurs during the operation.

        Returns:
            _type_: List of Ticket model instances or an empty list if no tickets are found.
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
            raise e
        finally:
            self.repository.session.close()
