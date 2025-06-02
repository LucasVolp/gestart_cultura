from modules.rating.repository import CreateRatingRepository
from modules.rating.dto import CreateRatingDTO
from modules.user.repository import FindUserByIdRepository
from modules.event.repository import FindEventByIdRepository
from fastapi import HTTPException

class CreateRatingUseCase:
    def __init__(self, repository=None, findUserById=None, findEventById=None):
        self.repository = repository or CreateRatingRepository()
        self.findUserById = findUserById or FindUserByIdRepository()
        self.findEventById = findEventById or FindEventByIdRepository()

    def execute(self, data: CreateRatingDTO):
        """Executes the use case to create a new rating.

        Args:
            data (CreateRatingDTO): Data Transfer Object containing the rating information to be created.

        Raises:
            HTTPException: If user or event doesn't exist, or if an error occurs during creation.

        Returns:
            Rating: Created Rating model instance.
        """
        try:
            user = self.findUserById.findById(data.userId)
            if not user:
                raise HTTPException(status_code=404, detail=f"Usuário com ID {data.userId} não encontrado.")

            event = self.findEventById.findById(data.eventId)
            if not event:
                raise HTTPException(status_code=404, detail=f"Evento com ID {data.eventId} não encontrado.")

            rating = self.repository.create(data)
            print(f"Avaliação '{rating.id}' criada com sucesso por {user.name} para o evento {event.name}.")
            return rating
            
        except HTTPException as e:
            print(f"Erro ao criar avaliação: {e.detail}")
            raise e
        except Exception as e:
            print(f"Erro ao criar avaliação: {e}")
            raise HTTPException(status_code=500, detail="Erro interno do servidor ao criar avaliação.")
        finally:
            self.repository.session.close()
            if hasattr(self.findUserById, 'session'):
                self.findUserById.session.close()
            if hasattr(self.findEventById, 'session'):
                self.findEventById.session.close()
