from dataclasses import dataclass, field


@dataclass()
class TrainParams:
    model_type: str = field(default="CatBoostRegressor")
    random_state: int = field(default=42)
