from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from schema import FileCreate

from db import Base


class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    summary = Column(String)
    content = Column(String)
    path = Column(String)
    format = Column(String)
    size = Column(Integer)


def get_file(db: Session, file_id: int):
    return db.query(File).filter(File.id == file_id).first()


def get_files(db: Session, skip: int = 0, limit: int = 100):
    return db.query(File).offset(skip).limit(limit).all()


def create_file(db: Session, file: FileCreate):
    db_file = File(**file.model_dump())
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file
