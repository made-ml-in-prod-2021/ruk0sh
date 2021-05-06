# Machine Learning in Production Course: Homework 1
Maintainer: [Ruslan Akhmerov](https://data.mail.ru/profile/r.akhmerov/)

Status: Under Construction

## Load data:

Download [data](https://www.kaggle.com/ronitf/heart-disease-uci) and extract into folder `data/raw`

```bash
mkdir -p data/raw && unzip archive.zip -d data/raw
```

## Prerequisites

* [`Python 3`](https://www.python.org/)
* `virtualenv` (`pip install virtualenv`)

Create and activate virtual environment:

```bash
virtualenv venv
. venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Installation

```bash
pip install .
```

### Fit Model

```bash
python -m homework1.train
```

### Make Predictions

```bash
python -m homework1.predict
```

### Generate Fake Trainable Data Sample

```bash
python -m tests.datagen
```

## Tests

```bash
pip install pytest, pytest-cov
python -m pytest . -v --cov
```

## Project Roadmap

- [X] Назовите ветку homework1 (1 балл)
- [X] положите код в папку ml_project
- [ ] В описании к пулл реквесту описаны основные "архитектурные" и тактические решения,
  которые сделаны в вашей работе. В общем, описание, что именно вы сделали и для чего,
  чтобы вашим ревьюерам было легче понять ваш код. (2 балла)
- [X] Выполнение EDA, закоммитьте ноутбук в папку с ноутбуками (2 баллов)
  - [X] Вы так же можете построить в ноутбуке прототип(если это вписывается в ваш стиль работы)
  - [ ] Можете использовать не ноутбук, а скрипт, который сгенерит отчет, закоммитьте и скрипт и отчет (за это + 1 балл)
- [X] Проект имеет модульную структуру (не все в одном файле) (2 баллов)
- [X] использованы логгеры (2 балла)
- [ ] написаны тесты на отдельные модули и на прогон всего пайплайна (3 баллов)
  - [ ] юнит тесты
  - [X] end2end тесты
- [X] Для тестов генерируются синтетические данные, приближенные к реальным (3 баллов)
  - ( ) можно посмотреть на библиотеки https://faker.readthedocs.io/en/, https://feature-forge.readthedocs.io/en/latest/
  - (X) можно просто руками посоздавать данных, собственноручно написанными функциями
  - ( ) как альтернатива, можно закоммитить файл с подмножеством трейна(это не оценивается)
- [X] Обучение модели конфигурируется с помощью конфигов в json или yaml,
  закоммитьте как минимум 2 корректные конфигурации,
  с помощью которых можно обучить модель (разные модели, стратегии split, preprocessing) (3 балла)
- [X] Используются датаклассы для сущностей из конфига, а не голые dict (3 балла)
- [X] Используйте кастомный трансформер (написанный своими руками) и протестируйте его(3 балла)
- [X] Обучите модель, запишите в readme как это предлагается (3 балла)
- [X] напишите функцию predict, которая примет на вход артефакт/ы от обучения,
  тестовую выборку(без меток) и запишет предикт, напишите в readme как это сделать (3 балла)
- [X] Используется hydra (https://hydra.cc/docs/intro/) (3 балла — доп баллы)
- [ ] Настроен CI (прогон тестов, линтера) на основе github actions (3 балла — доп баллы)
  (будем проходить дальше в курсе, но если есть желание поразбираться — welcome)
- [ ] Проведите самооценку, опишите, в какое колво баллов по вашему мнению
  стоит оценить вашу работу и почему (1 балл доп баллы)
  