import logging
from uuid import UUID

class Rating:
    def __init__(self, id: UUID, rate: int, comment: str):
        self.__id = id
        self.__rate = rate
        self.__comment = comment

    @property
    def id(self) -> UUID:
        return self.__id

    @property
    def rate(self) -> int:
        return self.__rate

    @property
    def comment(self) -> str:
        return self.__comment

    @rate.setter
    def rate(self, rate: int) -> None:
        try:
            if rate < 1 or rate > 5:
                raise ValueError("A nota deve ser entre 1 e 5.")
            self.__rate = rate
        except ValueError as e:
            logging.error(f"Erro: {str(e)}")
            raise

    @comment.setter
    def comment(self, comment: str) -> None:
        try:
            if not comment.strip():
                raise ValueError("Comentário não pode ser vazio.")
            self.__comment = comment
        except ValueError as e:
            logging.error(f"Erro: {str(e)}")
            raise
        