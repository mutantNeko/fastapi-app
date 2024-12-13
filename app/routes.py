from fastapi import APIRouter, HTTPException
from app.models import Todo

todo_router = APIRouter()

# In-memory storage
todos = []

@todo_router.get("/todos", tags=["ToDo"])
def get_all_todos():
    return todos

@todo_router.post("/todos", tags=["ToDo"])
def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "Todo created successfully", "todo": todo}

@todo_router.get("/todos/{todo_id}", tags=["ToDo"])
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@todo_router.put("/todos/{todo_id}", tags=["ToDo"])
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return {"message": "Todo updated successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")

@todo_router.delete("/todos/{todo_id}", tags=["ToDo"])
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")

