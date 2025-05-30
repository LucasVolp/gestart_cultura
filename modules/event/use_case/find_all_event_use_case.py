from modules.event import FindAllEventsRepository

class FindAllEventUseCase:
    def __init__(self, repository=None):
        self.repository = repository or FindAllEventsRepository()
    def execute(self):
        try:
            events = self.repository.findAll()
            if not events:
                print("Nenhum evento encontrado.")
                return []
            return events
        except Exception as e:
            print(f"Erro ao buscar eventos: {e}")
            raise e
        finally:
            self.repository.session.close()
