import pandas as pd

from homework1.data.make_dataset import read_data, split_data
from tests.conftest import TEST_DATA_PATH


def test_read_data_can_read_from_file():
    data = read_data(TEST_DATA_PATH)
    assert isinstance(
        data, pd.DataFrame
    ), f"Data type is {type(data)}, expected: pd.Dataframe"


def test_split_data_works_correctly(mock_dataset, split_params_fixture):
    train, val = split_data(mock_dataset, split_params_fixture)
    rows_expected = split_params_fixture.val_size * 100
    cols_expected = mock_dataset.shape[1]
    assert (
        val.shape[0] == rows_expected
    ), f"Validation dataset has {val.shape[0]} rows, expected: {rows_expected}"
    assert (
        train.shape[1] == val.shape[1] == cols_expected
    ), f"Data have {train.shape[1]} columns, expected: {cols_expected}"
