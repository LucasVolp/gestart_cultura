from modules.ticket import CreateTicketRepository, CreateTicketDTO

class CreateTicketUseCase:
    def __init__(self, repository=None):
        self.repository = repository or CreateTicketRepository()
    def execute(self, data: CreateTicketDTO):
        """Executes the use case to create a new ticket.

        Args:
            data (CreateTicketDTO): Data Transfer Object containing the ticket information to be created.

        Raises:
            e: Exception if an error occurs during the operation.

        Returns:
            _type_: Created Ticket model instance.
        """
        try:
            ticket = self.repository.create(data)
            print(f"Ingresso Cód. {ticket.code} criado com sucesso.")
            return ticket
        except Exception as e:
            print(f"Erro ao criar Ingresso {e}")
            raise e
        finally:
            self.repository.session.close()
