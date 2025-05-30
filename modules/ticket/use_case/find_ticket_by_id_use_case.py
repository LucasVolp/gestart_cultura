from modules.ticket import FindTicketByIdRepository

class FindTicketByIdUseCase:
    def __init__(self, repository=None):
        self.repository = repository or FindTicketByIdRepository()
    def execute(self, id: str):
        """Finds a ticket by ID in the database.

        Args:
            id (str): ID of the ticket to be found.

        Raises:
            ValueError: If the ticket with the given ID does not exist.

        Returns:
            _type_: Ticket model instance if found, otherwise raises ValueError.
        """
        try:
            ticket = self.repository.findById(id)
            if not ticket:
                raise ValueError("Ingresso não encontrado.")
            return ticket
        finally:
            self.repository.session.close()
