from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Base, get_files, get_file
from db import engine, get_db
from schema import FileRead
from resource_handler import process_files
import configparser


Base.metadata.create_all(bind=engine)

app = FastAPI()

config = configparser.ConfigParser()
config.read('config.ini')
PATH = config.get("FILES", 'path')


@app.post("/refresh/")
def refresh(db: Session = Depends(get_db)):
    process_files(path=PATH, db=db)
    return {"Message": "Processing successful"}


@app.get("/file/list", response_model=list[FileRead])
def get_file_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_files(db, skip=skip, limit=limit)


@app.get("/file/summary/")
def get_file_summary(id: int, db: Session = Depends(get_db)):
    file = get_file(db, file_id=id)
    if file is None:
        raise HTTPException(status_code=404, detail="File not found")
    return {"summary": file.summary}


@app.get("/file/content/")
def get_file_content(id: int, db: Session = Depends(get_db)):
    file = get_file(db, file_id=id)
    if file is None:
        raise HTTPException(status_code=404, detail="File not found")
    return {"content": file.content}
