from datetime import datetime
from Service import Service
from FileHandler import FileHandler
from Query import Query

class SaveLogsService(Service):
    """
    Handles saving query logs to a file.

    This class inherits from the `Service` abstract base class and implements the
    `doWork` method to save query logs. It interacts with the `FileHandler`
    class to manage file operations and the `Query` class to represent individual logs.
    """
    def __init__(self, command, gui_server=None):
        """
        Initializes the SaveLogsService object.

        Args:
            command (str): The command string to be logged.
            gui_server (GUIServer, optional): A reference to the GUIServer instance. Defaults to None.
        """
        super().__init__(command)
        self.gs = gui_server  # Reference to GUIServer
        self.logs = FileHandler.getData("LogsOfQueries.txt")  # List of Query objects
        self.query = None

    def doWork(self):
        return self.saveLogs(self.command)

    def saveLogs(self, command):
        """
        Saves the query log to a file.

        This method creates a timestamp,  formats the command, creates a `Query` object, adds it to the log list,
        saves the updated log to the file using `FileHandler.save()`, and formats the log entry for display.

        Args:
            command (str): The command string to be saved in the log.

        Returns:
            str:  The formatted log entry string.
        """
        # Create a timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Remove leading '#' if present
        if command.startswith("#"):
            command = command[1:]

        # Create a new Query object
        self.query = Query(timestamp, command)

        # Add to logs
        self.logs.append(self.query)

        # Save updated logs to file
        FileHandler.save(self.logs)

        # Convert timestamp string to datetime
        datetime_obj = datetime.strptime(self.query.timestamp, "%Y%m%d_%H%M%S")
        # Make a content to return to processor to display
        content = f"{datetime_obj} - command: {self.query.queryDetails}"
        return content
        

    