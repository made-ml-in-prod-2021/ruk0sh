import pytest
from airflow.models import DagBag


@pytest.fixture
def dag_bag():
    return DagBag(dag_folder="dags/", include_examples=False)


@pytest.mark.parametrize(
    "expected, dag_id",
    [
        pytest.param(
            {"docker-airflow-download-data": []},
            "download_data",
        ),
        pytest.param(
            {
                "features-sensor": ["preprocess-data"],
                "target-sensor": ["preprocess-data"],
                "preprocess-data": ["split-data"],
                "split-data": ["train-model"],
                "train-model": ["validate"],
                "validate": [],
            },
            "train_pipeline",
        ),
        pytest.param(
            {
                "data-sensor": ["predict"],
                "model-sensor": ["predict"],
                "scaler-sensor": ["predict"],
                "predict": [],
            },
            "predict_pipeline",
        )
    ],
)
def test_dag_structure(dag_bag, expected, dag_id):
    dag = dag_bag.get_dag(dag_id=dag_id)
    assert dag.task_dict.keys() == expected.keys(), (
        f"Task ids in DAG {dag_id} doesn't match.\n"
        f"Expected: {expected.keys()}\n"
        f"Got: {dag.task_dict.keys()}"
    )
    for task_id, downstream in expected.items():
        assert dag.has_task(task_id), (
            f"Task {task_id} wasn't found in DAG {dag_id}"
        )
        task = dag.get_task(task_id)
        assert task.downstream_task_ids == set(downstream), (
            f"List of downstream tasks for task {task_id} doesn't match expectations.\n"
            f"Expected: {set(downstream)}\n"
            f"Got: {task.downstream_task_ids}"
        )


@pytest.mark.parametrize(
    "dag_id, num_tasks",
    [
        pytest.param("download_data", 1),
        pytest.param("train_pipeline", 6),
        pytest.param("predict_pipeline", 4),
    ],
)
def test_dag_can_load_succesfully(dag_bag, dag_id, num_tasks):
    dag = dag_bag.get_dag(dag_id=dag_id)
    assert dag_bag.import_errors == {}, (
        f"Import errors occures in DAG: {dag_id}"
    )
    assert dag is not None, (
        f"Seems like DAG didn't loaded successfully: {dag_id}"
    )
    assert len(dag.tasks) == num_tasks, (
        f"Number of tasks in DAG {dag_id} doesn't match.\n"
        f"Expected: {num_tasks}\nGot: {len(dag.tasks)}"
    )
