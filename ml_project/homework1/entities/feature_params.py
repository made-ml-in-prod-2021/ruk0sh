from dataclasses import dataclass
from typing import List, Optional


@dataclass()
class FeatureParams:
    cat_features: List[str]
    num_features: List[str]
    drop_features: List[str]
    target_col: Optional[str]
