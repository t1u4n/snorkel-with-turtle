from drift_detector.base_drift_detector import BaseDriftDetector
from river import drift
from numpy import array, mean
from typing import Callable


class RiverDriftDetector(BaseDriftDetector):
    def __init__(
        self,
        drift_detect_algo: str = 'ADWIN',
        agg_func: Callable[[array], float] = lambda x: mean(x)
    ) -> None:
        super().__init__()
        if drift_detect_algo == 'ADWIN':
            self.drift_detector = drift.ADWIN()
        else:
            raise ValueError(f"Support for algorithm {drift_detect_algo} not implemented yet")
        
        if not callable(agg_func):
            raise TypeError("Aggregation function must be a callable.")
        self.agg_func = agg_func

    def is_drifted(self, feat_vec: array) -> bool:
        """
        Check if the given feature vector indicates drift.

        Parameters:
        feat_vec (array): The feature vector to be checked for drift.

        Returns:
        bool: True if the feature vector indicates drift, False otherwise.
        """
        val = self.agg_func(feat_vec)
        self.drift_detector.update(val)
        return self.drift_detector.drift_detected