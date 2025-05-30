from modules.event import FindAllEventsRepository

class FindAllEventUseCase:
    def __init__(self, repository=None):
        self.repository = repository or FindAllEventsRepository()
    def execute(self):
        """Returns all events from the database.

        Raises:
            e: Error while fetching events.

        Returns:
            _type_: List of Event model instances or an empty list if no events are found.
        """
        try:
            events = self.repository.findAll()
            if not events:
                print("Nenhum evento encontrado.")
                return []
            return events
        except Exception as e:
            print(f"Erro ao buscar eventos: {e}")
            raise e
        finally:
            self.repository.session.close()
