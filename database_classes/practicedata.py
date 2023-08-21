"""
:module: practicedata
:synopsis: Defines a class to use SQL basic features.
.. moduleauthor:: Elizabeth Macias <lzbthmacias@gmail.com>, August 2023
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from .baseclass import BaseClass


class PracticeData(BaseClass):
    DEFINED_COLUMNS = "(column1, column2)"
    DEFINED_COLUMNS_TYPE = "(column1 INT, column2 INT)"
    STORE_DATA_FORMAT = "(%s, %s)"
    FILE_COLUMN1 = "col1"
    FILE_COLUMN2 = "col2"
    PLOT_COLUMN1 = 0
    PLOT_COLUMN2 = 1

    """
        MySQL database managing class.

        Keyword Arguments:
            host (str): Host system.
            user (str): Database log-in user.
            password (str): User password.
            filename (str): Name of file from which to load data.
            database (str): Name of user-defined database.
            table (str): Name of user-defined table.

        Attributes:
            _DEFINED_COLUMNS (str): Columns to create.
            _DEFINED_COLUMNS_TYPE (str): Columns data types.
            _STORE_DATA_FORMAT (str): Format for storing data in database.
            _FILE_COLUMN1 (str): Name of column one as defined in file.
            _FILE_COLUMN2 (str): Name of column two as defined in file.
            _PLOT_COLUMN1 (int): Fetched data index for column 1.
            _PLOT_COLUMN2 (int): Fetched data index for column 2.
        """

    def __init__(self, **kwargs):
        """Database manager class initializer."""
        super().__init__(self.DEFINED_COLUMNS_TYPE, **kwargs)

    @BaseClass.commit_changes
    def populate_table(self):
        """Load data and store it in the database table."""
        # Load data from xlsx into a pandas variable
        data = pd.read_excel(f"{self.EXCEL_PATH}/{self.filename}")

        # Iterate through the rows and insert data into the table
        for index, row in data.iterrows():
            # Construct and execute the SQL insert statement
            insert_query = f"INSERT INTO {self.table} {self.DEFINED_COLUMNS} VALUES {self.STORE_DATA_FORMAT}"
            self.cursor.execute(
                insert_query, (int(row[self.FILE_COLUMN1]), int(row[self.FILE_COLUMN2]))
            )

    @BaseClass.query
    def query_data(self):
        """Query data. Decorator returns query output in the _results attribute.

        return (str): User-defined query.
        """
        query = f"SELECT * FROM {self.table}"
        return query

    def plot_data(self):
        """Plot data. User defines what to plot. _results contains
        all data queried when query_data was called.
        """
        plt.plot(
            np.stack(self.results, axis=1)[self.PLOT_COLUMN1],
            np.stack(self.results, axis=1)[self.PLOT_COLUMN2],
            "o",
        )
        plt.ylabel(self.FILE_COLUMN1)
        plt.xlabel(self.FILE_COLUMN2)
        plt.title("Two-column Practice Data Set")
        plt.savefig("practice_data.png")
        plt.show()
