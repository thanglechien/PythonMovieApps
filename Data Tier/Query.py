class Query:
    """
    Represents a query with a timestamp.

    This class stores the timestamp of a query and the details of the query.
    """
    def __init__(self, timestamp, queryDetails):
        """
        Initializes a Query object.

        Args:
            timestamp (str): The timestamp of the query.
            queryDetails (str): The details of the query.
        """
        self.timestamp = timestamp
        self.queryDetails = queryDetails

    def writeAsRecord(self):
        """
        Formats the query as a record string.

        This method formats the timestamp and query details into a single string,
        separated by a delimiter ('#').  This format is suitable for saving
        the query to a file.

        Returns:
            str: The formatted string representing the query record.
        """
        return f"{self.timestamp}#{self.queryDetails}"
