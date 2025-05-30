from modules.event import UpdateEventRepository, UpdateEventDTO, FindEventByIdRepository

class UpdateEventUseCase:
    def __init__(self, repository=None, findEventById=None):
        self.repository = repository or UpdateEventRepository()
        self.findEventById = findEventById or FindEventByIdRepository()
    def execute(self, id, data: UpdateEventDTO):
        try:
            eventExists = self.findEventById.findById(id)
            if not eventExists:
                raise ValueError(f"Evento não encontrado.")
            event = self.repository.update(id, data)
            print(f"Evento {event.name} atualizado com sucesso.")
            return event
        except Exception as e:
            print(f"Erro ao atualizar evento: {e}")
            raise e
        finally:
            self.repository.session.close()
