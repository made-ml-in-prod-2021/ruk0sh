import os

import click
import pandas as pd
from sklearn.model_selection import train_test_split


@click.command("split")
@click.option("--input-dir")
@click.option("--output-dir")
def split_data(input_dir: str, output_dir: str):
    data = pd.read_csv(os.path.join(input_dir, "data.csv"))
    train, val = train_test_split(data, test_size=0.2, random_state=42)
    os.makedirs(output_dir, exist_ok=True)
    train.to_csv(os.path.join(output_dir, "train.csv"))
    val.to_csv(os.path.join(output_dir, "val.csv"))


if __name__ == '__main__':
    split_data()
