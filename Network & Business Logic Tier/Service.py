from abc import ABC, abstractmethod

class Service(ABC):
    """
    An abstract base class for defining service operations.

    This class serves as a blueprint for other service classes. It cannot be
    instantiated directly and requires subclasses to implement the `doWork` method.

    Attributes:
        command (str): The command or data that the service will process.
    """

    #constructor
    def __init__(self, command):
        """
        Initializes the Service object with a command.

        Args:
            command (str): The command or data to be processed by the service.
        """
        self.command = command
    
    @abstractmethod
    def doWork(self):
        """
        Abstract method to perform the service's work.

        This method must be implemented by any class that inherits from `Service`.
        It defines the core logic of the service.

        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        #this method will be implemented by subclasses
        pass