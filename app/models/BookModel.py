from sqlalchemy import Integer, Column, String  # Add other necessary imports as well
from sqlalchemy.orm import relationship
from app.models.BaseModel import EntityMeta
from app.models.BookAuthorAssociation import book_author_association


class Book(EntityMeta):
    __tablename__ = "books"

    # Define id as UUID with primary key and default value
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)

    # Many-to-many relationship with Author
    authors = relationship(
        "Author",
        lazy="dynamic",
        secondary=book_author_association,
    )

    def normalize(self):
        # Normalize method returns the data as a dictionary, converting id and name to strings
        return {
            "id": str(self.id),
            "name": self.name,
        }
