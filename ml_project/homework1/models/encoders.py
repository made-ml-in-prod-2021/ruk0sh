from typing import Optional, Union

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import FLOAT_DTYPES

ArrayLike = Union[np.ndarray, pd.DataFrame]


class CustomLogTransformer(BaseEstimator, TransformerMixin):
    """
    Stupid log transformer to proof a concept
    """

    def __init__(self, copy: bool = True) -> None:
        self.copy = copy

    def fit(
        self, X: ArrayLike, y: Optional[np.ndarray] = None
    ) -> "CustomLogTransformer":
        return self

    def transform(
        self, X: ArrayLike, y: Optional[np.ndarray] = None, copy: Optional[bool] = None
    ):
        copy = copy or self.copy
        X_new = self._validate_data(
            X,
            reset=False,
            estimator=self,
            dtype=FLOAT_DTYPES,
            force_all_finite="allow-nan",
            copy=copy,
        )
        X_new -= np.min(X_new, axis=0, keepdims=True)
        X_new = np.log1p(X_new)
        return X_new

    def fit_transform(self, X: ArrayLike, y: Optional[np.ndarray] = None) -> ArrayLike:
        return self.fit(X, y).transform(X, y)
