import logging
import os
import sys

import hydra
import numpy as np
import pandas as pd
from omegaconf import DictConfig, OmegaConf

from homework1.entities.predict_pipeline_params import (PredictParams,
                                                        PredictParamsSchema)
from homework1.features.build_features import column_transformer, make_features
from homework1.models.fit_predict import deserialize_model, predict_model

logger = logging.getLogger("ml_project")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(levelname)s: %(name)s [%(asctime)s] %(message)s")
file_handler = logging.FileHandler(f"logs/predict.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def predict_pipeline(predict_pipeline_params: PredictParams) -> None:
    """
    Get predictions from model and data artifacts
    :param predict_pipeline_params: parameters dataclass
    :return: None
    """
    logger.info("Loading data...")
    data = pd.read_csv(predict_pipeline_params.raw_data_path)
    logger.info(f"Data shape is {data.shape}")

    logger.info("Loading model...")
    model = deserialize_model(predict_pipeline_params.model_path)
    logger.info(f"Loaded: {model}")

    feature_transformer = column_transformer(predict_pipeline_params.feature_params)
    feature_transformer.fit(data)

    logger.info("Making features...")
    features, target = make_features(
        feature_transformer,
        data,
        predict_pipeline_params.feature_params,
        test_mode=False,
    )
    logger.info(f"Features shape is {features.shape}")

    logger.info("Making predictions...")
    predictions = predict_model(
        model, features, predict_pipeline_params.feature_params.use_log_trick
    )
    logger.info(f"Predictions shape is {predictions.shape}")

    data["predictions"] = predictions
    logger.info(f"Saving predictions to {predict_pipeline_params.proceed_data_path}...")
    data.to_csv(predict_pipeline_params.proceed_data_path)


@hydra.main(config_path="../configs", config_name="predict_config.yaml")
def main(config: DictConfig) -> None:
    """
    Hydra wrapper for parsing CLI arguments
    :return: None
    """
    os.chdir(hydra.utils.to_absolute_path("."))
    schema = PredictParamsSchema()
    logger.info(f"Train configurations is:\n{OmegaConf.to_yaml(config)}")
    config = schema.load(config)
    predict_pipeline(config)


if __name__ == "__main__":
    main()
