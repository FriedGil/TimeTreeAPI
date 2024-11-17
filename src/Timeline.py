import pandas as pd
from io import StringIO


class Timeline:
    """
    A class to represent a timetree taxa.

    This class processes CSV string data, loading it into a pandas DataFrame,
    and provides methods to filter and retrieve taxa information based on
    specific criteria such as rank and taxonomic level.

    Attributes:
    df (pd.DataFrame): A pandas DataFrame holding the data.

    Methods:
    __repr__(): Returns a string representation of the object, showing a summary of the data.
    get_taxa_by_rank(rank: str): Filters and returns taxa with a specific rank.
    get_taxa_above_level(level: int): Filters and returns taxa above a certain taxonomic level.
    get_taxa_below_level(level: int): Filters and returns taxa below a certain taxonomic level.
    """

    def __init__(self, data: str):

        # Use StringIO to simulate a file-like object from the string data
        self.data = StringIO(data)

        # Read the CSV data into a pandas DataFrame
        self.df = pd.read_csv(self.data)

    def __repr__(self) -> str:
        # Show the first few rows for summary
        summary = self.df.head().to_string(index=False)
        return f"TaxonomyData({summary})"

    def get_taxa_by_rank(self, rank: str) -> pd.DataFrame:
        """
        Filters the data to return only rows with a specific rank.

        :param rank: The rank (e.g., 'family', 'order', etc.)
        :return: DataFrame with rows matching the rank
        """
        return self.df[self.df["rank"] == rank]

    def get_taxa_above_level(self, level: int) -> pd.DataFrame:
        """
        Filters the data to return taxa above a certain level.

        :param level: The level to filter by (only taxa above this level will be returned)
        :return: DataFrame with rows where 'level' is greater than the specified level
        """
        return self.df[self.df["level"] > level]

    def get_taxa_below_level(self, level: int) -> pd.DataFrame:
        """
        Filters the data to return taxa below a certain level.

        :param level: The level to filter by (only taxa below this level will be returned)
        :return: DataFrame with rows where 'level' is less than the specified level
        """
        return self.df[self.df["level"] < level]
