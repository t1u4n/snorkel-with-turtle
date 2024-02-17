import pytest
import pandas as pd
from pandas.testing import assert_frame_equal
from loader_interface.csv_file_loader import CSVLoader
import asyncio

@pytest.mark.asyncio
async def test_csv_loader(tmp_path):
    # Create a temp path
    destination_file = tmp_path / "output.csv"
    
    # Create DataFrame used for tests
    df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
    
    loader = CSVLoader(str(destination_file))
    
    # Write the first batch of data
    await loader.write_data(df1)
    
    # Verify if the first write successful
    loaded_df1 = pd.read_csv(destination_file)
    assert_frame_equal(loaded_df1, df1, check_dtype=False)
    
    # Write the second batch of data
    await loader.write_data(df2)
    
    # Verify if the second write successful
    loaded_df2 = pd.read_csv(destination_file)
    combined_df = pd.concat([df1, df2], ignore_index=True)
    assert_frame_equal(loaded_df2, combined_df, check_dtype=False)

# Clean files
@pytest.fixture(autouse=True)
def run_around_tests():
    # Do nothing before test
    yield
    # Execute cleanup
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.sleep(0.1))
    # Delete anything here if need
