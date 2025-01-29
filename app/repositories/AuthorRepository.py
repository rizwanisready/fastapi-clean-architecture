from typing import List, Optional
from fastapi import Depends
from sqlalchemy.orm import Session
from app.configs.Database import get_db_connection
from app.models.AuthorModel import Author
from app.repositories.BaseRepository import BaseRepository  # ✅ Import the class directly

class AuthorRepository(BaseRepository[Author, int]):  # ✅ Now it should work
    def __init__(self, db: Session = Depends(get_db_connection)):
        super().__init__(db, Author)  # ✅ Pass the model class

    def list(self, name: Optional[str] = None, limit: int = 100, start: int = 0) -> List[Author]:
        query = self.db.query(self.model_class)
        if name:  # ✅ Apply filter if name is provided
            query = query.filter(self.model_class.name.ilike(f"%{name}%"))        
        return query.offset(start).limit(limit).all()
