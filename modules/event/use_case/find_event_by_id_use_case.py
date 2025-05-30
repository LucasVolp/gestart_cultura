from modules.event import FindEventByIdRepository

class FindEventByIdUseCase:
    def __init__(self, repository=None):
        self.repository = repository or FindEventByIdRepository()
    def execute(self, id):
        try:
            event = self.repository.findById(id)
            if not event:
                raise ValueError("Evento não encontrado.")
            return event
        except Exception as e:
            print(f"Erro ao buscar evento: {e}")
            raise e
        finally:
            self.repository.session.close()
