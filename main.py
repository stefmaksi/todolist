from fastapi import FastAPI

from routers import users

app = FastAPI()

# Plug in the users router
app.include_router(users.router)


@app.get("/")
def read_root():
    return {
        "message": "Welcome to the To-Do List API! Go to /docs to see the endpoints."
    }
