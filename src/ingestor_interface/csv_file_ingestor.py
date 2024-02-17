from ingestor_interface.base_ingestor import BaseIngestor
from pandas import Series, read_csv
from pathlib import Path


class CSVFileIngestor(BaseIngestor):
    def __init__(self, source_file: str) -> None:
        """
        Initialize the CSVIngestor object.

        Args:
            source_file (str): The path to the source CSV file.

        Raises:
            ValueError: If the source file is not provided or does not exist.
        """
        super().__init__()
        if not source_file:
            raise ValueError("source file is required")

        file = Path(source_file)
        if not file.exists():
            raise ValueError("source file does not exist")
            
        self.csv_iter = read_csv(source_file).iterrows()
        
    async def fetch_next_data(self) -> Series | None:
        """
        Fetches the next data from the CSV iterator.

        Returns:
            Series | None: The next data from the CSV iterator, or None if there is no more data.
        """
        try:
            _, data = next(self.csv_iter)
        except StopIteration:
            data = None
        return data
