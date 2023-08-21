import os
import mysql.connector
from abc import abstractmethod


class BaseClass:
    EXCEL_PATH = f"{os.getcwd()}"
    DELETE_DATABASE = "DROP DATABASE IF EXISTS"
    CREATE_DATABASE = "CREATE DATABASE IF NOT EXISTS"
    """
    MySQL database managing base class.
    
    Positional Arguments:
        defined_columns (tuple): Columns to create.
    
    Keyword Arguments:
        host (str): Host system.
        user (str): Database log-in user.
        password (str): User password.
        filename (str): Name of file from which to load data.
        database (str): Name of user-defined database.
        table (str): Name of user-defined table.
    
    Attributes:
        _host (str): Host system.
        _user (str): Database log-in user.
        _password (str): User password.
        _filename (str): Name of file from which to load data.
        _database (str): Name of user-defined database.
        _table (str): Name of user-defined table.
        _defined_columns (tuple): Columns to create.
        _db (Obj): MySQL server object.
        _cursor (obj): Shell cursor object.
        _results (tuple): Tuple with queried data.
    """

    def __init__(self, defined_columns, **kwargs):
        """Database manager base class initializer."""
        self.host = kwargs.get("host", "localhost")
        self.user = kwargs.get("user", "root")
        self.password = kwargs.get("password", "new_password")
        self.filename = kwargs.get("filename")
        self.database = kwargs.get("database")
        self.table = kwargs.get("table")
        self.defined_columns = defined_columns
        self.results = ()

        # Connect to MySQL server
        self.db = mysql.connector.connect(
            host=self.host, user=self.user, password=self.password
        )

        # Create a cursor to execute queries
        self.cursor = self.db.cursor()

    def delete_db(self):
        """Delete the database."""
        self.cursor.execute(f"{self.DELETE_DATABASE} {self.database}")

    def create_db(self):
        """Create the database if it doesn't exist. Switch to it."""
        self.cursor.execute(f"{self.CREATE_DATABASE} {self.database}")
        # Switch to the newly created database
        self.db.database = self.database

    def create_table(self):
        """Create the table if doesn't exist."""
        self.cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {self.table} {self.defined_columns}"
        )

    @staticmethod
    def commit_changes(func):
        """Database-management class method decorator. Commits
        changes made to the database.

        Arguments:
            func (method): Database management class method.

        return (func): The modified class method.
        """

        def append(self):
            """Commit changes made to the database."""
            func(self)
            # Commit the changes
            self.db.commit()

        return append

    @staticmethod
    def query(func):
        """Database-management class query_data() method decorator.

        Arguments:
            func (method): Database management class query_data method.

        return (func): The modified query_data class method.
        """

        def append(self):
            """Takes user-defined query and executes it. Then it stores
            the output into _results.

            Arguments:
                self (obj): Database management class object.
            """
            # Execute the query
            self.cursor.execute(func(self))
            # Fetch the results
            self.results = self.cursor.fetchall()

        return append

    @abstractmethod
    def populate_table(self):
        """Load data and store it in the database table."""
        pass

    @abstractmethod
    def query_data(self):
        """Query data."""
        pass

    @abstractmethod
    def plot_data(self):
        """Plot data."""
        pass

    def close_connection(self):
        """Close the cursor and database connection."""
        self.cursor.close()
        self.db.close()
