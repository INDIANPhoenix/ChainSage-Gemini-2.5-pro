Title: Path Parameters - FastAPI

URL Source: https://fastapi.tiangolo.com/tutorial/path-params/

Markdown Content:
You can declare path "parameters" or "variables" with the same syntax used by Python format strings:

Python 3.8+

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
```

The value of the path parameter `item_id` will be passed to your function as the argument `item_id`.

So, if you run this example and go to [http://127.0.0.1:8000/items/foo](http://127.0.0.1:8000/items/foo), you will see a response of:

```
{"item_id":"foo"}
```

Path parameters with types[¶](https://fastapi.tiangolo.com/tutorial/path-params/#path-parameters-with-types "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------

You can declare the type of a path parameter in the function, using standard Python type annotations:

Python 3.8+

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

In this case, `item_id` is declared to be an `int`.

Check

This will give you editor support inside of your function, with error checks, completion, etc.

Data conversion[¶](https://fastapi.tiangolo.com/tutorial/path-params/#data-conversion "Permanent link")
-------------------------------------------------------------------------------------------------------

If you run this example and open your browser at [http://127.0.0.1:8000/items/3](http://127.0.0.1:8000/items/3), you will see a response of:

```
{"item_id":3}
```

Check

Notice that the value your function received (and returned) is `3`, as a Python `int`, not a string `"3"`.

So, with that type declaration, **FastAPI** gives you automatic request "parsing".

Data validation[¶](https://fastapi.tiangolo.com/tutorial/path-params/#data-validation "Permanent link")
-------------------------------------------------------------------------------------------------------

But if you go to the browser at [http://127.0.0.1:8000/items/foo](http://127.0.0.1:8000/items/foo), you will see a nice HTTP error of:

```
{
  "detail": [
    {
      "type": "int_parsing",
      "loc": [
        "path",
        "item_id"
      ],
      "msg": "Input should be a valid integer, unable to parse string as an integer",
      "input": "foo"
    }
  ]
}
```

because the path parameter `item_id` had a value of `"foo"`, which is not an `int`.

The same error would appear if you provided a `float` instead of an `int`, as in: [http://127.0.0.1:8000/items/4.2](http://127.0.0.1:8000/items/4.2)

Check

So, with the same Python type declaration, **FastAPI** gives you data validation.

Notice that the error also clearly states exactly the point where the validation didn't pass.

This is incredibly helpful while developing and debugging code that interacts with your API.

Documentation[¶](https://fastapi.tiangolo.com/tutorial/path-params/#documentation "Permanent link")
---------------------------------------------------------------------------------------------------

And when you open your browser at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs), you will see an automatic, interactive, API documentation like:

![Image 1](https://fastapi.tiangolo.com/img/tutorial/path-params/image01.png)

Check

Again, just with that same Python type declaration, **FastAPI** gives you automatic, interactive documentation (integrating Swagger UI).

Notice that the path parameter is declared to be an integer.

Standards-based benefits, alternative documentation[¶](https://fastapi.tiangolo.com/tutorial/path-params/#standards-based-benefits-alternative-documentation "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

And because the generated schema is from the [OpenAPI](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.1.0.md) standard, there are many compatible tools.

Because of this, **FastAPI** itself provides an alternative API documentation (using ReDoc), which you can access at [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc):

![Image 2](https://fastapi.tiangolo.com/img/tutorial/path-params/image02.png)

The same way, there are many compatible tools. Including code generation tools for many languages.

Pydantic[¶](https://fastapi.tiangolo.com/tutorial/path-params/#pydantic "Permanent link")
-----------------------------------------------------------------------------------------

All the data validation is performed under the hood by [Pydantic](https://docs.pydantic.dev/), so you get all the benefits from it. And you know you are in good hands.

You can use the same type declarations with `str`, `float`, `bool` and many other complex data types.

Several of these are explored in the next chapters of the tutorial.

Order matters[¶](https://fastapi.tiangolo.com/tutorial/path-params/#order-matters "Permanent link")
---------------------------------------------------------------------------------------------------

When creating _path operations_, you can find situations where you have a fixed path.

Like `/users/me`, let's say that it's to get data about the current user.

And then you can also have a path `/users/{user_id}` to get data about a specific user by some user ID.

Because _path operations_ are evaluated in order, you need to make sure that the path for `/users/me` is declared before the one for `/users/{user_id}`:

Python 3.8+

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
```

Otherwise, the path for `/users/{user_id}` would match also for `/users/me`, "thinking" that it's receiving a parameter `user_id` with a value of `"me"`.

Similarly, you cannot redefine a path operation:

Python 3.8+

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]

