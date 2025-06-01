from modules.event import FindEventByIdRepository
from fastapi import HTTPException

class FindEventByIdUseCase:
    def __init__(self, repository=None):
        self.repository = repository or FindEventByIdRepository()
    def execute(self, id: str):
        """
        Find an event by its ID in the database.

        Args:
            id (str): ID of the event to be found.

        Raises:
            ValueError: Event not found with the given ID.
            e: Error while fetching the event.

        Returns:
            _type_: Event model instance or None if not found.
        """
        try:
            event = self.repository.findById(id)
            if not event:
                raise HTTPException(status_code=404, detail=f"Evento com ID {id} não encontrado.")
            print(f"Evento com ID {id} encontrado: {event.name}")
            return event
        except Exception as e:
            print(f"Erro ao buscar evento: {e}")
            raise HTTPException(status_code=500, detail=f"Erro ao buscar evento")
        finally:
            self.repository.session.close()
