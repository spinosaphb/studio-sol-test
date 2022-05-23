"""
Models
"""
from pydantic import BaseModel
import strawberry

class AlphaString(BaseModel):
    """
    Model for Alpha String
    """
    text: str

class AlphaStringReponse(BaseModel):
    """
    Model for Alpha String Response
    """
    value: str
    number: int

@strawberry.type
class AlphaStringReponseGQL:
    value: str
    number: int
