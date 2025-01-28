from typing import List, Optional
from fastapi import Depends
from models.AuthorModel import Author
from models.BookModel import Book
from repositories.AuthorRepository import AuthorRepository
from repositories.BookRepository import BookRepository
from schemas.pydantic.AuthorSchema import AuthorSchema
from schemas.pydantic.BookSchema import BookSchema, BookAuthorPostRequestSchema

class BookService:
    authorRepository: AuthorRepository
    bookRepository: BookRepository

    def __init__(
        self,
        authorRepository: AuthorRepository = Depends(),
        bookRepository: BookRepository = Depends(),
    ) -> None:
        self.authorRepository = authorRepository
        self.bookRepository = bookRepository

    def create(self, book_body: BookSchema) -> Book:
        # Create and return the Book entity
        return self.bookRepository.create(Book(name=book_body.name))

    def delete(self, book_id: int) -> None:
        # Delete a book by ID
        return self.bookRepository.delete(Book(id=book_id))

    def get(self, book_id: int) -> Book:
        # Get a book by ID
        return self.bookRepository.get(Book(id=book_id))

    def list(
        self,
        name: Optional[str] = None,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
    ) -> List[Book]:
        # List books with optional filtering and pagination
        return self.bookRepository.list(name, pageSize, startIndex)

    def update(self, book_id: int, book_body: BookSchema) -> Book:
        # Update an existing book by ID
        return self.bookRepository.update(
            book_id, Book(name=book_body.name)
        )

    def get_authors(self, book_id: int) -> List[Author]:
        # Get all authors for the book by ID
        book = self.bookRepository.get(Book(id=book_id))
        return book.authors

    def add_author(
        self,
        book_id: int,
        author_body: BookAuthorPostRequestSchema,
    ) -> List[Author]:
        # Add an author to the book
        author = self.authorRepository.get(Author(id=author_body.author_id))
        book = self.bookRepository.get(Book(id=book_id))
        book.authors.append(author)
        self.bookRepository.update(book_id, book)

        return book.authors

    def remove_author(self, book_id: int, author_id: int) -> List[Author]:
        # Remove an author from the book
        book = self.bookRepository.get(Book(id=book_id))
        book.authors = [author for author in book.authors if author.id != author_id]
        self.bookRepository.update(book_id, book)

        return book.authors
