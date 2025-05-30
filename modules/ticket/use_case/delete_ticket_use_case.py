from modules.ticket import DeleteTicketRepository, FindTicketByIdRepository

class DeleteTicketUseCase:
    def __init__(self, repository=None, findTicketByIdRepo=None):
        self.repository = repository or DeleteTicketRepository()
        self.findTicketByIdRepo = findTicketByIdRepo or FindTicketByIdRepository()
    
    def execute(self, id: str):
        try:
            ticketExists = self.findTicketByIdRepo.findById(id)
            if not ticketExists:
                raise ValueError("Ingresso não encontrado.")
            ticket = self.repository.delete(ticketExists)
            if ticket:
                print(f"Ingresso deletado com sucesso.")
            return ticket
        except Exception as e:
            print(f"Erro ao deletar o ingresso {e}")
            raise e
        finally:
            self.repository.session.close()
