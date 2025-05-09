class Movie:
    """
    Represents a movie entity.

    This class stores information about a movie, including its ID, title,
    director, release year, description, and genre ID.
    """
    #constructors
    def __init__(self, title, director, yearReleased, description, genreID, movieID=None):
        """
        Initializes a Movie object.

        Args:
            title (str): The title of the movie.
            director (str): The director of the movie.
            yearReleased (int): The year the movie was released.
            description (str): A brief description of the movie.
            genreID (int): The ID of the movie's genre.
            movieID (int, optional): The unique ID of the movie. Defaults to None.
        """
        self.movieID = movieID
        self.title = title
        self.director = director
        self.yearReleased = yearReleased
        self.description = description
        self.genreID = genreID
    