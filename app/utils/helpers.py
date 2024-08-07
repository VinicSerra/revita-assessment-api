from typing import List, Any
from pydantic import BaseModel


def to_schema(obj: Any | List[Any], schema: BaseModel) -> BaseModel | List[BaseModel]:
    """retorna um Model (ou lista de Models) SQLAlchemy para um modelo do Pydantic (ou lista de modelos do Pydantic)"""
    if isinstance(obj, list):
        return [schema.model_validate(model) for model in obj]
    else:
        return schema.model_validate(obj)