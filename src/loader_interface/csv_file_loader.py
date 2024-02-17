from loader_interface.base_loader import BaseLoader
from pandas import DataFrame
from pathlib import Path


class CSVLoader(BaseLoader):
    def __init__(self, destination_file: str) -> None:
        """
        Initialize the CSVLoader object.

        Args:
            destination_file (str): The path to the destination CSV file.
        """
        super().__init__()
        self.destination_file = destination_file
        self.initial_write = not Path(self.destination_file).exists()

    async def write_data(self, data: DataFrame) -> None:
        """
        Writes the given data to a CSV file.

        Args:
            data (DataFrame): The data to be written. Expected to be a pandas DataFrame.
        """
        # Write DataFrame to CSV file
        data.to_csv(self.destination_file, mode='a', header=self.initial_write, index=False)
        
        # After the first write, set initial_write to False so headers are not repeated
        self.initial_write = False
