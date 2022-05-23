"""
Main file
"""
from os.path import join, dirname
import logging
import uvicorn

from fastapi import FastAPI
from fastapi.logger import logger as fastapi_logger
from dotenv import load_dotenv

DOTENV_PATH = join(dirname(__file__), '.env')
load_dotenv(DOTENV_PATH)

from core.config import API_PREFIX, OPENAPI_URL, DOCS_URL, REDOC_URL, API_GRAPHQL_PREFIX
#from routers import router as api_router, graphql_router
from routers import rest_router, graphql_router
gunicorn_logger = logging.getLogger("gunicorn")

app = FastAPI()

app = FastAPI(
    title="Studio Sol Test API",
    description="API with services for Studio Sol test",
    version="0.0.1",
    openapi_url=OPENAPI_URL,
    docs_url=DOCS_URL,
    redoc_url=REDOC_URL,
)

app.include_router(rest_router, prefix=API_PREFIX)
app.include_router(graphql_router, prefix=API_GRAPHQL_PREFIX)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
else:
    logging.info("------------------ Application Started -------------------")
    fastapi_logger.setLevel(gunicorn_logger.level)
