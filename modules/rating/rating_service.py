from modules.rating import (
    CreateRatingUseCase,
    FindRatingByIdUseCase,
    FindAllRatingUseCase,
    UpdateRatingUseCase,
    DeleteRatingUseCase,
    CreateRatingDTO,
    UpdateRatingDTO
)

class RatingService:
    def __init__(self, CreateRatingUseCase = CreateRatingUseCase(), FindRatingByIdUseCase = FindRatingByIdUseCase(), FindAllRatingUseCase = FindAllRatingUseCase(), UpdateRatingUseCase = UpdateRatingUseCase(), DeleteRatingUseCase = DeleteRatingUseCase()):
        self.CreateRatingUseCase = CreateRatingUseCase
        self.FindRatingByIdUseCase = FindRatingByIdUseCase
        self.FindAllRatingUseCase = FindAllRatingUseCase
        self.UpdateRatingUseCase = UpdateRatingUseCase
        self.DeleteRatingUseCase = DeleteRatingUseCase

    def create(self, data: CreateRatingDTO):
        """
        Creates a new rating using the CreateRatingUseCase.

        Args:
            data: Data Transfer Object containing the rating information to be created.
        
        Returns:
            Created rating instance.
        """
        return self.CreateRatingUseCase.execute(data)
    
    def findAll(self):
        """
        Retrieves all ratings using the FindAllRatingUseCase.

        Returns:
            List of all rating instances.
        """
        return self.FindAllRatingUseCase.execute()
    
    def findOne(self, id: str):
        """
        Finds a rating by its ID using the FindRatingByIdUseCase.

        Args:
            id: The ID of the rating to be found.
        
        Returns:
            Rating instance with the specified ID.
        """
        return self.FindRatingByIdUseCase.execute(id)
    
    def update(self, id: str, data: UpdateRatingDTO):
        """
        Updates an existing rating using the UpdateRatingUseCase.

        Args:
            id: The ID of the rating to be updated.
            data: Data Transfer Object containing the updated rating information.
        
        Returns:
            Updated rating instance.
        """
        return self.UpdateRatingUseCase.execute(id, data)
    
    def remove(self, id: str):
        """
        Deletes a rating by its ID using the DeleteRatingUseCase.

        Args:
            id: The ID of the rating to be deleted.
        
        Returns:
            Confirmation of deletion.
        """
        return self.DeleteRatingUseCase.execute(id)
    

