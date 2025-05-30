from modules.event import UpdateEventRepository, UpdateEventDTO, FindEventByIdRepository

class UpdateEventUseCase:
    def __init__(self, repository=None, findEventById=None):
        self.repository = repository or UpdateEventRepository()
        self.findEventById = findEventById or FindEventByIdRepository()
    def execute(self, id: str, data: UpdateEventDTO):
        """Update an existing event in the database.

        Args:
            id (str): ID of the event to be updated.
            data (UpdateEventDTO): Data transfer object containing the updated event data.

        Raises:
            ValueError: If the event with the given ID does not exist.
            e: Error while updating the event.

        Returns:
            _type_: Updated Event model instance or None if not found.
        """
        try:
            eventExists = self.findEventById.findById(id)
            if not eventExists:
                raise ValueError(f"Evento não encontrado.")
            event = self.repository.update(eventExists, data)
            print(f"Evento {event.name} atualizado com sucesso.")
            return event
        except Exception as e:
            print(f"Erro ao atualizar evento: {e}")
            raise e
        finally:
            self.repository.session.close()
