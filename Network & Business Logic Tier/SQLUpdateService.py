from Service import Service
import MovieDAO
from Movie import Movie

class SQLUpdateService(Service):
    """
    Handles updating movie data in the database.

    This class inherits from the `Service` abstract base class and implements the
    `doWork` method to perform the movie update operation. It uses the `MovieDAO`
    module to interact with the database.
    """
    #constructor
    def __init__(self, command):
        super().__init__(command)
    
    #override doWork()
    def doWork(self):
        """
        Updates movie data in the database.

        This method parses the command string to extract the movie data,
        creates a `Movie` object, and calls the `MovieDAO.updateAMovie()`
        method to update the corresponding record in the database.
        """
        #split the command
        parts = self.command.split("|")
        #create a movie
        movie = Movie(parts[1], parts[2], parts[3], parts[4], parts[5], parts[6])
        #call a MovieDAO method to update the database
        MovieDAO.updateAMovie(movie)

