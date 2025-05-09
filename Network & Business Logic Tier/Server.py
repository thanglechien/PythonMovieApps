import socket
import threading
from concurrent.futures import ThreadPoolExecutor
from ProcessSQL import ProcessSQL

class Server:
    """
    A server class that listens for incoming client connections and processes their requests using a thread pool.

    This server binds to a specified host and port, accepts client connections, and delegates the handling of each client to 
    a separate thread managed by a 'ThreadPoolExecutor'. It interacts with an optional GUI to display server logs.

    Attributes:
        host (str): The IP address the server will listen on. Defaults to '127.0.0.1' (localhost).
        port (int): The port number the server will listen on. Defaults to 3202.
        running (bool): A flag indicating whether the server is currently running. Initialized to True.
        gui (object, optional): An optional GUI object with a `showLogs` method to display server activity. Defaults to None.
        executor (ThreadPoolExecutor): A thread pool used to manage the execution of client handling tasks. Initialized with a
        maximum of 50 worker threads.
    """
    def __init__(self, gui=None):
        """
        Initializes the `Server` object.

        Args:
            gui (object, optional): An optional GUI object with a `showLogs` method for displaying server logs. Defaults to None.
        """
        self.host = '127.0.0.1'
        self.port = 3202
        self.running = True
        self.gui = gui
        self.executor = ThreadPoolExecutor(max_workers=50)  # Thread pool

    def startServer(self):
        """
        Starts the server, making it listen for incoming client connections.

        This method creates a socket, binds it to the configured host and port, and starts listening for connections. It uses a non-blocking `accept()`
        call with a timeout to periodically check the `running` flag, allowing for graceful shutdown. Accepted client connections are submitted to the
        thread pool for handling. If a GUI object is provided, it displays a startup message in the logs.
        """
        self.running = True
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
            serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            serverSocket.bind((self.host, self.port))
            serverSocket.listen(5)
            serverSocket.settimeout(1.0)

            if self.gui:
                self.gui.showLogs(f"Server is running on {self.host}:{self.port}\n... Waiting for clients...")

            while self.running:
                try:
                    clientSocket, addr = serverSocket.accept()
                    #data = client_socket.recv(1024).decode()
                    # Submit the whole handling to thread pool - submit (function, arg1, arg2)
                    self.executor.submit(self.handleClient, clientSocket, addr)
                except socket.timeout:
                    continue
                except Exception as e:
                    print(f"Server error: {e}")

    def handleClient(self, clientSocket, addr):
        """
        Handles the communication with a connected client.

        This method is executed in a separate thread for each client. It creates a `ProcessSQL` object to manage the data exchange
        with the client and process any SQL commands received. 
        If a GUI object is available, it displays any data processed by `ProcessSQL`. Finally, it ensures the client socket is closed.

        Args:
            clientSocket (socket.socket): The socket object representing the connection to the client.
            addr (tuple): The address (IP address and port) of the connected client.
        """
        try:

            processor = ProcessSQL(clientSocket)
            data = processor.process()
            self.gui.showLogs(data)

        except socket.timeout:
            print("Client socket timed out waiting for data.")
        except Exception as e:
            print(f"Exception in handle_client: {e}")
        finally:
            clientSocket.close()


    def stopServer(self):
        """
        Stops the server gracefully.

        Sets the `running` flag to False, which will cause the server's main loop to terminate after the current `accept()` call (or timeout).
        It does not immediately terminate the handling of currently connected clients.
        The thread pool will also need to be shut down separately if immediate termination of client handling is required.
        """
        self.running = False