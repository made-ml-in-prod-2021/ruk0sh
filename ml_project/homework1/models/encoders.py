from typing import NoReturn

import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class CustomLogTransformer(BaseEstimator, TransformerMixin):
    """
    Stupid log transformer to proof a concept
    """

    def __init__(self) -> NoReturn:
        super(CustomLogTransformer, self).__init__()

    def fit_transform(self, X, y=None, **fit_params):
        X_ = X.copy()
        X_ = np.log(X_)
        return X_
