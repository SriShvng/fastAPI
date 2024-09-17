from fastapi import FastAPI
from fastapi import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


# path operation


my_posts = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "Favourite foods", "content": "Pizza", "id": 2},
]


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


@app.get(
    "/"
)  # Decorators (@ symbol clarifies that this is a decorator) (app=FastAPI instance) (get= method, http method that users can use. We have plenty of http methods: get, post, put, delete ect) (within quotes: path)
def root():  # function
    return {"message": "Hello World"}


# path_Operation2


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts")
# (Body is a library, we can create a dictionary. and store it in a variable)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    return {"post_detail": post}
