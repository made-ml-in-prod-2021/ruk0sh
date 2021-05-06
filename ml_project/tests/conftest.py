from textwrap import dedent

import pandas as pd
import pytest
import yaml
from catboost import CatBoostClassifier, CatBoostRegressor
from sklearn.compose import ColumnTransformer

from tests.datagen import CAT_FEATURES, NUM_FEATURES, TARGET_COL, generate
from homework1.entities.feature_params import FeatureParams
from homework1.entities.train_params import TrainParams
from homework1.entities.split_params import SplitParams
from homework1.entities.train_pipeline_params import TrainPipelineParams
from homework1.entities.predict_pipeline_params import PredictParams


@pytest.fixture
def feature_df():
    df = pd.DataFrame([[11, 22, 33], [-1, -2, -3], [0.0, 0.0, 0.0]])
    return df


@pytest.fixture
def target_col():
    target = pd.Series([1, 0, 1])
    return target


@pytest.fixture
def model_classifier():
    model = CatBoostClassifier()
    return model


@pytest.fixture
def model_regressor():
    model = CatBoostRegressor()
    return model


@pytest.fixture
def transformer():
    transformer = ColumnTransformer(["all", "passthrough", [0, 1, 2]])
    return transformer


@pytest.fixture
def mock_dataset():
    data = generate(size=100, writefile=False)
    return data


@pytest.fixture
def mock_train_config():
    raw_str = dedent(
        """
        version: 1
        input_data_path: "data/raw/heart.csv"
        output_model_path: "models/model.pkl"
        metrics_path: "models/metrics.json"
        defaults:
          split_params:
            val_size: 0.2
            random_state: 42
          train_params:
            model_type: "CatBoostClassifier"
          feature_params:
          cat_features:
            - "ca"
            - "cp"
            - "exang"
            - "fbs"
            - "restecg"
            - "sex"
            - "slope"
            - "thal"
          num_features:
            - "age"
            - "chol"
            - "oldpeak"
            - "thalach"
            - "trestbps"
          drop_features: []
          target_col: "target"
        """
    )
    cfg_dict = yaml.safe_load(raw_str)
    return cfg_dict


@pytest.fixture
def feature_params_fixture():
    params = FeatureParams(
        cat_features=CAT_FEATURES,
        num_features=NUM_FEATURES,
        target_col=TARGET_COL,
        drop_features=[],
    )
    return params


@pytest.fixture
def train_params_fixture():
    params = TrainParams()
    return params


@pytest.fixture
def split_params_fixture():
    params = SplitParams()
    return params


@pytest.fixture
def train_pipeline_params_fixture(
    feature_params_fixture, split_params_fixture, train_params_fixture
):
    params = TrainPipelineParams(
        feature_params=feature_params_fixture,
        split_params=split_params_fixture,
        train_params=train_params_fixture,
        input_data_path="data/test_data/generated.csv",
        metrics_path="data/test_data/metrics.json",
        version=1,
        output_model_path="data/test_data/model.pkl",
    )
    return params


@pytest.fixture
def predict_pipeline_params_fixture(feature_params_fixture):
    params = PredictParams(
        version=1,
        model_path="data/test_data/model.pkl",
        raw_data_path="data/test_data/generated.csv",
        proceed_data_path="data/test_data/preds.csv",
        metrics_path="data/test_data/metrics.json",
        feature_params=feature_params_fixture,
    )
    return params
