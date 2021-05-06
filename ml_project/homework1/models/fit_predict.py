import pickle
from typing import Dict, Union

import numpy as np
import pandas as pd
from catboost import CatBoostClassifier, CatBoostRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from homework1.entities.feature_params import FeatureParams
from homework1.entities.train_params import TrainParams

ValidModelClass = Union[CatBoostClassifier, CatBoostRegressor]


def train_model(
    features: pd.DataFrame,
    target: pd.Series,
    train_params: TrainParams,
    feature_params: FeatureParams,
) -> ValidModelClass:
    if train_params.model_type == "CatBoostClassifier":
        model = CatBoostClassifier(random_state=train_params.random_state)
    elif train_params.model_type == "CatBoostRegressor":
        model = CatBoostClassifier(random_state=train_params.random_state)
    else:
        raise NotImplementedError()
    model.fit(features, target, verbose=100)
    return model


def predict_model(
    model: ValidModelClass, features: pd.DataFrame, use_log_trick: bool = True
) -> np.ndarray:
    preds = model.predict(features)
    return preds


def eval_model(
    preds: np.ndarray, target: pd.Series, use_log_trick: bool = False
) -> Dict[str, float]:
    return dict(
        r2_score=r2_score(target, preds),
        rmse=mean_squared_error(target, preds, squared=False),
        mae=mean_absolute_error(target, preds),
    )


def serialize_model(model: ValidModelClass, output: str) -> str:
    with open(output, "wb") as f:
        pickle.dump(model, f)
    return output


def deserialize_model(path: str) -> ValidModelClass:
    with open(path, "rb") as f:
        return pickle.load(f)
