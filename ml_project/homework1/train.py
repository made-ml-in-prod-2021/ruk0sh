import json
import logging
import os
import sys

import hydra
from omegaconf import DictConfig, OmegaConf

from homework1.data.make_dataset import read_data, split_data
from homework1.entities.train_pipeline_params import (
    TrainPipelineParams, TrainPipelineParamsSchema, read_train_pipeline_params)
from homework1.features.build_features import column_transformer, make_features
from homework1.models.fit_predict import (eval_model, predict_model,
                                          serialize_model, train_model)

logger = logging.getLogger("ml_project")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(levelname)s: %(name)s [%(asctime)s] %(message)s")
file_handler = logging.FileHandler(f"logs/train.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def train_pipeline(train_pipeline_params: TrainPipelineParams):

    logger.info(f"Start training...\nParams: {train_pipeline_params}")
    data = read_data(train_pipeline_params.input_data_path)
    logger.info(f"Data shape is {data.shape[0]} rows X {data.shape[1]} cols")

    train_df, val_df = split_data(data, train_pipeline_params.split_params)
    logger.info(f"Train is {train_df.shape[0]} rows X {train_df.shape[1]} cols")
    logger.info(f"Validation is {val_df.shape[0]} rows X {val_df.shape[1]} cols")

    feature_transformer = column_transformer(train_pipeline_params.feature_params)
    feature_transformer.fit(train_df)

    train_features, train_target = make_features(
        feature_transformer,
        train_df,
        train_pipeline_params.feature_params,
        test_mode=False,
    )
    logger.info(
        f"Train features is {train_features.shape[0]} rows X {train_features.shape[1]} cols"
    )

    model = train_model(
        train_features,
        train_target,
        train_pipeline_params.train_params,
        train_pipeline_params.feature_params,
    )

    val_features, val_target = make_features(
        feature_transformer,
        val_df,
        train_pipeline_params.feature_params,
        test_mode=False,
    )
    logger.info(
        f"Validation features is {val_features.shape[0]} rows X {val_features.shape[1]} cols"
    )

    predictions = predict_model(
        model, val_features, train_pipeline_params.feature_params.use_log_trick
    )

    metrics = eval_model(
        predictions,
        val_target,
        use_log_trick=train_pipeline_params.feature_params.use_log_trick,
    )

    with open(train_pipeline_params.metrics_path, "w") as metric_file:
        json.dump(metrics, metric_file)
    logger.info(f"Metrics: {metrics}")

    path_to_model = serialize_model(model, train_pipeline_params.output_model_path)

    return path_to_model, metrics


@hydra.main(config_path="../configs", config_name="train_config.yaml")
def main(config: DictConfig) -> None:
    """
    Hydra wrapper for parsing CLI arguments
    :return: Nothing
    """
    os.chdir(hydra.utils.to_absolute_path("."))
    schema = TrainPipelineParamsSchema()
    logger.info(f"Train configurations is:\n{OmegaConf.to_yaml(config)}")
    config = schema.load(config)
    train_pipeline(config)


if __name__ == "__main__":
    main()
