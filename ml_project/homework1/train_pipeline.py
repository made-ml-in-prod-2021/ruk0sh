import json
import logging
import sys

import click

from data.make_dataset import read_data, split_data
from entities.train_pipeline_params import (
    TrainPipelineParams,
    read_train_pipeline_params,
)
from features.build_features import column_transformer, make_features
from models.fit_predict import train_model, predict_model, eval_model, serialize_model

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)


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


@click.command(name="train_pipeline")
@click.argument("config_path")
def train_pipeline_command(config_path: str):
    params = read_train_pipeline_params(config_path)
    train_pipeline(params)


if __name__ == "__main__":
    train_pipeline_command()
