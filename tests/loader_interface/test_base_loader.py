import pytest
from typing import Any, List
from loader_interface.base_loader import BaseLoader

class _TestLoader(BaseLoader):
    def __init__(self, output: List) -> None:
        super().__init__()
        self.out = output

    async def write_data(self, data: Any) -> None:
        self.out.append(data)

@pytest.mark.asyncio
async def test_run():
    async def dummy_data_generator():
        for i in range(5):
            yield f"data {i}"

    # Catch the output of write data
    output = []
    loader = _TestLoader(output=output)
    
    # Run loader
    await loader.run(dummy_data_generator())

    # Verify if output equal as expected
    assert output == [f"data {i}" for i in range(5)]
