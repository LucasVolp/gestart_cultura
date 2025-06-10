from modules.event import CreateEventRepository, CreateEventDTO
from fastapi import HTTPException

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
            if not event:
                raise HTTPException(status_code=400, detail="Erro ao criar evento. Verifique os dados fornecidos.")
            print(f"Evento {event.name} criado com sucesso.")
            return event
        except Exception as e:
            print(f"Erro ao criar evento: {e}")
            raise HTTPException(status_code=500, detail=f"Erro ao criar evento")
        finally:
            self.repository.session.close()
