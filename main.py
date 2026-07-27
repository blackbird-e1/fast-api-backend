from fastapi import FastAPI

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Atomic Habits",
        "author": "James Clear"
    },
    {
        "id": 2,
        "title": "Deep Work",
        "author": "Cal Newport"
    }
]

@app.get("/")
def home():
    return {
        "message": "Welcome to the Books API"
    }


@app.get("/books")
def get_books():
    return books