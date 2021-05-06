import pandas as pd
import numpy as np
import pytest
from typing import Union

from homework1.models.encoders import CustomLogTransformer


test_X = np.array([[11, 22, 33], [-1, -2, -3], [0.0, 0.0, 0.0]])
expected_X = test_X.copy()
expected_X -= np.min(expected_X, axis=0, keepdims=True)
expected_X = np.log1p(expected_X)


@pytest.mark.parametrize(
    "test_input, expected", [(test_X, expected_X), (pd.DataFrame(test_X), expected_X)]
)
def test_CustomLogTransformer_works_as_expected(
    test_input: np.ndarray, expected: Union[np.ndarray, pd.DataFrame]
) -> None:
    transformer = CustomLogTransformer()
    transformed_X = transformer.fit_transform(test_input)
    if isinstance(expected, pd.DataFrame):
        assert (
            transformed_X.tolist() == expected.values.tolist()
        ), "CustomLogTransformer failed to procees pd.Dataframe"
    else:
        assert (
            transformed_X.tolist() == expected.tolist()
        ), "CustomLogTransformer failed to procees np.ndarray"
