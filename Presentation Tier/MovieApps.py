#from a Filename python import a classname or method

import tkinter as tk
from GUIClient import GUIClient
from GUIServer import GUIServer

def main():
    """
    Main function to initialize and run the GUI application.

    This function creates the main tkinter window, hides it,
    initializes the client and server GUI components, and
    starts the tkinter event loop.
    """
    root = tk.Tk() # Creates the main tkinter window (root window).
    root.withdraw()  # Hides the main window.  This is often done when you don't want the default tkinter window.

    #start the client GUI
    GUIClient(root)
    
    #start the server GUI
    GUIServer(root)

    root.mainloop()
    
if __name__ == "__main__":
    main()