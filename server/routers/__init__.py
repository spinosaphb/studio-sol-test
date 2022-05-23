from fastapi import APIRouter

from routers import root, graphql

router = APIRouter()
router.include_router(root.router)

graphql_router = graphql.graphql_app