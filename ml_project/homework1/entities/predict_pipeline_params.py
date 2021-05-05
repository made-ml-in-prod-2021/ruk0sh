import yaml
from dataclasses import dataclass, field
from marshmallow_dataclass import class_schema

from homework1.entities.feature_params import FeatureParams


@dataclass()
class PredictParams:
    """
    Class for predict.py configuration
    """
    version: int
    model_path: str
    raw_data_path: str
    proceed_data_path: str
    metrics_path: str
    feature_params: FeatureParams
    threshold: float = field(default=0.5)


PredictParamsSchema = class_schema(PredictParams)


def read_predict_pipeline_params(path: str) -> PredictParams:
    """
    :param path: path to config
    :return: config dataclass
    """
    with open(path, "r") as fin:
        schema = PredictParamsSchema()
        return schema.load(yaml.safe_load(fin))
