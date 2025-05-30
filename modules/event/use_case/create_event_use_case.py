from modules.event import CreateEventRepository, CreateEventDTO

class CreateEventUseCase:
    def __init__(self, repository=None):
        self.repository = repository or CreateEventRepository()
    def execute(self, data: CreateEventDTO):
        """Create a new event in the database.

        Args:
            data (CreateEventDTO): Data of the event to be created.

        Raises:
            e: Error while creating the event.

        Returns:
            _type_: Created Event model instance.
        """
        try:
            event = self.repository.create(data)
            print(f"Evento {event.name} criado com sucesso.")
            return event
        except Exception as e:
            print(f"Erro ao criar evento: {e}")
            raise e
        finally:
            self.repository.session.close()
