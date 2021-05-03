from dataclasses import dataclass, field
from typing import List, Optional


@dataclass()
class FeatureParams:
    cat_features: List[str]
    num_features: List[str]
    drop_features: List[str]
    target_col: Optional[str]
    use_log_trick: bool = field(default=True)  # TODO: WAT?
