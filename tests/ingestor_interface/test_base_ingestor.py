from typing import Any
from ingestor_interface.base_ingestor import BaseIngestor
import pytest
from unittest.mock import call, Mock, AsyncMock

class _TestIngestor(BaseIngestor):
    def __init__(self, data, max_fetches):
        super().__init__()
        self.data = data
        self.max_fetches = max_fetches
        self.fetch_count = 0

    async def fetch_next_data(self) -> Any | None:
        if self.fetch_count < self.max_fetches:
            self.fetch_count += 1
            return self.data
        return None
    
@pytest.mark.asyncio
async def test_run():
    # Data and max fetch count
    test_data = "test data"
    max_fetches = 3

    ingestor = _TestIngestor(test_data, max_fetches)
    
    # Mock the functions
    handle_data = Mock()
    sample_policy = lambda data: True
    handle_sample_data = Mock()
    
    # Test run method
    await ingestor.run(handle_data, sample_policy, handle_sample_data)
    
    # Verify handle_data and handle_sample_data has been called with right times
    assert handle_data.call_count == max_fetches
    assert handle_sample_data.call_count == max_fetches
    handle_data.assert_has_calls([call(test_data)] * max_fetches)
    handle_sample_data.assert_has_calls([call(test_data)] * max_fetches)

@pytest.mark.asyncio
async def test_async_run():
    # Data and max fetch count
    test_data = "test data"
    max_fetches = 3

    ingestor = _TestIngestor(test_data, max_fetches)
    
    # Mock the functions
    handle_data = AsyncMock()
    sample_policy = lambda data: True
    handle_sample_data = AsyncMock()
    
    # Test run method
    await ingestor.run(handle_data, sample_policy, handle_sample_data)
    
    # Verify handle_data and handle_sample_data has been called with right times
    assert handle_data.call_count == max_fetches
    assert handle_sample_data.call_count == max_fetches
    handle_data.assert_has_calls([call(test_data)] * max_fetches)
    handle_sample_data.assert_has_calls([call(test_data)] * max_fetches)