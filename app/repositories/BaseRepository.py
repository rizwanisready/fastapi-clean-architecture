from typing import Type, List, Generic, TypeVar
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app.configs.FastAPIExceptions import NotFoundError, DuplicatedError, DatabaseError
from app.repositories.RepositoryMeta import RepositoryMeta

M = TypeVar("M")
K = TypeVar("K")

class BaseRepository(RepositoryMeta[M, K], Generic[M, K]):
    def __init__(self, db: Session, model_class: Type[M]):
        self.db = db
        self.model_class = model_class  # Store the model class

    def create(self, instance: M) -> M:
        try:
            self.db.add(instance)
            self.db.commit()
            self.db.refresh(instance)
            return instance
        except IntegrityError as e:
            self.db.rollback()
            raise DuplicatedError("A duplicate entry error occurred during creation") from e
        except SQLAlchemyError as e:
            self.db.rollback()
            raise DatabaseError("An error occurred during creation") from e

    def delete(self, id: K) -> None:
        try:
            instance = self.db.query(self.model_class).get(id)
            if not instance:
                raise NotFoundError(f"{self.model_class.__name__} with ID {id} not found")
            self.db.delete(instance)
            self.db.commit()
        except SQLAlchemyError as e:
            self.db.rollback()
            raise DatabaseError("An error occurred during deletion") from e

    def get(self, id: K) -> M:
        try:
            instance = self.db.query(self.model_class).get(id)
            if not instance:
                raise NotFoundError(f"{self.model_class.__name__} with ID {id} not found")
            return instance
        except SQLAlchemyError as e:
            self.db.rollback()
            raise NotFoundError(f"{self.model_class.__name__} with ID {id} not found")

    def list(self, limit: int, start: int) -> List[M]:
        try:
            return self.db.query(self.model_class).offset(start).limit(limit).all()
        except SQLAlchemyError as e:
            raise DatabaseError("An error occurred during listing") from e

    def update(self, id: K, instance: M) -> M:
        try:
            existing_instance = self.db.query(self.model_class).get(id)
            if not existing_instance:
                raise NotFoundError(f"{self.model_class.__name__} with ID {id} not found")
            self.db.merge(instance)
            self.db.commit()
            self.db.refresh(instance)
            return instance
        except SQLAlchemyError as e:
            self.db.rollback()
            raise DatabaseError("An error occurred during update") from e
