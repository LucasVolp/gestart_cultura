from modules.ticket import FindTicketByIdRepository

class FindTicketByIdUseCase:
    def __init__(self, repository=None):
        self.repository = repository or FindTicketByIdRepository()
    def execute(self, id: str):
        try:
            ticket = self.repository.findById(id)
            if not ticket:
                raise ValueError("Ingresso não encontrado.")
            return ticket
        finally:
            self.repository.session.close()
