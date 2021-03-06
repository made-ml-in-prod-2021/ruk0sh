# -*- coding: utf-8 -*-
from typing import Tuple

import pandas as pd
from sklearn.model_selection import train_test_split

from homework1.entities.split_params import SplitParams


def read_data(path: str) -> pd.DataFrame:
    data = pd.read_csv(path)
    return data


def split_data(
    data: pd.DataFrame, params: SplitParams
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    train_data, val_data = train_test_split(
        data, test_size=params.val_size, random_state=params.random_state
    )
    return train_data, val_data
