import click
import numpy as np
import pandas as pd

CAT_FEATURES = [
    "ca",
    "cp",
    "exang",
    "fbs",
    "restecg",
    "sex",
    "slope",
    "thal",
]
NUM_FEATURES = ["age", "chol", "oldpeak", "thalach", "trestbps"]
TARGET_COL = "target"


@click.command()
@click.option(
    "-m",
    "--mock",
    type=str,
    default="data/raw/heart.csv",
    help="path to real .csv file to mock it",
)
@click.option(
    "-s", "--size", type=int, default=1000, help="number of rows in mocked data"
)
@click.option(
    "-o",
    "--output",
    type=str,
    default="data/test_data/generated.csv",
    help="output path",
)
def generate_cli(
    size: int, mock: str, output: str, writefile: bool = True
) -> pd.DataFrame:
    generate(size=size, mock=mock, output=output, writefile=writefile)


def generate(size: int, mock: str, output: str, writefile: bool = True) -> pd.DataFrame:
    origin_df = pd.read_csv(mock)
    res_df = pd.DataFrame(index=range(size), columns=origin_df.columns)
    for colname, coldata in origin_df.iteritems():
        if colname in NUM_FEATURES:
            res_df[colname] = np.random.uniform(
                low=coldata.min(), high=coldata.max(), size=(size,)
            )
        elif colname in CAT_FEATURES or colname == TARGET_COL:
            res_df[colname] = np.random.choice(coldata.unique(), size=size)
        else:
            raise ValueError(f"Unexpected column: {colname}")
    if writefile:
        res_df.to_csv(output)
    return res_df


if __name__ == "__main__":
    generate_cli()
