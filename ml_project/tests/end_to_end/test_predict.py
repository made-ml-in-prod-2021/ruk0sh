import pandas as pd

from homework1.predict import predict_pipeline


def test_predict_e2e(predict_pipeline_params_fixture):
    predict_pipeline(predict_pipeline_params_fixture)
    preds = pd.read_csv(predict_pipeline_params_fixture.proceed_data_path)
    assert (
        "predictions" in preds.columns
    ), f"Predictions column not found in file, columns are: {preds.columns}"
