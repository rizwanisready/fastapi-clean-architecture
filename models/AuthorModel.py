from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from models.BaseModel import EntityMeta
from models.BookAuthorAssociation import (
    book_author_association,
)


class Author(EntityMeta):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String(16), nullable=False)
    books = relationship(
        "Book",
        lazy="dynamic",
        secondary=book_author_association,
        back_populates="authors",  # Added back_populates here
    )

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "name": self.name.__str__(),
        }
