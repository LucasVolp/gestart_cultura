from models.models import Status
from modules.rating.repository import CreateRatingRepository
from modules.rating.dto import CreateRatingDTO
from modules.user.repository import FindUserByIdRepository
from modules.event.repository import FindEventByIdRepository
from modules.ticket.repository import CheckUserTicketForEventRepository
from fastapi import HTTPException

class CreateRatingUseCase:
    def __init__(self, repository=None, findUserById=None, findEventById=None, checkUserTicketForEvent=None):
        self.repository = repository or CreateRatingRepository()
        self.findUserById = findUserById or FindUserByIdRepository()
        self.findEventById = findEventById or FindEventByIdRepository()
        self.checkUserTicketForEvent = checkUserTicketForEvent or CheckUserTicketForEventRepository()

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
            event = self.findEventById.findById(data.eventId)

            if not user:
                raise HTTPException(status_code=404, detail=f"Usuário com ID {data.userId} não encontrado.")
                        
            if not event:
                raise HTTPException(status_code=404, detail=f"Evento com ID {data.eventId} não encontrado.")
            
            if not self.checkUserTicketForEvent.userHasTicketForEvent(data.userId, data.eventId):
                raise HTTPException(status_code=400, detail="Usuário não possui ingresso para este evento.")

            if event.status != Status.CLOSED:
                raise HTTPException(status_code=400, detail="Avaliações só podem ser feitas após o evento ser fechado.")

            for eventRating in event.ratings:
                if eventRating.userId == data.userId:
                    raise HTTPException(status_code=400, detail="Usuário já avaliou este evento.")

            rating = self.repository.create(data)
            print(f"Avaliação '{rating.id}' criada com sucesso por {user.name} para o evento {event.name}.")
            return rating
            
        except HTTPException as e:
            print(f"Erro ao criar avaliação: {e.detail}")
            raise e
        except Exception as e:
            print(f"Erro ao criar avaliação: {e}")
            raise HTTPException(status_code=400, detail="Erro ao criar avaliação.")
        finally:
            self.repository.session.close()
            if hasattr(self.findUserById, 'session'):
                self.findUserById.session.close()
            if hasattr(self.findEventById, 'session'):
                self.findEventById.session.close()
            if hasattr(self.checkUserTicketForEvent, 'session'):
                self.checkUserTicketForEvent.session.close()
