from modules.ticket import UpdateTicketRepository, UpdateTicketDTO, FindTicketByIdRepository

class UpdateTicketUseCase:
    def __init__(self, repository=None, FindTicketByIdRepo=None):
        self.repository = repository or UpdateTicketRepository()
        self.findTicketByIdRepo = FindTicketByIdRepo or FindTicketByIdRepository()

    def execute(self, id, data: UpdateTicketDTO):
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
