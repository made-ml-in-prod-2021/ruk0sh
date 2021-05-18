FROM python:3.9

COPY requirements.txt .
COPY model.pkl .
COPY app.py .
COPY constants.py .

RUN pip install -r requirements.txt
RUN pip install "git+https://github.com/made-ml-in-prod-2021/ruk0sh@homework1#egg=homework1&subdirectory=ml_project"

WORKDIR .

ENV PATH_TO_MODEL="/model.pkl"

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]