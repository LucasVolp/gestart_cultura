from modules.tier.repository import UpdateTierRepository, FindTierByIdRepository, FindTierByNameRepository, FindTiersByEventRepository
from modules.event.repository import FindEventByIdRepository
from modules.tier.dto import UpdateTierDTO
from fastapi import HTTPException

class UpdateTierUseCase:
    def __init__(self, repository=None, findTierByIdRepo=None, findTierByNameRepo=None, findTiersByEventRepo=None, findEventByIdRepo=None):
        self.repository = repository or UpdateTierRepository()
        self.findTierByIdRepo = findTierByIdRepo or FindTierByIdRepository()
        self.findTierByNameRepo = findTierByNameRepo or FindTierByNameRepository()
        self.findTiersByEventRepo = findTiersByEventRepo or FindTiersByEventRepository()
        self.findEventByIdRepo = findEventByIdRepo or FindEventByIdRepository()
        
    def execute(self, id: str, data: UpdateTierDTO):
        """Updates a tier by its ID with the provided data.

        Args:
            id (str): ID of the tier to be updated.
            data (UpdateTierDTO): Data transfer object containing the updated tier information.

        Raises:
            HTTPException: If the tier with the given ID does not exist or if an error occurs.

        Returns:
            Tier: Updated Tier model instance if successful.
        """
        try:
            tierExists = self.findTierByIdRepo.findById(id)
            eventId = data.eventId if data.eventId is not None else tierExists.eventId
            event = self.findEventByIdRepo.findById(eventId)
            
            if not tierExists:
                raise HTTPException(status_code=404, detail="Tier não encontrado.")

            if not event:
                raise HTTPException(status_code=404, detail=f"Evento com ID {eventId} não encontrado.")

            if data.name is not None and data.name != tierExists.name:
                conflictingTier = self.findTierByNameRepo.findByName(data.name)
                if conflictingTier and conflictingTier.eventId == eventId and conflictingTier.id != tierExists.id:
                    raise HTTPException(status_code=400, detail=f"Já existe um tier com o nome '{data.name}' para este evento.")

            if data.amount is not None:
                existingTiers = self.findTiersByEventRepo.findByEventId(eventId)
                totalAmountAllocated = sum(tier.amount for tier in existingTiers if tier.id != tierExists.id) 
                availableSize = event.size - totalAmountAllocated
                
                if data.amount > availableSize:
                    raise HTTPException(
                        status_code=400, 
                        detail=f"Quantidade solicitada ({data.amount}) excede a capacidade disponível do evento ({availableSize} de {event.size} total)."
                    )

            startDate = data.startDate if data.startDate is not None else tierExists.startDate
            endDate = data.endDate if data.endDate is not None else tierExists.endDate

            if data.startDate is not None and data.startDate >= event.date:
                raise HTTPException(
                    status_code=400, 
                    detail=f"A data de início do tier ({data.startDate}) deve ser anterior à data do evento ({event.date})."
                )
            
            if data.endDate is not None and data.endDate >= event.date:
                raise HTTPException(
                    status_code=400, 
                    detail=f"A data de fim do tier ({data.endDate}) deve ser anterior à data do evento ({event.date})."
                )
            
            if startDate >= endDate:
                raise HTTPException(
                    status_code=400, 
                    detail="A data de início do tier deve ser anterior à data de fim."
                )

            tier = self.repository.update(tierExists, data)
            print(f"Tier {tier.name} atualizado com sucesso.")
            return tier
        except HTTPException as e:
            print(f"Erro ao atualizar tier: {e.detail}")
            raise e
        except Exception as e:
            print(f"Erro ao atualizar tier: {e}")
            raise HTTPException(status_code=500, detail="Erro ao atualizar tier.")
        finally:
            self.repository.session.close()
            if hasattr(self.findTierByNameRepo, 'session'):
                self.findTierByNameRepo.session.close()
            if hasattr(self.findTiersByEventRepo, 'session'):
                self.findTiersByEventRepo.session.close()
            if hasattr(self.findEventByIdRepo, 'session'):
                self.findEventByIdRepo.session.close()
