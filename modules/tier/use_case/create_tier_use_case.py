from modules.tier.repository import CreateTierRepository, FindTierByNameRepository, FindTiersByEventRepository
from modules.event.repository import FindEventByIdRepository
from modules.tier.dto import CreateTierDTO
from fastapi import HTTPException

class CreateTierUseCase:
    def __init__(self, repository=None, findTierByNameRepo=None, findTiersByEvent=None, findEventById=None):
        self.repository = repository or CreateTierRepository()
        self.findTierByName = findTierByNameRepo or FindTierByNameRepository()
        self.findTiersByEvent = findTiersByEvent or FindTiersByEventRepository()
        self.findEventById = findEventById or FindEventByIdRepository()
        
    def execute(self, data: CreateTierDTO):
        """Executes the use case to create a new tier.

        Args:
            data (CreateTierDTO): Data Transfer Object containing the tier information to be created.

        Raises:
            HTTPException: If a tier with the same name already exists, if the event doesn't exist,
                          or if the tier amount exceeds available capacity.

        Returns:
            Tier: Created Tier model instance.
        """
        try:

            event = self.findEventById.findById(data.eventId)
            if not event:
                raise HTTPException(status_code=404, detail=f"Evento com ID {data.eventId} não encontrado.")
 
            existingTiers = self.findTiersByEvent.findByEventId(data.eventId)

            tierExists = self.findTierByName.findByName(data.name)
            if tierExists and tierExists.eventId == data.eventId:
                raise HTTPException(status_code=400, detail=f"Já existe um tier com o nome '{data.name}' para este evento.")

            totalAmountAllocated = sum(tier.amount for tier in existingTiers)
            availableSize = event.size - totalAmountAllocated
            
            if data.amount > availableSize:
                raise HTTPException(
                    status_code=400, 
                    detail=f"Quantidade solicitada ({data.amount}) excede a capacidade disponível do evento ({availableSize} de {event.size} total)."
                )

            tier = self.repository.create(data)
            print(f"Tier '{tier.name}' criado com sucesso. Capacidade restante: {availableSize - data.amount}")
            return tier
            
        except HTTPException as e:
            print(f"Erro ao criar tier: {e.detail}")
            raise e
        except Exception as e:
            print(f"Erro ao criar tier: {e}")
            raise HTTPException(status_code=500, detail="Erro interno do servidor ao criar tier.")
        finally:
            self.repository.session.close()
            if hasattr(self.findTiersByEvent, 'session'):
                self.findTiersByEvent.session.close()
            if hasattr(self.findEventById, 'session'):
                self.findEventById.session.close()
            if hasattr(self.findTierByName, 'session'):
                self.findTierByName.session.close()
