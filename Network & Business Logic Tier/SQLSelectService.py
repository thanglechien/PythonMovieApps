from Service import Service
import MovieDAO

class SQLSelectService(Service):
    """
    Handles the retrieval of movie data from the database based on a MovieID.

    This class inherits from the `Service` abstract base class and implements the
    `doWork` method to perform the movie selection operation.  It uses the
    `MovieDAO` module to interact with the database.

    Attributes:
        command (str):  The command string containing the MovieID to select.
                        The expected format is "#select|MovieID".
    """
    def __init__(self, command):
        super().__init__(command)
    
    def doWork(self):
        """
        Retrieves movie data from the database and formats it as a string.

        This method parses the command string to extract the MovieID,
        uses the `MovieDAO.getMovieById()` method to fetch the movie data,
        and formats the movie attributes into a string separated by '|'.

        Returns:
            str: A string containing the movie data in the format
                 "title|director|yearReleased|description|genreID|movieID".
        """
        #split the command
        parts = self.command.split("|")
        #get the movieID
        movieID = parts[1]
        #query the database to get the movie by ID
        movie = MovieDAO.getMovieById(movieID)
        #create the command string
        response = f"{movie.title}|{movie.director}|{movie.yearReleased}|{movie.description}|{movie.genreID}|{movie.movieID}"
        return response

