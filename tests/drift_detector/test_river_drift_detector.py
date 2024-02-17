from unittest.mock import patch
from numpy import mean, array
from drift_detector.river_drift_detector import RiverDriftDetector

def test_initialization():
    with patch('river.drift.ADWIN') as MockADWIN:
        RiverDriftDetector()
        MockADWIN.assert_called_once()

def test_agg_func_usage():
    test_data = array([1, 2, 3, 4, 5])
    custom_agg_func = lambda x: sum(x) / len(x)  # Same as mean
    detector = RiverDriftDetector(agg_func=custom_agg_func)
    assert detector.agg_func(test_data) == mean(test_data), "Aggregation function doesn't work as expected."

@patch('river.drift.ADWIN')
def test_is_drifted(MockADWIN):
    mock_adwin_instance = MockADWIN.return_value
    mock_adwin_instance.drift_detected = False
    detector = RiverDriftDetector()
    
    # No drift
    assert not detector.is_drifted(array([1, 2, 3])), "Shouldn't detect drift."
    
    # Drift exists
    mock_adwin_instance.drift_detected = True
    assert detector.is_drifted(array([4, 5, 6])), "Should detect drift."
