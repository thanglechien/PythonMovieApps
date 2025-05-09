
import socket
from Movie import Movie

class Client:
    """
    A client class responsible for communicating with a movie database server.

    This class handles establishing a network connection, sending commands to the server, and processing the server's responses. It interacts with
    a `clientGUI` object to update the graphical user interface based on
    the server's replies.

    Attributes:
        clientSocket (socket.socket): The socket object used for network communication with the server. Initialized to None.
        clientGUI (GUIClient): An instance of the `GUIClient` class, used to update the user interface.
    """
    def __init__(self, clientGUI):
        """
        Initializes the `Client` object.

        Args:
            clientGUI (GUIClient): An instance of the `GUIClient` class that this client will interact with to update the UI.
        """
        self.clientSocket = None
        self.clientGUI = clientGUI

    def sendCommand(self, command):
        """
        Sends a command to the movie database server.

        This method first establishes a connection to the server, then encodes and sends the provided command. If the command is a "#select" command,
        it waits for and processes the server's response, updating the GUI with the retrieved movie details. Finally, it disconnects from the server.

        Args:
            command (str): The command string to be sent to the server.
                           Commands are expected to be prefixed with a '#'(e.g., "#select|1", "#insert|...").
        """
        try:
            #connect to the server
            self.connectToServer()
            #send the command to the server
            self.clientSocket.sendall(command.encode())  # Send command to server
            if command.startswith("#select"):
                response = self.clientSocket.recv(1024).decode()  # Receive response from server up to 1024 bytes of data
                if response:
                    parts = response.split("|")
                    if len(parts) == 6:
                        movie = Movie(*parts)
                self.clientGUI.updateGUI(movie)
            #disconnect
            self.disconnectFromServer()
        except Exception as e:
            print(f"Error sending command: {e}")
    
    def connectToServer(self, host="127.0.0.1", port=3202):
        """
        Establishes a connection to the movie database server.

        This method creates a socket object and attempts to connect to the specified host and port.

        Args:
            host (str, optional): The IP address or hostname of the server. Defaults to "127.0.0.1" (localhost).
            port (int, optional): The port number on which the server is listening. Defaults to 3202.
        """
        try:
            # Create a socket and connect to the server
            self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.clientSocket.connect((host, port))
            print("Connected to the server.")
        except Exception as e:
            print(f"Error connecting to server: {e}")
    
    def disconnectFromServer(self):
        """
        Closes the connection to the movie database server.

        If there is an active socket connection, this method closes it.
        """
        if self.clientSocket:
            self.clientSocket.close()
            print("Connection closed.")
        else:
            print("No active connection.")