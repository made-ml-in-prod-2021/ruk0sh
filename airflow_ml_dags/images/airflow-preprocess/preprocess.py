import os
import pickle

import click
import pandas as pd
from sklearn.preprocessing import StandardScaler


@click.command("preprocess")
@click.option("--input-dir")
@click.option("--output-dir")
@click.option("--model-dir")
def preprocess(input_dir: str, output_dir: str, model_dir: str):
    # Load data from local filesystem
    features = pd.read_csv(os.path.join(input_dir, "data.csv"))
    feature_cols = features.columns
    target = pd.read_csv(os.path.join(input_dir, "target.csv"))
    # Standardize features
    scaler = StandardScaler()
    features = pd.DataFrame(scaler.fit_transform(features))
    features.columns = feature_cols
    # Merge features and target for further splitting
    data = features.merge(target, right_index=True, left_index=True)
    # Save processed data to local filesystem
    os.makedirs(output_dir, exist_ok=True)
    data.to_csv(os.path.join(output_dir, "data.csv"))
    # Save scaler too
    os.makedirs(model_dir, exist_ok=True)
    with open(os.path.join(model_dir, "scaler.pkl"), "wb") as output_file:
        pickle.dump(scaler, output_file)


if __name__ == '__main__':
    preprocess()