
import tkinter as tk
from Server import Server
import threading

class GUIServer:
    """
    A graphical user interface (GUI) for managing and displaying logs from the SQL server.

    This class provides a window with buttons to start and stop the server, and a text area to display server logs in real-time. 
    It interacts with an instance of the `Server` class, running the server in a separate thread to prevent blocking the GUI.

    Attributes:
        root (tkinter.Tk): The main window of the application.
        window (tkinter.Toplevel): The separate top-level window for the server GUI.
        server (Server): An instance of the `Server` class that this GUI manages.
        btnStart (tkinter.Button): Button to start the server.
        btnStop (tkinter.Button): Button to stop the server.
        txtLogs (tkinter.Text): Text area to display server logs.
    """
    def __init__(self, root):
        """
        Initializes the `GUIServer` object.

        Args:
            root (tkinter.Tk): The main application window.
        """
        self.root = root
        self.window = tk.Toplevel(self.root)
        self.setupGUI()
        # Create an instance of the Server class and pass the GUI instance to it
        self.server = Server(self)  # Pass GUI instance to the Server

    def showLogs(self, log):
        """
        Displays a log message in the GUI's text area.

        This method uses `root.after` to ensure that the GUI update is performed in the main Tkinter thread, making it thread-safe.

        Args:
            log (str): The log message to be displayed.
        """
        # Thread-safe GUI update
        self.root.after(0, lambda: self._insert_log(log))
    
    def _insert_log(self, log):
        """
        Inserts the log message into the text area and scrolls to the end.

        This is the actual method that modifies the GUI elements and is called by `showLogs` using `root.after`.

        Args:
            log (str): The log message to be inserted.
        """
        self.txtLogs.insert(tk.END, log + "\n")
        self.txtLogs.see(tk.END)

    def startAction(self):
        """
        Handles the action when the "Start" button is clicked.

        This method displays a "Server started." message in the logs and starts the `Server` in a separate daemon thread. 
        Using a daemon thread ensures that the server thread will automatically exit when the main GUI application closes.
        """
        try:
            self.showLogs("Server started.")
            # Start the server in a separate thread
            serverThread = threading.Thread(target=self.server.startServer, daemon=True)
            serverThread.start()

        except Exception as e:
            self.showLogs(f"Error when starting server: {e}")

    def stopAction(self):
        """
        Handles the action when the "Stop" button is clicked.

        This method calls the `stopServer` method of the `Server` instance and displays a "Server has been stopped." message in the logs.
        Note that stopping the server might take a moment depending on the server's current activity and how the `stopServer` method is implemented.
        """
        self.server.stopServer()
        self.showLogs("Server has been stopped.")
    
    def setupGUI(self):
        """
        Sets up the graphical user interface elements within the window.

        This method creates and arranges labels, buttons (Start and Stop), and a text area to display server logs using the Tkinter grid layout
        manager. It also configures column weights to ensure proper resizing.
        """
        self.window.title("Server SQL Logs Form")
        self.window.geometry("400x400+100+100")
        frame = tk.Frame(self.window)
        frame.grid(row=0, column=0, columnspan=4, padx=10, pady=30, sticky='ew')

        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)
        frame.columnconfigure(3, weight=1)

        # Correct assignment: store buttons in instance if needed later
        self.btnStart = tk.Button(frame, text="Start", width=4, command=self.startAction)
        self.btnStart.grid(row=0, column=0, sticky='ew', padx=10)

        self.btnStop = tk.Button(frame, text="Stop", width=4, command=self.stopAction)
        self.btnStop.grid(row=0, column=3, sticky='ew', padx=10)

        self.txtLogs = tk.Text(self.window, width=50, height=17, wrap=tk.WORD)
        self.txtLogs.grid(row=2, column=0, padx=15, pady=10)
