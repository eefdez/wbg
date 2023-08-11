from file_manager import get_file_content, get_file_info, get_file_names
from sqlalchemy.orm import Session
from models import create_file
from chatgpt_manager import get_summary
from concurrent.futures import ThreadPoolExecutor
import os


def process_files(path: str, db: Session):
    file_paths = [os.path.join(path, file_name) for file_name in get_file_names(path)]
    with ThreadPoolExecutor() as executor:
        files = executor.map(process_file, file_paths)
    for file in files:
        create_file(db=db, file=file)


def process_file(path: str):
    file = get_file_info(path)
    file.content = get_file_content(path)
    file.summary = get_summary(file.content)
    return file
