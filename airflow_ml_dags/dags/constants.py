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
DATA_RAW_DIR = "/data/raw/{{ ds }}"
LOCAL_FS_DATA_DIR = "/C/dev/MADE_2_PML/ruk0sh/airflow_ml_dags/data"