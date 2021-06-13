import requests
import logging

import numpy as np
import pandas as pd
import click


DEFAULT_HOST = "localhost"
DEFAULT_PORT = 8000
DEFAULT_NUM_REQUESTS = 5
DEFAULT_DATA_PATH = "ml_project/data/raw/heart.csv"
logger = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)


@click.command()
@click.option(
    "-d",
    "--data-path",
    type=str,
    default=DEFAULT_DATA_PATH,
    help="path to dataset to query from",
)
@click.option(
    "-h",
    "--host",
    type=str,
    default=DEFAULT_HOST,
    help="host where inference web-server is running",
)
@click.option(
    "-p",
    "--port",
    type=int,
    default=DEFAULT_PORT,
    help="port where inference web-server is running",
)
@click.option(
    "-n",
    "--num-requests",
    type=int,
    default=DEFAULT_NUM_REQUESTS,
    help="how many requests to perform",
)
def make_requests_cli(data_path, host, port, num_requests):
    make_requests(data_path, host, port, num_requests)


def make_requests(data_path, host, port, num_requests):
    data = pd.read_csv(data_path)
    data.drop("target", inplace=True, axis=1)
    request_features = data.columns
    logger.info(f"Would perform {num_requests} requests with features: {request_features}")
    request_features = list(range(len(data.columns)))  # For CatBoost internal validation compatibility
    for i in range(num_requests):
        request_data = [
            x.item() if isinstance(x, np.generic) else x for x in data.iloc[i].tolist()
        ]
        logger.info(f"Request #{i + 1}: {request_data}")
        response = requests.get(
            f"http://{host}:{port}/predict/",
            json={"data": [request_data], "features": request_features},
        )
        logger.info(f"Got responce, status code: {response.status_code}")
        logger.info(f"Response contents: {response.json()}")


def main():
    make_requests_cli()


if __name__ == "__main__":
    main()
