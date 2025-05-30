from modules.event import CreateEventRepository, CreateEventDTO

class CreateEventUseCase:
    def __init__(self, repository=None):
        self.repository = repository or CreateEventRepository()
    def execute(self, data: CreateEventDTO):
        try:
            event = self.repository.create(data)
            print(f"Evento {event.name} criado com sucesso.")
            return event
        except Exception as e:
            print(f"Erro ao criar evento: {e}")
            raise e
        finally:
            self.repository.session.close()
