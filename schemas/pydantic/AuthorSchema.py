from pydantic import BaseModel
class AuthorPostRequestSchema(BaseModel):
    name: str

# Author schema with UUID as the type for id
class AuthorSchema(AuthorPostRequestSchema):
    id: int
