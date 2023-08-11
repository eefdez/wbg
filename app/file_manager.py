import os
from docx import Document
from pypdf import PdfReader
from schema import FileCreate
from mimetypes import guess_type


def get_file_names(path: str):
    try:
        return os.listdir(path)
    except Exception as e:
        print(f"Error while retrieving file list: {e}")
        raise


def get_file_info(path: str):
    try:
        file = FileCreate(
            name=os.path.basename(path),
            size=os.path.getsize(path),
            format=guess_type(path)[0],
            path=path,
            summary='',
            content=''
        )
        return file
    except Exception as e:
        print(f"Error while retrieving file info: {e}")
        raise


def get_file_content(path: str):
    try:
        extension = os.path.splitext(path)[1]
        if extension == '.docx':
            doc = Document(path)
            return '\n'.join([paragraph.text for paragraph in doc.paragraphs])
        elif extension == '.pdf':
            pdf = PdfReader(path)
            content = ''
            for i in range(len(pdf.pages)):
                content += pdf.pages[i].extract_text()
            return content
        elif extension == '.txt':
            with open(path) as file:
                return file.read()
        else:
            raise Exception(f"File type not supported for file: {path}")
    except Exception as e:
        print(f"Error retrieving file content: {e}")
        raise




