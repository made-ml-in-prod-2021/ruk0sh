from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.sensors.filesystem import FileSensor

from constants import (
    DEFAULT_ARGS,
    START_DATE,
    DATA_RAW_DIR,
    DATA_PROCESSED_DIR,
    LOCAL_FS_DATA_DIR,
    AIRFLOW_BASE_DIR
)


with DAG(
    "train_pipeline",
    default_args=DEFAULT_ARGS,
    schedule_interval="@weekly",
    start_date=START_DATE,
    tags=["custom"],
) as dag:

    features_sensor = FileSensor(
        task_id="features-sensor",
        filepath=f"{DATA_RAW_DIR}/data.csv",
        timeout=60 * 10,
        poke_interval=10,
        retries=50,
        mode="reschedule",
        fs_conn_id="fs_default",
    )

    target_sensor = FileSensor(
        task_id="target-sensor",
        filepath=f"{DATA_RAW_DIR}/target.csv",
        timeout=60 * 10,
        poke_interval=10,
        retries=50,
        mode="reschedule",
        fs_conn_id="fs_default",
    )

    preprocess_data = DockerOperator(
        image="airflow-preprocess",
        command=\
            f"--input-dir={DATA_RAW_DIR} "
            f"--output-dir={DATA_PROCESSED_DIR}",
        network_mode="bridge",
        task_id="preprocess-data",
        do_xcom_push=False,
        volumes=[f"{LOCAL_FS_DATA_DIR}/:/data"],
    )

    [features_sensor, target_sensor] >> preprocess_data
