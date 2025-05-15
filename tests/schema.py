from pydantic import BaseModel
from typing import Optional, Union, List


class CypherQuery(BaseModel):
    name: str
    guid: str
    platform: str
    category: str
    description: Optional[str] = None
    query: str
    revision: int
    note: Optional[str] = None
    resources: Optional[Union[str, List[str]]] = None
    acknowledgement: Optional[Union[str, List[str]]] = None
