import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import ttk
from Client import Client

class GUIClient:
    """
    A graphical user interface (GUI) client for interacting with a movie database.

    This class provides a window with input fields for movie details (title, director, year, description, genre) and buttons to perform
    database operations (Select, Update, Insert, Delete) through a `Client` object.

    Attributes:
        root (tkinter.Tk): The main window of the application.
        window (tkinter.Toplevel): The separate top-level window for the client form.
        client (Client): An instance of the `Client` class responsible for communicating with the server.
        txtTitle (tkinter.Entry): Entry field for the movie title.
        txtDirector (tkinter.Entry): Entry field for the movie director.
        txtYear (tkinter.Entry): Entry field for the movie release year.
        txtDescription (tkinter.Text): Text area for the movie description.
        cbbGenre (ttk.Combobox): Combobox for selecting the movie genre.
        currentMovieID (int): Stores the ID of the currently displayed movie. Initialized to -1.
    """
    currentMovieID = -1
    def __init__(self, root):
        """
        Initializes the `GUIClient` object.

        Args:
            root (tkinter.Tk): The main application window.
        """
        self.root = root
        self.window = tk.Toplevel(self.root)
        self.setupGUI()
        self.client = Client(self)

    def selectAction(self):
        """
        Handles the "Select" button action.

        Prompts the user for a movie ID using a simple dialog and sends a "#select" command with the provided ID to the server through the `Client`.
        """
        # Ask for movie ID via simple dialog
        movie_id = simpledialog.askinteger("Movie ID", "Please enter the movie ID: ")
        if movie_id:
            #create a select command
            command = f"#select|{movie_id}"
            self.client.sendCommand(command)

    def updateAction(self):
        """
        Handles the "Update" button action.

        Retrieves the data from the input fields, constructs an "#update" command
        containing the movie details and the `currentMovieID`, and sends it to the server through the `Client`.
        """
        #get information from the inputs using get() to create a command
        genreList = self.cbbGenre['values']
        genreID = genreList.index(self.cbbGenre.get()) + 1 #convert genre name to genreID
        command = f"#update|{self.txtTitle.get()}|{self.txtDirector.get()}|{self.txtYear.get()}|{self.txtDescription.get('1.0', 'end-1c')}|{genreID}|{self.currentMovieID}"
        self.client.sendCommand(command)
    
    def insertAction(self):
        """
        Handles the "Insert" button action.

        Retrieves the data from the input fields, constructs an "#insert" command containing the new movie details, and sends it to the server through the `Client.
        The `currentMovieID` is also included (though it might not be relevant for insertion).
        """
        #get information from the inputs using get()
        genreList = self.cbbGenre['values']
        genreID = genreList.index(self.cbbGenre.get()) + 1 #convert genre name to genreID
        command = f"#insert|{self.txtTitle.get()}|{self.txtDirector.get()}|{self.txtYear.get()}|{self.txtDescription.get('1.0', 'end-1c')}|{genreID}|{self.currentMovieID}"
        self.client.sendCommand(command)
    
    def deleteAction(self):
        """
        Handles the "Delete" button action.

        Prompts the user for a movie ID using a simple dialog and sends a "#delete" command with the provided ID to the server through the `Client.
        """
        # Ask for movie ID via simple dialog
        movie_id = simpledialog.askinteger("Movie ID", "Please enter the movie ID: ")
        #create a delete command
        command = f"#delete|{movie_id}"
        #send to command to client to handle
        self.client.sendCommand(command)

    def setupGUI(self):
        """
        Sets up the user interface elements within the client window.

        This method creates and arranges labels, entry fields, a text area, a combobox for genre selection, and buttons for database operations
        using the Tkinter grid layout manager.
        """
        #1/ create an empty window
        self.window.title("Client Form") #add the title to the window
        self.window.geometry("400x400+800+100") #set the size and position of the windodw
        
        #2/ add the labels and input fieldss (textboxes, text area, combo box)
        #a-create a Title label
        lblTitle = tk.Label(self.window, text = "Title")
        # where to place it
        lblTitle.grid(row=0, column=0, padx=20, pady=10, sticky="e")
        # create a textbox and set it inside the window and at a width
        self.txtTitle = tk.Entry(self.window, width=30)
        self.txtTitle.grid(row=0, column=1, padx=15, pady=15)

        #b-create a Director label and set where it is placed at once
        lblDirector = tk.Label(self.window, text = "Director").grid(row=1, column=0, padx=20, pady=15, sticky="e")
        # create a textbox and set it inside the window and at a width
        self.txtDirector = tk.Entry(self.window, width=30)
        self.txtDirector.grid(row=1, column=1, padx=15, pady=15)

        #c-create a Year label and set where it is placed at once
        lblYear = tk.Label(self.window, text = "Year Released").grid(row=2, column=0, padx=20, pady=15, sticky="e")
        # create a textbox and set it inside the window and at a width
        self.txtYear = tk.Entry(self.window, width=30)
        self.txtYear.grid(row=2, column=1, padx=15, pady=15)

        #d-create a Description label and set where it is placed at once
        lblYear = tk.Label(self.window, text = "Description").grid(row=3, column=0, padx=20, pady=15, sticky="e")
        # create a multi-line text input
        self.txtDescription = tk.Text(self.window, width=23, height=3, wrap=tk.WORD)
        self.txtDescription.grid(row=3, column=1, padx=15, pady=10)

        #e-create a Genre label and set where it is placed at once
        lblGenre = tk.Label(self.window, text = "Genre").grid(row=4, column=0, padx=20, pady=15, sticky="e")
        #create a combobox
        self.cbbGenre = ttk.Combobox(self.window, width=27, values=["Horror", "Fantacy", "Action", "Drama", "Science Fiction", "Comedy", "Thriller", "Adventure", "Romance", "Crime"])
        self.cbbGenre.grid(row=4, column=1, padx=15, pady=15)
        self.cbbGenre.current(0)

        #3-add the SQL buttons - Select, Update, Insert, Delete
        #create a frame to contain the for buttons
        frame = tk.Frame(self.window)
        #place it at row 6, column 1, but span across two columns, maket it align east to west (horizontally)
        frame.grid(row=5, column=0, columnspan=2, padx=10, pady=30, sticky='ew')
        #make the windown and the frame extendable
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)
        frame.columnconfigure(3, weight=1)
        #create buttons and place it inside the frame
        btnSelect = tk.Button(frame, text="Select", width=6, command=self.selectAction).grid(row=0, column=0, sticky='ew', padx=10)
        btnUpdate = tk.Button(frame, text="Update", width=6, command=self.updateAction).grid(row=0, column=1, sticky='ew', padx=10)
        btnInsert = tk.Button(frame, text="Insert", width=6, command=self.insertAction).grid(row=0, column=2, sticky='ew', padx=10)
        btnDelete = tk.Button(frame, text="Delete", width=6, command=self.deleteAction).grid(row=0, column=3, sticky='ew', padx=10)

    def updateGUI(self, movie):
        """
        Updates the GUI input fields with the details of a given movie.

        Args:
            movie (Movie): An object containing the movie details (title, director, yearReleased, description, genreID, movieID).
        """
        self.txtTitle.delete(0, tk.END)
        self.txtTitle.insert(0, movie.title)

        self.txtDirector.delete(0, tk.END)
        self.txtDirector.insert(0, movie.director)

        self.txtYear.delete(0, tk.END)
        self.txtYear.insert(0, movie.yearReleased)

        self.txtDescription.delete("1.0", tk.END)
        self.txtDescription.insert(tk.END, movie.description)

        #get the genre list
        genreList = self.cbbGenre['values']
        self.cbbGenre.set(genreList[int(movie.genreID)])
        self.currentMovieID = int(movie.movieID)        
