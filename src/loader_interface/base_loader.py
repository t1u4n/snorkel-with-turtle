from abc import ABC, abstractmethod
from typing import Any, AsyncGenerator
import logging


class BaseLoader(ABC):
    def __init__(self) -> None:
        """
        Initializes the BaseLoader object.
        """
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    async def write_data(self, data: Any) -> None:
        """
        Writes the given data to a destination.

        Args:
            data (Any): The data to be written.
        """
        ...

    async def run(self, data_generator: AsyncGenerator[Any, None]) -> None:
        """
        Starts processing data from the given generator and writes it to the destination.

        Args:
            data_generator: An asynchronous generator that yields data to be written.
        """
        self.logger.info("Starting data loading process.")
        async for data in data_generator:
            await self.write_data(data)
        self.logger.info("Data loading process completed.")
