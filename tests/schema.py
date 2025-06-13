from pydantic import BaseModel, field_validator, ConfigDict
from typing import Optional, Union


class CypherQuery(BaseModel):
    model_config = ConfigDict(extra='forbid')

    name: str
    guid: str
    prebuilt: bool = False
    platforms: Union[str, list[str]]
    category: str
    description: Optional[str] = None
    query: str
    revision: int
    resources: Optional[Union[str, list[str]]] = None
    acknowledgements: Optional[Union[str, list[str]]] = None

    @field_validator('platforms', mode='after')  
    @classmethod
    def platforms_is_list(cls, value: str | list[str]) -> list[str]:
        return value if isinstance(value, list) else [value]

    @field_validator('resources', mode='after')
    @classmethod
    def resources_is_list(cls, value: str | list[str]) -> list[str]:
        return value if isinstance(value, list) else [value]

    @field_validator('acknowledgements', mode='after')
    @classmethod
    def acknowledgementsis_list(cls, value: str | list[str]) -> list[str]:
        return value if isinstance(value, list) else [value]
