import os
from Query import Query

class FileHandler:
    """
    Handles reading and writing query data from/to files.

    This class provides static methods for loading query data from a file and saving query data to a file.
    It interacts with the `Query` class to represent individual queries.
    """
    queries = []

    @staticmethod
    def getData(fileName):
        """
        Reads query data from a file.

        The file should contain the number of queries on the first line,
        followed by each query on a new line in the format "timestamp#queryDetails".

        Args:
            fileName (str): The name of the file to read from.

        Returns:
            list: A list of `Query` objects, or an empty list if the file
                  does not exist, an I/O error occurs, or the file format is invalid.
                  Returns None if file is empty.
        """
        FileHandler.queries = []

        # Try to open the file
        try:
            with open(fileName, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            print("File Not Found.")
            return []
        except IOError:
            print("Unknown IO error occurred.")
            return []
        except Exception as e:
            print("An unknown error occurred:", e)
            return []

        # Try to read the size from the first line
        try:
            size = int(lines[0].strip())
            FileHandler.queries = [None] * size
        except (ValueError, IndexError):
            print("File Format Error")
            return []

        # Process each line
        index = 0
        for line in lines[1:]:
            parts = line.strip().split("#", 1)
            if len(parts) == 2 and index < size:
                timestamp = parts[0].strip()
                queryDetails = parts[1].strip()
                FileHandler.queries[index] = Query(timestamp, queryDetails)
                index += 1

        print("Log Added.")
        return FileHandler.queries

    @staticmethod
    def save(queriesToSave):
        """
        Saves query data to a file.

        The file will be formatted with the number of queries on the first line,
        followed by each query on a new line in the format "timestamp#queryDetails".

        Args:
            queriesToSave (list): A list of `Query` objects to save.
        """
        try:
            with open("LogsOfQueries.txt", 'w') as file:
                file.write(f"{len(queriesToSave)}\n")
                for query in queriesToSave:
                    file.write(f"{query.writeAsRecord()}\n")
        except IOError as e:
            print("Error saving file:", e)
