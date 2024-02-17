from abc import ABC, abstractmethod
from typing import Any, Callable
import logging
import inspect


class BaseIngestor(ABC):
    def __init__(self) -> None:
        """
        Initializes the BaseIngestor object.
        """
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    async def fetch_next_data(self) -> Any | None:
        """
        Fetches the next data.

        Returns:
            The next data item, or None if there is no more data.
        """
        ...

    async def run(
            self,
            handle_data: Callable[[Any], None],
            sample_policy: Callable[[Any], bool] = lambda _: True,
            handle_sample_data: Callable[[Any], None] = lambda _: None,
    ) -> None:
        """
        Start ingesting data.

        Args:
            handle_data (Callable[[Any], None]): A function to handle the ingested data.
            sample_policy (Callable[[Any], bool], optional): A function to determine if the data should
                                                             be sampled. Defaults to sample all data.
            handle_sample_data (Callable[[Any], None], optional): A function to handle the sampled data.
                                                                  Defaults to do nothing.
        """
        self.logger.info(f"Start ingesting data with {self}")

        if not callable(handle_data):
            raise TypeError("'handle_data' must be a function")

        if not callable(sample_policy):
            raise TypeError("'sample_policy' must be a function")
            
        if not callable(handle_sample_data):
            raise TypeError("'handle_sample_data' must be a function or None")
            
        while True:
            data = await self.fetch_next_data()
            if data is None: # Stop ingesting if data is None
                break

            if inspect.iscoroutinefunction(handle_data):
                await handle_data(data)
            else:
                handle_data(data)

            if sample_policy(data) and handle_sample_data is not None:
                if inspect.iscoroutinefunction(handle_sample_data):
                    await handle_sample_data(data)
                else:
                    handle_sample_data(data)

        self.logger.info("Finish ingesting data")
