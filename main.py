from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field

app = FastAPI()


@app.get("/", description="This is our first route")
async def root():
    return {"message": "hello there"}


@app.post("/")
async def post():
    return {"message": "Hello from the post route"}


@app.put("/")
async def put():
    return {"message": "hello from the put route"}

# @app.get("/items")
# async def get_items():
#     return {"message": "list of items"}


# @app.get("/items/{item_id}")
# async def show_particular_item(item_id: int):
#     return {"item id": item_id}


# @app.get("/items/{item_id}")
# async def get_items(item_id: int):
#     return {"message": item_id}


# @app.get("/items/{path_parameter}")
# async def path_vs_query_param(path_parameter: str, query_parameter: str | None = None):
#     return {"path parameter": path_parameter,
#             "query parameter": query_parameter}

class Image(BaseModel):
    url: str = Field("string")
    name: str = Field("string")


class Item(BaseModel):
    name: str
    price: float = Field(..., gt=0, description="Price must be greater than 0")
    description: str | None = Field(None, title="description of the item", max_length=300)
    tax: float | None = None
    tags: set[int] = []
    image: Image | None = None


item_db = {
    "I0": Item(
        name="Dummy",
        price=0.01,
        description="Dummy placeholder item",
        tax=0,
    ),
    "I1": Item(
        name="Mouse",
        price=24,
        description="A Wired Mouse",
        tax=1.5,
    ),
    "I2": Item(
        name="Keyboard",
        price=30,
        description="A Wired Keyboard",
        tax=1.5,
    ),
    "I3": Item(
        name="Headphone",
        price=50,
        description="A Wireless Mouse",
        tax=2,
    )
}


@app.post("/items")
async def create_item(item: Item):
    return item


# @app.get("/items/read")
# async def read_items(qp1: list[str] | None = Query(["-1", "-2"], alias="1st query parameter"),
#                      qp2: list[str] | None = Query(None)):
#     print(qp1, qp2)
#     # if item_id and item_id in item_db:
#     #     return item_db[item_id]
#     return {"qp1": qp1, "qp2": qp2}

# @app.get("/items/{item_id}")
# async def read_items(*,
#                      item_id: int = Path(..., title="Id pof the item to get", gt=10, le=100),
#                      q: str = Query(None)):
#     print(item_id, q)
#     # if item_id and item_id in item_db:
#     #     return item_db[item_id]
#     return {"item id": item_id}

@app.post("/items/read")
async def read_items(item: Item = Body(...,
                                       embed=True,
                                       example={
                                                "name": "Foo",
                                                "description": "A very nice Item",
                                                "price": 16.25,
                                                "tax": 1.5
                                                }),
                     random_id: int = Body(None)):
    print(item, random_id)
    # if item_id and item_id in item_db:
    #     return item_db[item_id]
    return {"item ": item, "random id": random_id}


@app.post("/images/multiple")
async def multiple_images(images: list[Image]):
    return images
