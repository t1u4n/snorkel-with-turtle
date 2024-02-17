from abc import ABC, abstractmethod
from typing import Dict
from numpy import array
import logging


class BaseEmbeddingSystem(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)

    def preprocess(self, text: str) -> str:
        """
        Preprocesses the input text before embedding.
            
        Args:
            text (str): The input text to be preprocessed.
            
        Returns:
            str: The preprocessed text.
        """
        ...

    @abstractmethod
    def embed(self, text: str) -> array:
        """
        Embeds the given text into a numerical representation.

        Args:
            text (str): The text to be embedded.

        Returns:
            array: The numerical representation of the embedded text.
        """
        ...
