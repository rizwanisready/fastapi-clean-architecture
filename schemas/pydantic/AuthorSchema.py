from pydantic import BaseModel
from uuid import UUID

class AuthorPostRequestSchema(BaseModel):
    name: str

# Author schema with UUID as the type for id
class AuthorSchema(AuthorPostRequestSchema):
    id: UUID
