import os
import pickle

import click
import pandas as pd
from sklearn.linear_model import LogisticRegression


@click.command("train")
@click.option("--input-dir")
@click.option("--output-dir")
def train_model(input_dir: str, output_dir: str):
    model = LogisticRegression(random_state=42)
    data = pd.read_csv(os.path.join(input_dir, "train.csv"), index_col = 0)
    X_train = data.drop("target", axis=1).values
    y_train = data["target"].values
    model.fit(X_train, y_train)
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "model.pkl"), "wb") as output_file:
        pickle.dump(model, output_file)


if __name__ == '__main__':
    train_model()
