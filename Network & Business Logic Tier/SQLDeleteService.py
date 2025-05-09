from Service import Service
import MovieDAO

class SQLDeleteService(Service):
    """
    Handles deleting movie data from the database.

    This class inherits from the `Service` abstract base class and implements the
    `doWork` method to perform the movie deletion operation. It uses the
    `MovieDAO` module to interact with the database.
    """
    
    def __init__(self, command):
        super().__init__(command)
    
    def doWork(self):
        """
        Deletes movie data from the database.

        This method parses the command string to extract the MovieID,
        and calls the `MovieDAO.deleteAMovie()` method to delete the
        corresponding record from the database.
        """
        #split the command
        parts = self.command.split("|")
        #get the movieID
        movieID = parts[1]
        #query the database to delete the movie by ID
        MovieDAO.deleteAMovie(movieID)
