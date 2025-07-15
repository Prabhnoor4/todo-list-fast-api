from datetime import datetime
from pydantic import BaseModel

class create(BaseModel):
    title: str
    description: str
    due_date: datetime
    
class update(create):
    completed: bool
    
class out(update):
    id: int
    
    class Config:
        orm_mode= True


    
    