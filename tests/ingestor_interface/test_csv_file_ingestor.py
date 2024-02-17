import pytest
from ingestor_interface.csv_file_ingestor import CSVFileIngestor
import tempfile

def test_csv_ingestor_init_failure():
    with pytest.raises(ValueError):
        CSVFileIngestor("nonexistent_file.csv")

@pytest.mark.asyncio
async def test_csv_ingestor_read():
    with tempfile.NamedTemporaryFile(mode='w+', suffix='.csv') as tmpfile:
        tmpfile.write('column1,column2\ndata1,data2\ndata3,data4')
        tmpfile.flush()
    
        ingestor = CSVFileIngestor(tmpfile.name)
        
        data1 = await ingestor.fetch_next_data()
        assert data1 is not None
        assert data1['column1'] == 'data1'

        data2 = await ingestor.fetch_next_data()
        assert data2 is not None
        assert data2['column1'] == 'data3'

        data_end = await ingestor.fetch_next_data()
        assert data_end is None
