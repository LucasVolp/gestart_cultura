from modules.ticket import CreateTicketRepository, CreateTicketDTO

class CreateTicketUseCase:
    def __init__(self, repository=None):
        self.repository = repository or CreateTicketRepository()
    def execute(self, data: CreateTicketDTO):
        try:
            ticket = self.repository.create(data)
            print(f"Ingresso Cód. {ticket.code} criado com sucesso.")
            return ticket
        except Exception as e:
            print(f"Erro ao criar Ingresso {e}")
            raise e
        finally:
            self.repository.session.close()
