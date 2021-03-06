# Machine Learning in Production Course: Homework 3
Maintainer: [Ruslan Akhmerov](https://data.mail.ru/profile/r.akhmerov/)

Status: 99.9% ready for PR 😅

## Configure
Airflow parameters can be found and changed in `dags/constants.py`

## Run Airflow
From directory with `docker-compose.yml`:
```bash
# Unix host
export GMAIL_USR=your_login@gmail.com
export GMAIL_PWD=your_gmail_password
export FERNET_KEY=$(python -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")

# Windows host
set GMAIL_USR=your_login@gmail.com
set GMAIL_PWD=your_gmail_password
python -c "import os; from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY);" > tmp.txt
set /P FERNET_KEY=<tmp.txt
del tmp.txt

# Any host
docker-compose up --build
```

## Stop Airflow
```bash
docker-compose down
docker system prune  # yes
docker volume prune  # yes
docker network prune  # yes
```

## Test DAGs
Tests will probably crash on Windows host due to: https://stackoverflow.com/questions/52779920/why-is-signal-sigalrm-not-working-in-python-on-windows
```bash
pytest -v
```

## Project Roadmap
- [X] Поднимите airflow локально, используя docker compose (можно использовать из примера https://github.com/made-ml-in-prod-2021/airflow-examples/)
- [X] (5 баллов) Реализуйте dag, который генерирует данные для обучения модели (генерируйте данные, можете использовать как генератор синтетики из первой дз, так и что-то из датасетов sklearn), вам важно проэмулировать ситуации постоянно поступающих данных - записывайте данные в /data/raw/{{ ds }}/data.csv, /data/raw/{{ ds }}/target.csv
- [X] (10 баллов) Реализуйте dag, который обучает модель еженедельно, используя данные за текущий день. В вашем пайплайне должно быть как минимум 4 стадии, но дайте волю своей фантазии=)
    - [X] подготовить данные для обучения(например, считать из /data/raw/{{ ds }} и положить /data/processed/{{ ds }}/train_data.csv)
    - [X] расплитить их на train/val
    - [X] обучить модель на train (сохранить в /data/models/{{ ds }} 
    - [X] провалидировать модель на val (сохранить метрики к модельке)
- [X] Реализуйте dag, который использует модель ежедневно (5 баллов)
    - [X] принимает на вход данные из пункта 1 (data.csv)
    - [ ] считывает путь до модельки из airflow variables(идея в том, что когда нам нравится другая модель и мы хотим ее на прод 
    - [X] делает предсказание и записывает их в /data/predictions/{{ds }}/predictions.csv
- [X] Реализуйте сенсоры на то, что данные готовы для дагов тренировки и обучения (3 доп балла)
- [X] вы можете выбрать 2 пути для выполнения ДЗ. 
    - [ ] поставить все необходимые пакеты в образ с airflow и использовать bash operator, python operator (0 баллов)
    - [X] использовать DockerOperator, тогда выполнение каждой из тасок должно запускаться в собственном контейнере
        - [X] 1 из дагов реализован с помощью DockerOperator (5 баллов)
        - [X] все даги реализованы только с помощью DockerOperator (10 баллов) (пример https://github.com/made-ml-in-prod-2021/airflow-examples/blob/main/dags/11_docker.py).
    По технике, вы можете использовать такую же структуру как в примере, пакую в разные докеры скрипты, можете использовать общий докер с вашим пакетом, но с разными точками входа для разных тасок. 
    Прикольно, если вы покажете, что для разных тасок можно использовать разный набор зависимостей.
    https://github.com/made-ml-in-prod-2021/airflow-examples/blob/main/dags/11_docker.py#L27 в этом месте пробрасывается путь с хостовой машины, используйте здесь путь типа /tmp или считывайте из переменных окружения.
- [X] Протестируйте ваши даги (5 баллов) https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
- [ ] В docker compose так же настройте поднятие mlflow и запишите туда параметры обучения, метрики и артефакт(модель) (5 доп баллов)
- [ ] вместо пути в airflow variables  используйте апи Mlflow Model Registry (5 доп баллов)
- [X] Настройте alert в случае падения дага (3 доп. балла) https://www.astronomer.io/guides/error-notifications-in-airflow
- [X] традиционно, самооценка (1 балл)


## Самооценка
```
  0  За то, что я есть
+ 5  DAG генерации данных
+ 10 DAG пайплайна обучения модели
+ 5  DAG генерации и хранения предсказаний
+ 3' Настроил сенсоры, всё по расписанию
+ 10 Всё на докер-операторах
+ 5  Написаны тесты на успешную загрузку DAG-ов и их соответствие ожидаемой структуре
+ 0' Не настраивал MLFlow (как-то очень уж потно, но ещё не вечер)
+ 0' Не взился с Mlflow Model Registry
+ 3' Настроил alert
+ 1  Самооценочка
-------------------------------------------------------------------------------------
```
**ИТОГО: 36 / 36 базовых баллов + 6 / 16 дополнительных =** `42 / 52 баллов`
