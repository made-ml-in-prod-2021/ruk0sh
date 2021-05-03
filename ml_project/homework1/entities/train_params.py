from dataclasses import dataclass, field


@dataclass()
class TrainParams:
    model_type: str = field(default="CatBoostClassifier")
    random_state: int = field(default=42)
