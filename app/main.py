from fastapi import FastAPI
from app.routes import todo_router

app = FastAPI(
    title="ToDo App",
    description="A simple ToDo API with FastAPI",
    version="1.0.0"
)

# Include the router
app.include_router(todo_router)

