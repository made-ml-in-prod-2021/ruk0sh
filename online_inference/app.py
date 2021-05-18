import logging
import os
from typing import List, Optional, Union

import pandas as pd
import uvicorn
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from constants import (
    PATH_TO_MODEL,
    LANDING_MESSAGE,
    ModelResponse,
    DataSample,
    STATUS_CODE_DATA_VALIDATION_FAILED,
)
from homework1.models.fit_predict import (
    deserialize_model,
    predict_model,
    ValidModelClass,
)


logger = logging.getLogger(__name__)
app = FastAPI()
model: Optional[ValidModelClass] = None


def make_predict(
    data: List[List[Union[int, float]]], features: List[str], model: ValidModelClass
) -> List[ModelResponse]:
    df = pd.DataFrame(data=data, columns=features)
    preds = predict_model(model=model, features=df)
    resp = [ModelResponse(id=idx, proba=proba) for idx, proba in zip(df.index, preds)]
    return resp


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=STATUS_CODE_DATA_VALIDATION_FAILED,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )


@app.get("/")
def main():
    return LANDING_MESSAGE


# You would be surprised when routes ending with 'z' would not work on
# the Google Cloud Platform due to internal naming convention.
@app.get("/health")
def health() -> bool:
    return not (model is None)


@app.on_event("startup")
def preload_model():
    global model
    model_path = os.getenv("PATH_TO_MODEL", PATH_TO_MODEL)
    logger.info(f"Loading model from {model_path}")
    if model_path is None:
        error_message = f"PATH_TO_MODEL is not specified or is None"
        logger.error(error_message)
        raise FileNotFoundError(error_message)
    model = deserialize_model(model_path)


@app.get("/predict")
def predict(request: DataSample):
    logger.info("Got prediction query")
    logger.info(f"data: {request.data}")
    logger.info(f"features: {request.features}")
    logger.info(f"model: {model}")
    resp = make_predict(request.data, request.features, model)
    return resp


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=os.getenv("PORT", 8000))
