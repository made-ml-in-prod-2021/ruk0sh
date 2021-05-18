# Machine Learning in Production Course: Homework 1
Maintainer: [Ruslan Akhmerov](https://data.mail.ru/profile/r.akhmerov/)

Status: In Progress

## Docker
Build from local project
```bash
docker build -t ruk0sh/online_inference:v1 .
```

Pull from DockerHub
```bash
docker pull ruk0sh/online_inference:v1
```

## Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

Run via Docker container (recommended)
```bash
docker run --rm -p 8000:8000 ruk0sh/online_inference:v1
````

...via uvicorn
```bash
PATH_TO_MODEL=model.pkl uvicorn app:app --host 0.0.0.0 --port 8000
```

...via python
```bash
python path/to/app.py
```

Make requests
```bash
python path/to/make_request.py [OPTIONS]

Options:
  -d, --data-path TEXT        path to dataset to query from
  -h, --host TEXT             host where inference web-server is running
  -p, --port INTEGER          port where inference web-server is running
  -n, --num-requests INTEGER  how many requests to perform
  --help                      Show this message and exit.

```

## Docker Image Optimization
I started with example Dockerfile from course repo but with default python:3.9
With all dependencies image I was first able to pull off was mostrous `1,72 GB`
I switched to more lightweight python:3.9-slim and optimized RUN and COPY commands
to produce less layers, added commend for Git installation which is not included.
It's ended with `867 MB` disk usage. It looks like Image mage may be optimized
further by manual exclusion of unnecessary dependencies from requirements.txt.


## Project Roadmap

- [X] ветку назовите homework2, положите код в папку online_inference

- [X] Оберните inference вашей модели в rest сервис
  (вы можете использовать как FastAPI, так и flask,
  другие желательно не использовать, дабы не плодить излишнего разнообразия
  для проверяющих), должен быть endpoint /predict (3 балла)

- [ ] Напишите тест для /predict  (3 балла)
  (https://fastapi.tiangolo.com/tutorial/testing/, https://flask.palletsprojects.com/en/1.1.x/testing/)

- [X] Напишите скрипт, который будет делать запросы к вашему сервису -- 2 балла

- [X] Сделайте валидацию входных данных (например, порядок колонок не совпадает с трейном,
  типы не те и пр, в рамках вашей фантазии) (вы можете сохранить вместе с моделью доп информацию,
  о структуре входных данных, если это нужно) -- 3 доп балла
  https://fastapi.tiangolo.com/tutorial/handling-errors/
  возращайте 400, в случае, если валидация не пройдена

- [X] Напишите dockerfile, соберите на его основе образ и запустите локально
  контейнер(docker build, docker run), внутри контейнера должен запускать сервис,
  написанный в предущем пункте, закоммитьте его, напишите в readme корректную
  команду сборки (4 балл)

- [X] Оптимизируйте размер docker image (3 доп балла)
  (опишите в readme.md что вы предприняли для сокращения размера и каких результатов удалось добиться)
  https://docs.docker.com/develop/develop-images/dockerfile_best-practices/

- [X] опубликуйте образ в https://hub.docker.com/, используя docker push
  (вам потребуется зарегистрироваться) (2 балла)

- [X] напишите в readme корректные команды docker pull/run, которые должны привести к тому,
  что локально поднимется на inference ваша модель (1 балл)
  Убедитесь, что вы можете протыкать его скриптом из пункта 3

- [X] проведите самооценку -- 1 доп балл

- [X] создайте пулл-реквест и поставьте label -- hw2


## Самооценка
- Инференс обёрнут в REST API на базе FastAPI, есть все оговоренные endpoint'ы
  - 0 + 3 == 3 балла.
  
- Тесты писать пока не стал — очень боюсь не успеть в другими дедлайнами; может, добавлю позже;
  - 3 + 0 == 3 балла.
  
- Есть скрипт для обстрела веб-сервиса запросами, есть валидация исходных данныч (pydantic) по
порядку колонок и по допустимым даиапазонам значений для категориальных признаков.
  - 3 + 2 + 3 = 8 баллов.
  
- Докер-файл есть в репо, образ на его основе корректно создаётся и запускается, обстреливается
скриптом и отвечает. Образ залит на DockerHub, инструкции по обращению в README (то есть выше).
Проведена самооценка.
  - 8 + 4 + 2 + 1 + 1 = 16 баллов.
  
- Краткий рассказ об оптимизации докер-образа приведён выше в разделе Docker Image Optimization.
Там, в общем-то ничего особенного: минимизировал число слоёв, взял легковесную базу.
  - 16 + 3 = 19 баллов.
  
**ИТОГО: 12 / 15 базовых баллов + 7 / 7 дополнительных =** `19 / 22 баллов`
