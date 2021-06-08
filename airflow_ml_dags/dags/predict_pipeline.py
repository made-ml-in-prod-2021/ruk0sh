from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.sensors.filesystem import FileSensor

from constants import (
    DEFAULT_ARGS,
    LOCAL_FS_DATA_DIR,
    START_DATE,
    DATA_RAW_DIR,
    DATA_MODEL_DIR,
    DATA_PREDICTIONS_DIR,
)


with DAG(
    "predict_pipeline",
    default_args=DEFAULT_ARGS,
    schedule_interval="@daily",
    start_date=START_DATE,
    tags=["custom"],
) as dag:

    data_sensor = FileSensor(
        task_id="data-sensor",
        filepath=f"{DATA_RAW_DIR}/data.csv",
        timeout=60 * 10,
        poke_interval=10,
        retries=50,
        mode="reschedule",
        fs_conn_id="fs_default",
    )

    model_sensor = FileSensor(
        task_id="model-sensor",
        filepath=f"{DATA_MODEL_DIR}/model.pkl",
        timeout=60 * 10,
        poke_interval=10,
        retries=50,
        mode="reschedule",
        fs_conn_id="fs_default",
    )

    scaler_sensor = FileSensor(
        task_id="scaler-sensor",
        filepath=f"{DATA_MODEL_DIR}/scaler.pkl",
        timeout=60 * 10,
        poke_interval=10,
        retries=50,
        mode="reschedule",
        fs_conn_id="fs_default",
    )

    predict = DockerOperator(
        image="airflow-predict",
        command=f"--input-dir={DATA_RAW_DIR} "
                f"--output-dir={DATA_PREDICTIONS_DIR} "
                f"--model-dir={DATA_MODEL_DIR}",
        network_mode="bridge",
        task_id="predict",
        do_xcom_push=False,
        volumes=[f"{LOCAL_FS_DATA_DIR}/:/data"],
    )

    [data_sensor, model_sensor, scaler_sensor] >> predict
