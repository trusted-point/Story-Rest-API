from pydantic import BaseModel
from typing import Optional

class ErrorResponseModel(BaseModel):
    code: int
    message: str
    