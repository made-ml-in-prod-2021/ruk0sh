from pathlib import Path

from homework1.train import train_pipeline


def test_train_e2e(train_pipeline_params_fixture):
    path_to_model, metrics = train_pipeline(train_pipeline_params_fixture)
    assert Path(path_to_model).exists(), f"Path to saved model doesn't exist: {path_to_model}"
    assert len(metrics.values()) > 0, f"Something with metrics: {metrics}"
