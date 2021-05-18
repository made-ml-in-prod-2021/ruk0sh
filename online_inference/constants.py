from typing import Union

from pydantic import BaseModel, conlist, validator


PATH_TO_MODEL = "online_inference/model.pkl"
LANDING_MESSAGE = """
This is a entry point of our demo REST API\n
Other available routes are:\n

"""

# Features and their expected values.
# Based on EDA. Columns order matches column order of original dtataset.
FEATURE_RANGES = [
    ("age", None),
    ("sex", [0, 1]),
    ("cp", [0, 3]),
    ("trestbps", None),
    ("chol", None),
    ("fbs", [0, 1]),
    ("restecg", [0, 2]),
    ("thalach", None),
    ("exang", [0, 1]),
    ("oldpeak", None),
    ("slope", [0, 2]),
    ("ca", [0, 4]),
    ("thal", [0, 3]),
]
NUM_FEATURES = len(FEATURE_RANGES)
FEATURES = [feature for feature, range in FEATURE_RANGES]

# Errors and status codes
STATUS_CODE_DATA_VALIDATION_FAILED = 400
ERROR_CAT_FEATURE_OUT_OF_RANGE = "Error: categorical feature out of range"
ERROR_WRONG_FEATURES = "Error: wrong feature column order or shape"


class DataSample(BaseModel):
    features: conlist(item_type=str, min_items=NUM_FEATURES, max_items=NUM_FEATURES)
    data: conlist(
        conlist(Union[float, int], min_items=NUM_FEATURES, max_items=NUM_FEATURES),
        min_items=1,
    )

    @validator("features")
    def validate_features(cls, features):
        if features != FEATURES:
            raise ValueError(ERROR_WRONG_FEATURES)
        return features

    @validator("data")
    def validate_data(cls, data):
        for sample in data:
            for value, (feature_name, feature_range) in zip(sample, FEATURE_RANGES):
                if feature_range is None:
                    continue
                if not (feature_range[0] <= value <= feature_range[1]):
                    raise ValueError(ERROR_CAT_FEATURE_OUT_OF_RANGE)
        return data


class ModelResponse(BaseModel):
    id: str
    proba: float
