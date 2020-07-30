from pydantic import BaseModel

class Record(BaseModel):
    id: int
    Albums: str
    Artist: str
    Songs: str
    

    class Config:
        orm_mode = True