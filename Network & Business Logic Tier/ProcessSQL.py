
from SQLSelectService import SQLSelectService
from SQLUpdateService import SQLUpdateService
from SQLInsertService import SQLInsertService
from SQLDeleteService import SQLDeleteService
from SaveLogsService import SaveLogsService

class ProcessSQL:
    """
    Processes SQL-like commands received from a client.

    This class receives data (assumed to be an SQL-like command) from a client, determines the type of command (SELECT, UPDATE, INSERT, DELETE),
    and uses the appropriate service class to handle the command. It also uses `SaveLogsService` to log the command.

    Attributes:
        data (str): The data (command string) received from the client.
        clientSocket (socket.socket): The socket object used to communicate with the client.
    """
    def __init__(self, clientSocket):
        """
        Initializes the `ProcessSQL` object.

        Args:
            clientSocket (socket.socket): The socket object for communicating with the client.  The constructor receives data from the client using
                                         this socket.
        """
        self.data = clientSocket.recv(1024).decode()
        self.clientSocket = clientSocket
    
    def process(self):
        """
        Processes the command and returns a result.

        This method parses the command, calls the appropriate service class (e.g., `SQLSelectService`, `SQLUpdateService`), and handles sending
        responses to the client for SELECT commands.  It also calls the `SaveLogsService` to log the command.

        Returns:
            str: The content to be logged by the server.  This is typically the command that was processed.
        """
        #process based on type of request
        if self.data.startswith("#select"):
            selectService = SQLSelectService(self.data)
            
            try:
                response = selectService.doWork()
                #send the response back to the client
                self.clientSocket.sendall(response.encode())
                print("Sent response back to client")
            except Exception as e:
                print(f"[ERROR] Exception during SQL processing: {e}")
        elif self.data.startswith("#update"):
            updateService = SQLUpdateService(self.data)
            try:
                updateService.doWork()
                print("Updated the database")
            except Exception as e:
                print(f"[ERROR] Exception during SQL processing: {e}")
        elif self.data.startswith("#insert"):
            insertService = SQLInsertService(self.data)
            insertService.doWork()
            print("Inserted a movie to the database")                 
        elif self.data.startswith("#delete"):
            deleteService = SQLDeleteService(self.data)
            deleteService.doWork()
            print("Deleted a movie to the database")
        else:
            self.clientSocket.sendall("Unknown command".encode())
        
        #handle saving and displaying logs
        saveService = SaveLogsService(self.data)
        content = saveService.doWork()
        #return this information to update the logs to server GUI
        return content


        

   

    