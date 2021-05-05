import pickle
from typing import Union, Dict

import numpy as np
import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from catboost import CatBoostClassifier

from entities.train_params import TrainParams
from entities.feature_params import FeatureParams

TrainedModel = Union[CatBoostClassifier]


def train_model(
    features: pd.DataFrame,
    target: pd.Series,
    train_params: TrainParams,
    feature_params: FeatureParams,
) -> TrainedModel:
    if train_params.model_type == "CatBoostClassifier":
        model = CatBoostClassifier(random_state=train_params.random_state)
    else:
        raise NotImplementedError()
    model.fit(features, target)
    return model


def predict_model(
    model: TrainedModel, features: pd.DataFrame, use_log_trick: bool = True
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


def serialize_model(model: TrainedModel, output: str) -> str:
    with open(output, "wb") as f:
        pickle.dump(model, f)
    return output
