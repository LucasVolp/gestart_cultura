from modules.event import DeleteEventRepository, FindEventByIdRepository

class DeleteEventUseCase:
    def __init__(self, repository=None, FindEventByIdRepo=None):
        self.repository = repository or DeleteEventRepository()
        self.findEventByIdRepo = FindEventByIdRepo or FindEventByIdRepository()
    def execute(self, id):
        """Delete an event by its ID from the database.

        Args:
            id (_type_): ID of the event to be deleted.

        Raises:
            ValueError: If the event with the given ID does not exist.
            e: Error while deleting the event.

        Returns:
            _type_: Deleted Event model instance or None if not found.
        """        
        try:
            eventExists = self.findEventByIdRepo.findById(id)
            if not eventExists:
                raise ValueError(f"Evento não encontrado.")
            event = self.repository.delete(eventExists)
            if event:
                print(f"Evento {event.name} deletado com sucesso.")
            return event
        except Exception as e:
            print(f"Erro ao deletar evento: {e}")
            raise e
        finally:
            self.repository.session.close()
