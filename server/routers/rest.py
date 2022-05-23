"""
API Rest Routers
"""
from fastapi import APIRouter
from models.alpha_string import AlphaString, AlphaStringReponse
from services.alpha_string import find_max_roman_number

router = APIRouter()

@router.post("/search/", tags=['Alpha'], response_model=AlphaStringReponse)
async def search_max_number(alpha_string: AlphaString):
    max_alpha_string, qtd = find_max_roman_number(alpha_string.text)
    return AlphaStringReponse(
        value=max_alpha_string,
        number=qtd
    )