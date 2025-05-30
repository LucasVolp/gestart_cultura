from modules.event import DeleteEventRepository

class DeleteEventUseCase:
    def __init__(self, repository=None):
        self.repository = repository or DeleteEventRepository()
    def execute(self, id):
        try:
            result = self.repository.delete(id)
            print(f"Evento deletado com sucesso.")
            return result
        except Exception as e:
            print(f"Erro ao deletar evento: {e}")
            raise e
        finally:
            self.repository.session.close()
