import pytest
from model_trainer.model_trainer import ModelTrainer
from pandas import DataFrame
from snorkel.labeling import labeling_function
from snorkel.labeling.model import LabelModel
from unittest.mock import patch, MagicMock


# Sample labeling functions

@labeling_function("func_1")
def labeling_function_1(x):
    return 1

@labeling_function("func_2")
def labeling_function_2(x):
    return 0

@labeling_function("func_3")
def labeling_function_3(x):
    return 1

@pytest.fixture
def lf_lib_mock(mocker):
    # Mock labeling function library
    mock = MagicMock()
    mock.get_all.return_value = [labeling_function_1, labeling_function_2, labeling_function_3]
    return mock

@pytest.fixture
def data_mock():
    # Mock a DataFrame as data
    return DataFrame({"text": ["example1", "example2"]})

@pytest.fixture
def config_mock():
    return {"n_epochs": 100}

def test_train_fits_label_model(lf_lib_mock, data_mock, config_mock):
    # Initialize
    trainer = ModelTrainer(config=config_mock)

    try:
        trained_model = trainer.train(data=data_mock, lf_lib=lf_lib_mock, cardinality=2)
    except Exception as e:
        pytest.fail(f"test_train_fits_label_model() raised an exception {e}")

    # Verify return instance
    assert isinstance(trained_model, LabelModel), "train method should return a LabelModel instance"
