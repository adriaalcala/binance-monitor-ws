"""Check price processor."""
import json
from typing import Any


def transform_to_json(data: str, **kwargs: Any) -> dict:
    """Transform to json."""
    return json.loads(data)
