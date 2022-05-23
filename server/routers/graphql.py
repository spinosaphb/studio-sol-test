"""
GraphQL Routes
"""

import strawberry

from strawberry.fastapi import GraphQLRouter
from models.alpha_string import AlphaStringReponseGQL

from services.alpha_string import find_max_roman_number

@strawberry.type
class Query:
    @strawberry.field
    def hello() -> str:
        return "world"

@strawberry.type
class Mutation:
    @strawberry.mutation
    def search(text: str) -> AlphaStringReponseGQL:
        value, number = find_max_roman_number(text)
        return AlphaStringReponseGQL(value=value, number = number)

schema = strawberry.Schema(query=Query, mutation=Mutation)
router = GraphQLRouter(schema)