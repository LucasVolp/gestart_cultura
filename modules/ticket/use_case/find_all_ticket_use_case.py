from modules.ticket import FindAllTicketsRepository

class FindAllTicketUseCase:
    def __init__(self, repository=None):
        self.repository = repository or FindAllTicketsRepository()
    def execute(self):
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
