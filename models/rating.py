from uuid import UUID

class Rating:
    def __init__(self, id: UUID, rate: int, comment: str):
        self.__id = id
        self.__rate = rate
        self.__comment = comment

    @property
    def id(self) -> str:
        return self.__id

    @property
    def rate(self) -> int:
        return self.__rate

    @property
    def comment(self) -> str:
        return self.__comment

    @rate.setter
    def rate(self, rate: int) -> None:
        self.__rate = rate

    @comment.setter
    def comment(self, comment: str) -> None:
        self.__comment = comment