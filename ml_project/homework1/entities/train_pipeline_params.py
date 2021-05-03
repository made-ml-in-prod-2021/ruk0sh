import yaml
from dataclasses import dataclass

from marshmallow_dataclass import class_schema

from .feature_params import FeatureParams
from .train_params import TrainParams
from .split_params import SplitParams


@dataclass()
class TrainPipelineParams:
    input_data_path: str
    output_data_path: str
    metrics_path: str
    feature_params: FeatureParams
    split_params: SplitParams
    train_params: TrainParams


TrainPipelineParamsSchema = class_schema(TrainPipelineParams)


def read_train_pipeline_params(path: str) -> TrainPipelineParams:
    with open(path, "r") as input_stream:
        schema = TrainPipelineParamsSchema()
        return schema.load(yaml.safe_load(input_stream))