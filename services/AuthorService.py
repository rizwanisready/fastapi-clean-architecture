from typing import List, Optional
from uuid import UUID

from fastapi import Depends
from models.AuthorModel import Author
from models.BookModel import Book
from repositories.AuthorRepository import AuthorRepository
from schemas.pydantic.AuthorSchema import AuthorSchema


class AuthorService:
    authorRepository: AuthorRepository

    def __init__(self, authorRepository: AuthorRepository = Depends()) -> None:
        self.authorRepository = authorRepository

    def create(self, author_body: AuthorSchema) -> Author:
        # Create and return the Author entity
        return self.authorRepository.create(Author(name=author_body.name))

    def delete(self, author_id: UUID) -> None:
        # Delete an author by UUID
        return self.authorRepository.delete(Author(id=author_id))

    def get(self, author_id: UUID) -> Author:
        # Get an author by UUID
        return self.authorRepository.get(Author(id=author_id))

    def list(
        self,
        name: Optional[str] = None,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
    ) -> List[Author]:
        # List authors with optional filtering and pagination
        # You can add validations here for `pageSize` and `startIndex` if needed
        return self.authorRepository.list(name, pageSize, startIndex)

    def update(self, author_id: UUID, author_body: AuthorSchema) -> Author:
        # Update an existing author by UUID
        return self.authorRepository.update(
            author_id, Author(name=author_body.name)
        )

    def get_books(self, author_id: UUID) -> List[Book]:
        # Get all books for the author by UUID
        return self.authorRepository.get(Author(id=author_id)).books
