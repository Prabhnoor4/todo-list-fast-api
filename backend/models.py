
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from database import Base
from datetime import datetime

class Todo(Base):
    __tablename__='tasks'
    
    id=Column(Integer,primary_key=True,nullable=False,index=True)
    title=Column(String, index=True)
    description=Column(String,default="")
    completed= Column(Boolean,default=False)
    due_date= Column(DateTime,default=datetime.utcnow)
    
    