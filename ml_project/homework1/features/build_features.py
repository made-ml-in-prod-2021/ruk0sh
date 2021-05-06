from typing import Optional, Tuple

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.impute._base import _BaseImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

from homework1.entities.feature_params import FeatureParams
from homework1.models.encoders import CustomLogTransformer


def get_imputer(strategy: str) -> _BaseImputer:
    imputer = SimpleImputer(missing_values=np.nan, strategy=strategy)
    return imputer


def get_categorical_imputer() -> _BaseImputer:
    return get_imputer(strategy="most_frequent")


def get_numerical_imputer() -> _BaseImputer:
    return get_imputer(strategy="mean")


def process_cat_features(pipeline: Pipeline, cat_df: pd.DataFrame) -> pd.DataFrame:
    res_df = pd.DataFrame(
        pipeline.transform(cat_df).toarray(),
        columns=pipeline["encoder"].get_features_names(),
    )
    return res_df


def cat_features_pipeline() -> Pipeline:
    imputer = get_categorical_imputer()
    encoder = OneHotEncoder()
    pipeline = Pipeline(
        [
            ("imputer", imputer),
            ("encoder", encoder),
        ]
    )
    return pipeline


def num_features_pipeline() -> Pipeline:
    imputer = get_numerical_imputer()
    encoder = CustomLogTransformer()
    pipeline = Pipeline(
        [
            ("imputer", imputer),
            ("encoder", encoder),
        ]
    )
    return pipeline


def make_features(
    transformer: ColumnTransformer,
    df: pd.DataFrame,
    params: FeatureParams,
    test_mode: bool = False,
) -> Tuple[pd.DataFrame, Optional[pd.Series]]:
    featured_df = pd.DataFrame(transformer.transform(df))
    if test_mode:
        return featured_df, None
    target = df[params.target_col]
    return featured_df, target


def column_transformer(params: FeatureParams) -> ColumnTransformer:
    transformer = ColumnTransformer(
        [
            ("cat", cat_features_pipeline(), params.cat_features),
            ("num", num_features_pipeline(), params.num_features),
        ]
    )
    return transformer
