from pydantic import BaseModel
# Book post request schema with just the name field
class BookPostRequestSchema(BaseModel):
    name: str

# Book schema with UUID for the id field
class BookSchema(BookPostRequestSchema):
    id: int

# BookAuthor schema to associate an author by UUID
class BookAuthorPostRequestSchema(BaseModel):
    author_id: int
