from fastapi import Depends, FastAPI

from app.configs.Environment import get_environment_variables
from app.metadata.Tags import Tags
from app.models.BaseModel import init
from app.api.v1.author_endpoints.AuthorRouter import AuthorRouter
from app.api.v1.book_endpoints.BookRouter import BookRouter

# Application Environment Configuration
env = get_environment_variables()

# Core Application Instance
app = FastAPI(
    title=env.APP_NAME,
    version=env.API_VERSION,
    openapi_tags=Tags,
)

# Add Routers
app.include_router(AuthorRouter)
app.include_router(BookRouter)

# Initialise Data Model Attributes
init()