@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]
```

The first one will always be used since the path matches first.

Predefined values[¶](https://fastapi.tiangolo.com/tutorial/path-params/#predefined-values "Permanent link")
-----------------------------------------------------------------------------------------------------------

If you have a _path operation_ that receives a _path parameter_, but you want the possible valid _path parameter_ values to be predefined, you can use a standard Python `Enum`.

### Create an `Enum` class[¶](https://fastapi.tiangolo.com/tutorial/path-params/#create-an-enum-class "Permanent link")

Import `Enum` and create a sub-class that inherits from `str` and from `Enum`.

By inheriting from `str` the API docs will be able to know that the values must be of type `string` and will be able to render correctly.

Then create class attributes with fixed values, which will be the available valid values:

Python 3.8+

```
from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
```

Tip

If you are wondering, "AlexNet", "ResNet", and "LeNet" are just names of Machine Learning models.

### Declare a _path parameter_[¶](https://fastapi.tiangolo.com/tutorial/path-params/#declare-a-path-parameter "Permanent link")

Then create a _path parameter_ with a type annotation using the enum class you created (`ModelName`):

Python 3.8+

```
from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
```

### Check the docs[¶](https://fastapi.tiangolo.com/tutorial/path-params/#check-the-docs "Permanent link")

Because the available values for the _path parameter_ are predefined, the interactive docs can show them nicely:

![Image 3](https://fastapi.tiangolo.com/img/tutorial/path-params/image03.png)

### Working with Python _enumerations_[¶](https://fastapi.tiangolo.com/tutorial/path-params/#working-with-python-enumerations "Permanent link")

The value of the _path parameter_ will be an _enumeration member_.

#### Compare _enumeration members_[¶](https://fastapi.tiangolo.com/tutorial/path-params/#compare-enumeration-members "Permanent link")

You can compare it with the _enumeration member_ in your created enum `ModelName`:

Python 3.8+

```
from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
```

#### Get the _enumeration value_[¶](https://fastapi.tiangolo.com/tutorial/path-params/#get-the-enumeration-value "Permanent link")

You can get the actual value (a `str` in this case) using `model_name.value`, or in general, `your_enum_member.value`:

Python 3.8+

```
from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
```

Tip

You could also access the value `"lenet"` with `ModelName.lenet.value`.

#### Return _enumeration members_[¶](https://fastapi.tiangolo.com/tutorial/path-params/#return-enumeration-members "Permanent link")

You can return _enum members_ from your _path operation_, even nested in a JSON body (e.g. a `dict`).

They will be converted to their corresponding values (strings in this case) before returning them to the client:

Python 3.8+

```
from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
```

In your client you will get a JSON response like:

```
{
  "model_name": "alexnet",
  "message": "Deep Learning FTW!"
}
```

Path parameters containing paths[¶](https://fastapi.tiangolo.com/tutorial/path-params/#path-parameters-containing-paths "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------

Let's say you have a _path operation_ with a path `/files/{file_path}`.

But you need `file_path` itself to contain a _path_, like `home/johndoe/myfile.txt`.

So, the URL for that file would be something like: `/files/home/johndoe/myfile.txt`.

### OpenAPI support[¶](https://fastapi.tiangolo.com/tutorial/path-params/#openapi-support "Permanent link")

OpenAPI doesn't support a way to declare a _path parameter_ to contain a _path_ inside, as that could lead to scenarios that are difficult to test and define.

Nevertheless, you can still do it in **FastAPI**, using one of the internal tools from Starlette.

And the docs would still work, although not adding any documentation telling that the parameter should contain a path.

### Path convertor[¶](https://fastapi.tiangolo.com/tutorial/path-params/#path-convertor "Permanent link")

Using an option directly from Starlette you can declare a _path parameter_ containing a _path_ using a URL like:

```
/files/{file_path:path}
```

In this case, the name of the parameter is `file_path`, and the last part, `:path`, tells it that the parameter should match any _path_.

So, you can use it with:

Python 3.8+

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
```

Tip

You might need the parameter to contain `/home/johndoe/myfile.txt`, with a leading slash (`/`).

In that case, the URL would be: `/files//home/johndoe/myfile.txt`, with a double slash (`//`) between `files` and `home`.

Recap[¶](https://fastapi.tiangolo.com/tutorial/path-params/#recap "Permanent link")
-----------------------------------------------------------------------------------

With **FastAPI**, by using short, intuitive and standard Python type declarations, you get:

*   Editor support: error checks, autocompletion, etc.
*   Data "parsing"
*   Data validation
*   API annotation and automatic documentation

And you only have to declare them once.

That's probably the main visible advantage of **FastAPI** compared to alternative frameworks (apart from the raw performance).
