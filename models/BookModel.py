from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.orm import relationship
from models.BaseModel import EntityMeta
from models.BookAuthorAssociation import book_author_association

class Book(EntityMeta):
    __tablename__ = "books"

    # Define id as UUID with primary key and default value
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
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
