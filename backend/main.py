from fastapi import HTTPException,FastAPI,Depends
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import engine,get_db

models.Base.metadata.create_all(bind=engine)

app= FastAPI()

@app.post("/todos/",response_model=schemas.out)
def create(todo: schemas.create,db: Session = Depends(get_db)):
    return crud.create_todo(db,todo)

@app.get('/todos/',response_model=list[schemas.out])
def read_all(db:Session = Depends(get_db)):
    return crud.get_todos(db)

@app.get('/todos/{todo_id}',response_model=schemas.out)
def read_one(todo_id: int,db:Session = Depends(get_db)):
    db_todo =  crud.get_todo(db,todo_id)
    if not db_todo:
        raise HTTPException(status_code=404,detail=f'The item with id: {todo_id} does not exist')
    
    return db_todo


@app.put('/todo/{todo_id}',response_model= schemas.update)
def update_one(todo_id: int,todo: schemas.update,db: Session=Depends(get_db)):
    return crud.update_todo()


@app.delete('/todo/{todo_id}',response_model=schemas.out)
def del_todo(todo_id: int,db:Session=Depends(get_db)):
        crud.delete_todo(db,todo_id)
        return {'message':'deleted successfully'}
    
    

