from datetime import timedelta

from airflow.utils.dates import days_ago


DEFAULT_ARGS = {
    "owner": "airflow",
    "email": ["airflow@example.com"],
    "email_on_failure": True,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}
START_DATE = days_ago(1)
DATA_RAW_DIR = "data/raw/{{ ds }}"
DATA_PROCESSED_DIR = "data/processed/{{ ds }}"
DATA_MODEL_DIR = "data/models/{{ ds }}"
PREDICTIONS_DIR = "data/predictions/{{ ds }}"
LOCAL_FS_DATA_DIR = "/C/dev/MADE_2_PML/ruk0sh/airflow_ml_dags/data"
AIRFLOW_BASE_DIR = "usr/local/airflow"