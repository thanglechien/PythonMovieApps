import pyodbc
from Movie import Movie

def getConnection():
    """
    Establishes a connection to the SQL Server database.

    This function creates a connection string and uses pyodbc to connect to the database.  The connection string specifies the driver, 
    server, database name, and uses trusted authentication.

    Returns:
        pyodbc.Connection: A pyodbc Connection object representing the database connection.
    """
    #create a connection string to the database
    #conn_str = 'DRIVER={SQL Server};SERVER=localhost;DATABASE=MovieData;Trusted_Connection=yes'
    conn_str = "DRIVER={SQL Server};SERVER=THANG;DATABASE=MovieData;Trusted_Connection=yes"
    conn = pyodbc.connect(conn_str)
    return conn

# get a movie from the database by its movieID
def getMovieById(movieID):
    """
    Retrieves a movie from the database by its MovieID.

    This function establishes a database connection, executes a SELECT query to retrieve a movie with the specified MovieID, 
    and returns a `Movie` object representing the retrieved movie.

    Args:
        movieID (int): The MovieID of the movie to retrieve.

    Returns:
        Movie: A `Movie` object if the movie is found, None otherwise.

    Raises:
        pyodbc.Error: If a database error occurs during the operation.
        Exception: For any other unexpected error.
    """
    try:    
        # establish a connection with the Database
        conn = getConnection()

        # create a query string
        query = "SELECT MovieID, Title, Director, YearReleased, Description, GenreID FROM Movies WHERE MovieID=?"

        # create a cursor on the connection (a cursor is an object used to interact with the database)
        cursor = conn.cursor()

        # execuate the query
        cursor.execute(query, (movieID,))

        # fetch one record
        row = cursor.fetchone()
    except pyodbc.Error as e:
        print("Database error: ", e)
    except Exception as e:
        print("Unexpected error: ", e)
    finally:
        if conn:
            conn.close()    # close connection

    # create a movie object
    if row:
        movie = Movie(row[1], row[2], row[3], row[4], row[5], row[0])

    return movie

# update a movie
def updateAMovie(movie):
    """
    Updates an existing movie's information in the database.

    This function establishes a database connection, executes an UPDATE query
    to modify the movie's details, and commits the changes.

    Args:
        movie (Movie): A `Movie` object containing the updated movie information.

     Raises:
        pyodbc.Error: If a database error occurs during the operation.
        Exception: For any other unexpected error.
    """
    try:    
        # establish a connection with the Database
        conn = getConnection()
        # create a query string
        update_query = f"""
            UPDATE Movies SET 
                Title = ?,
                Director = ?,
                YearReleased = ?,
                Description = ?,
                GenreID = ?
            WHERE MovieID = ?
        """
        values = (movie.title, movie.director, movie.yearReleased, movie.description, movie.genreID, movie.movieID)

        # create a cursor on the connection (a cursor is an object used to interact with the database)
        cursor = conn.cursor()

        # execuate the query
        cursor.execute(update_query, values)
        # save all changes to the database
        conn.commit()
    except pyodbc.Error as e:
        print("Database error: ", e)
    except Exception as e:
        print("Unexpected error: ", e)
    finally:
        if conn:
            conn.close()    # close connection


# insert a movie into the database
def insertAMovie(movie):
    """
    Inserts a new movie into the database.

    This function establishes a database connection, executes an INSERT query
    to add the movie to the database, and commits the changes.

    Args:
        movie (Movie): A `Movie` object containing the movie's information.

    Raises:
        pyodbc.Error: If a database error occurs during the operation.
        Exception: For any other unexpected error.
    """
    try:
        # establish a connection with the Database
        conn = getConnection()
        # create a query string
        insert_query = f"""
            INSERT INTO Movies (Title, Director, YearReleased, Description, GenreID)
            VALUES (?, ?, ?, ?, ?)
        """
        values = (movie.title, movie.director, movie.yearReleased, movie.description, movie.genreID)

        # create a cursor on the connection (a cursor is an object used to interact with the database)
        cursor = conn.cursor()

        # execuate the query
        cursor.execute(insert_query, values)
        conn.commit()   # save all changes to the database
    except pyodbc.Error as e:
        print("Database error: ", e)
    except Exception as e:
        print("Unexpected error: ", e)
    finally:
        if conn:
            conn.close()    # close connection

# delete a movie by movieID
def deleteAMovie(movieID):
    """
    Deletes a movie from the database by its MovieID.

    This function establishes a database connection, executes a DELETE query
    to remove the movie with the specified MovieID, and commits the changes.

    Args:
        movieID (int): The MovieID of the movie to delete.

    Raises:
        pyodbc.Error: If a database error occurs during the operation.
        Exception: For any other unexpected error.
    """
    try:
        # establish a connection with the Database
        conn = getConnection()
        # create a query string
        delete_query = "DELETE FROM Movies WHERE MovieID =?"

        # create a cursor on the connection (a cursor is an object used to interact with the database)
        cursor = conn.cursor()

        # execuate the query
        cursor.execute(delete_query, (movieID,))
        conn.commit()   # save all changes to the database
    except pyodbc.Error as e:
        print("Database error: ", e)
    except Exception as e:
        print("Unexpected error: ", e)
    finally:
        if conn:
            conn.close()    # close connection
