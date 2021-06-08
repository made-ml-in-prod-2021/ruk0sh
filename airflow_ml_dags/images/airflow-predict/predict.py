import pickle
import os

import numpy as np
import pandas as pd
import click


@click.command("predict")
@click.option("--input-dir")
@click.option("--output-dir")
@click.option("--model-dir")
def predict(input_dir: str, output_dir: str, model_dir: str):
    data = pd.read_csv(os.path.join(input_dir, "data.csv"), index_col=0)
    with open(os.path.join(model_dir, "model.pkl"), "rb") as input_file:
        model = pickle.load(input_file)
    with open(os.path.join(model_dir, "scaler.pkl"), "rb") as input_file:
        scaler = pickle.load(input_file)

    preds = model.predict(scaler.transform(data.values)).astype(np.int)
    os.makedirs(output_dir, exist_ok=True)
    np.savetxt(os.path.join(output_dir, "prediction.csv"), preds)


if __name__ == '__main__':
    predict()
