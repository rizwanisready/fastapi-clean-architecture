from typing import List, Optional
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

    def delete(self, author_id: int) -> None:
        # Delete an author by ID
        return self.authorRepository.delete(Author(id=author_id))

    def get(self, author_id: int) -> Author:
        # Get an author by ID
        return self.authorRepository.get(Author(id=author_id))

    def list(
        self,
        name: Optional[str] = None,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
    ) -> List[Author]:
        # List authors with optional filtering and pagination
        return self.authorRepository.list(name, pageSize, startIndex)

    def update(self, author_id: int, author_body: AuthorSchema) -> Author:
        # Update an existing author by ID
        return self.authorRepository.update(
            author_id, Author(name=author_body.name)
        )

    def get_books(self, author_id: int) -> List[Book]:
        # Get all books for the author by ID
        author = self.authorRepository.get(Author(id=author_id))
        return author.books
