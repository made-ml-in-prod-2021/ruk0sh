FROM python:3.9-slim

COPY requirements.txt model.pkl app.py constants.py ./

RUN apt-get update \
    && apt-get install -y git \
    && apt-get clean \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir "git+https://github.com/made-ml-in-prod-2021/ruk0sh@homework1#egg=homework1&subdirectory=ml_project"

WORKDIR .

ENV PATH_TO_MODEL="/model.pkl"

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]