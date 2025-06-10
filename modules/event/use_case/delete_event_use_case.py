from modules.event import DeleteEventRepository, FindEventByIdRepository
from fastapi import HTTPException

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
                raise HTTPException(status_code=404, detail=f"Evento com ID {id} não encontrado.")
            print(f"Evento encontrado: {eventExists.name}. Deletando...")
            if not eventExists.producers:
                event = self.repository.delete(id)
                print(f"Evento {eventExists.name} deletado com sucesso.")
                raise HTTPException(status_code=200, detail=f"Evento {eventExists.name} deletado com sucesso.")
            event = self.repository.softDelete(id)
            if event:
                print(f"Evento {eventExists.name} deletado com sucesso.")
                raise HTTPException(status_code=200, detail=f"Evento {eventExists.name} deletado com sucesso.")
        except HTTPException as e:
            print(f"Erro ao deletar evento: {e.detail}")
            raise e
        except Exception as e:
            print(f"Erro ao deletar evento: {e}")
            raise HTTPException(status_code=500, detail=f"Erro ao deletar evento")
        finally:
            self.repository.session.close()
