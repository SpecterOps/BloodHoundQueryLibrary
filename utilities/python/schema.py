from pydantic import BaseModel, field_validator
from typing import Optional, Union


class CypherQuery(BaseModel):
    name: str
    guid: str
    prebuilt: bool = False
    platform: Union[str, list[str]]
    category: str
    description: Optional[str] = None
    query: str
    revision: int
    note: Optional[str] = None
    resources: Optional[Union[str, list[str]]] = None
    acknowledgement: Optional[Union[str, list[str]]] = None

    @field_validator('platform', mode='after')  
    @classmethod
    def platform_is_list(cls, value: str | list[str]) -> list[str]:
        return value if isinstance(value, list) else [value]