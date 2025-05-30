from modules.ticket import UpdateTicketRepository, UpdateTicketDTO, FindTicketByIdRepository

class UpdateTicketUseCase:
    def __init__(self, repository=None, FindTicketByIdRepo=None):
        self.repository = repository or UpdateTicketRepository()
        self.findTicketByIdRepo = FindTicketByIdRepo or FindTicketByIdRepository()

    def execute(self, id, data: UpdateTicketDTO):
        """Executes the use case to update an existing ticket.

        Args:
            id (_type_): ID of the ticket to be updated.
            data (UpdateTicketDTO): Data Transfer Object containing the updated ticket information.

        Raises:
            ValueError: If the ticket with the given ID does not exist.
            e: Exception raised during the update process.

        Returns:
            _type_: Updated Ticket model instance if successful, otherwise raises ValueError.
        """
        try:
            ticketExists = self.findTicketByIdRepo.findById(id)
            if not ticketExists:
                raise ValueError(f"Ingresso não encontrado.")
            
            ticket = self.repository.update(ticketExists, data)
            print(f"Ingresso atualizado com sucesso.")
            return ticket
        except Exception as e:
            print(f"Erro ao atualizar o ingresso {e}")
            raise e
        finally:
            self.repository.session.close()
