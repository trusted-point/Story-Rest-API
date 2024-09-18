from typing import List, Optional
from pydantic import BaseModel

class ValidationErrorDetail(BaseModel):
    loc: List[Optional[str]]
    msg: str
    type: str

class ValidationErrorResponseModel(BaseModel):
    detail: List[ValidationErrorDetail]

class ErrorResponseModel(BaseModel):
    code: int
    message: str

