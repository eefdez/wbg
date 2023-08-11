from pydantic import BaseModel


class FileBase(BaseModel):
    name: str
    format: str


class FileCreate(FileBase):
    summary: str
    content: str
    path: str
    size: int


class FileRead(FileBase):
    id: int

    class Config:
        orm_mode = True
