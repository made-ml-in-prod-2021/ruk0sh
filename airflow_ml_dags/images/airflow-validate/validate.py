import json
import os
import pickle

import click
import pandas as pd
from sklearn.metrics import f1_score


@click.command("train")
@click.option("--data-dir")
@click.option("--model-dir")
def validate(data_dir: str, model_dir: str):
    # Load data and model
    val = pd.read_csv(os.path.join(data_dir, "val.csv"), index_col=0)
    X_val = val.drop("target", axis=1).values
    y_val = val["target"].values
    with open(os.path.join(model_dir, "model.pkl"), "rb") as input_file:
        model = pickle.load(input_file)
    # Get metrics
    preds = model.predict(X_val)
    acc = model.score(X_val, y_val)
    f1 = f1_score(y_val, preds, average="micro")
    # Save metrics to local filesystem
    metrics = dict(Accuracy=acc, F1_Score=f1)
    os.makedirs(model_dir, exist_ok=True)
    with open(os.path.join(model_dir, "metrics.json"), "w") as output_file:
        json.dump(model, output_file)


if __name__ == '__main__':
    validate()
