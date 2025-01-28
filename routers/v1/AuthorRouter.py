from typing import List, Optional
from uuid import UUID
from fastapi import APIRouter, Depends, status

from schemas.pydantic.AuthorSchema import (
    AuthorPostRequestSchema,
    AuthorSchema,
)
from schemas.pydantic.BookSchema import BookSchema
from services.AuthorService import AuthorService

AuthorRouter = APIRouter(
    prefix="/v1/authors", tags=["author"]
)

@AuthorRouter.get("/", response_model=List[AuthorSchema])
def index(
    name: Optional[str] = None,
    pageSize: Optional[int] = 100,
    startIndex: Optional[int] = 0,
    authorService: AuthorService = Depends(),
):
    return [
        author.normalize()
        for author in authorService.list(
            name, pageSize, startIndex
        )
    ]

@AuthorRouter.get("/{id}", response_model=AuthorSchema)
def get(id: UUID, authorService: AuthorService = Depends()):
    return authorService.get(id).normalize()

@AuthorRouter.post(
    "/",
    response_model=AuthorSchema,
    status_code=status.HTTP_201_CREATED,
)
def create(
    author: AuthorPostRequestSchema,
    authorService: AuthorService = Depends(),
):
    return authorService.create(author).normalize()

@AuthorRouter.patch("/{id}", response_model=AuthorSchema)
def update(
    id: UUID,
    author: AuthorPostRequestSchema,
    authorService: AuthorService = Depends(),
):
    return authorService.update(id, author).normalize()

@AuthorRouter.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    id: UUID, authorService: AuthorService = Depends()
):
    authorService.delete(id)
    return None

@AuthorRouter.get("/{id}/books/", response_model=List[BookSchema])
def get_books(
    id: UUID, authorService: AuthorService = Depends()
):
    return [
        book.normalize()
        for book in authorService.get_books(id)
    ]
