from abc import ABC, abstractmethod
import logging
from numpy import array


class BaseDriftDetector(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    def is_drifted(self, feat_vec: array) -> bool:
        """
        Check if the given feature vector indicates drift.

        Parameters:
        feat_vec (array): The feature vector to be checked for drift.

        Returns:
        bool: True if the feature vector indicates drift, False otherwise.
        """
        ...
