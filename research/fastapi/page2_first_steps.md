Title: First Steps - FastAPI

URL Source: https://fastapi.tiangolo.com/tutorial/first-steps/

Markdown Content:
The simplest FastAPI file could look like this:

Python 3.8+

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

Copy that to a file `main.py`.

Run the live server:

```
$ <font color="#4E9A06">fastapi</font> dev <u style="text-decoration-style:solid">main.py</u>

  <span style="background-color:#009485"><font color="#D3D7CF"> FastAPI </font></span>  Starting development server 🚀

             Searching for package file structure from directories
             with <font color="#3465A4">__init__.py</font> files
             Importing from <font color="#75507B">/home/user/code/</font><font color="#AD7FA8">awesomeapp</font>

   <span style="background-color:#007166"><font color="#D3D7CF"> module </font></span>  🐍 main.py

     <span style="background-color:#007166"><font color="#D3D7CF"> code </font></span>  Importing the FastAPI app object from the module with
             the following code:

             <u style="text-decoration-style:solid">from </u><u style="text-decoration-style:solid"><b>main</b></u><u style="text-decoration-style:solid"> import </u><u style="text-decoration-style:solid"><b>app</b></u>

      <span style="background-color:#007166"><font color="#D3D7CF"> app </font></span>  Using import string: <font color="#3465A4">main:app</font>

   <span style="background-color:#007166"><font color="#D3D7CF"> server </font></span>  Server started at <font color="#729FCF"><u style="text-decoration-style:solid">http://127.0.0.1:8000</u></font>
   <span style="background-color:#007166"><font color="#D3D7CF"> server </font></span>  Documentation at <font color="#729FCF"><u style="text-decoration-style:solid">http://127.0.0.1:8000/docs</u></font>

      <span style="background-color:#007166"><font color="#D3D7CF"> tip </font></span>  Running in development mode, for production use:
             <b>fastapi run</b>

             Logs:

     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Will watch for changes in these directories:
             <b>[</b><font color="#4E9A06">&apos;/home/user/code/awesomeapp&apos;</font><b>]</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Uvicorn running on <font color="#729FCF"><u style="text-decoration-style:solid">http://127.0.0.1:8000</u></font> <b>(</b>Press CTRL+C
             to quit<b>)</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Started reloader process <b>[</b><font color="#34E2E2"><b>383138</b></font><b>]</b> using WatchFiles
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Started server process <b>[</b><font color="#34E2E2"><b>383153</b></font><b>]</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Waiting for application startup.
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Application startup complete.
```

In the output, there's a line with something like:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

That line shows the URL where your app is being served, in your local machine.

### Check it[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#check-it "Permanent link")

Open your browser at [http://127.0.0.1:8000](http://127.0.0.1:8000/).

You will see the JSON response as:

```
{"message": "Hello World"}
```

### Interactive API docs[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#interactive-api-docs "Permanent link")

Now go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

You will see the automatic interactive API documentation (provided by [Swagger UI](https://github.com/swagger-api/swagger-ui)):

![Image 1: Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)

### Alternative API docs[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#alternative-api-docs "Permanent link")

And now, go to [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).

You will see the alternative automatic documentation (provided by [ReDoc](https://github.com/Rebilly/ReDoc)):

![Image 2: ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

### OpenAPI[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#openapi "Permanent link")

**FastAPI** generates a "schema" with all your API using the **OpenAPI** standard for defining APIs.

#### "Schema"[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#schema "Permanent link")

A "schema" is a definition or description of something. Not the code that implements it, but just an abstract description.

#### API "schema"[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#api-schema "Permanent link")

In this case, [OpenAPI](https://github.com/OAI/OpenAPI-Specification) is a specification that dictates how to define a schema of your API.

This schema definition includes your API paths, the possible parameters they take, etc.

#### Data "schema"[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#data-schema "Permanent link")

The term "schema" might also refer to the shape of some data, like a JSON content.

In that case, it would mean the JSON attributes, and data types they have, etc.

#### OpenAPI and JSON Schema[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#openapi-and-json-schema "Permanent link")

OpenAPI defines an API schema for your API. And that schema includes definitions (or "schemas") of the data sent and received by your API using **JSON Schema**, the standard for JSON data schemas.

#### Check the `openapi.json`[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#check-the-openapi-json "Permanent link")

If you are curious about how the raw OpenAPI schema looks like, FastAPI automatically generates a JSON (schema) with the descriptions of all your API.

You can see it directly at: [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json).

It will show a JSON starting with something like:

```
{
    "openapi": "3.1.0",
    "info": {
        "title": "FastAPI",
        "version": "0.1.0"
    },
    "paths": {
        "/items/": {
            "get": {
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {

...
```

#### What is OpenAPI for[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#what-is-openapi-for "Permanent link")

The OpenAPI schema is what powers the two interactive documentation systems included.

And there are dozens of alternatives, all based on OpenAPI. You could easily add any of those alternatives to your application built with **FastAPI**.

You could also use it to generate code automatically, for clients that communicate with your API. For example, frontend, mobile or IoT applications.

Recap, step by step[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#recap-step-by-step "Permanent link")
--------------------------------------------------------------------------------------------------------------

### Step 1: import `FastAPI`[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#step-1-import-fastapi "Permanent link")

Python 3.8+

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

`FastAPI` is a Python class that provides all the functionality for your API.

Technical Details

`FastAPI` is a class that inherits directly from `Starlette`.

You can use all the [Starlette](https://www.starlette.io/) functionality with `FastAPI` too.

### Step 2: create a `FastAPI` "instance"[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#step-2-create-a-fastapi-instance "Permanent link")

Python 3.8+

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

Here the `app` variable will be an "instance" of the class `FastAPI`.

This will be the main point of interaction to create all your API.

### Step 3: create a _path operation_[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#step-3-create-a-path-operation "Permanent link")

#### Path[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#path "Permanent link")

"Path" here refers to the last part of the URL starting from the first `/`.

So, in a URL like:

```
https://example.com/items/foo
```

...the path would be:

```
/items/foo
```

Info

A "path" is also commonly called an "endpoint" or a "route".

While building an API, the "path" is the main way to separate "concerns" and "resources".

#### Operation[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#operation "Permanent link")

"Operation" here refers to one of the HTTP "methods".

One of:

*   `POST`
*   `GET`
*   `PUT`
*   `DELETE`

...and the more exotic ones:

*   `OPTIONS`
*   `HEAD`
*   `PATCH`
*   `TRACE`

In the HTTP protocol, you can communicate to each path using one (or more) of these "methods".

* * *

When building APIs, you normally use these specific HTTP methods to perform a specific action.

Normally you use:

*   `POST`: to create data.
*   `GET`: to read data.
*   `PUT`: to update data.
*   `DELETE`: to delete data.

So, in OpenAPI, each of the HTTP methods is called an "operation".

We are going to call them "**operations**" too.

#### Define a _path operation decorator_[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#define-a-path-operation-decorator "Permanent link")

Python 3.8+

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

The `@app.get("/")` tells **FastAPI** that the function right below is in charge of handling requests that go to:

*   the path `/`
*   using a `get` operation

`@decorator` Info

That `@something` syntax in Python is called a "decorator".

You put it on top of a function. Like a pretty decorative hat (I guess that's where the term came from).

A "decorator" takes the function below and does something with it.

In our case, this decorator tells **FastAPI** that the function below corresponds to the **path**`/` with an **operation**`get`.

It is the "**path operation decorator**".

You can also use the other operations:

*   `@app.post()`
*   `@app.put()`
*   `@app.delete()`

And the more exotic ones:

*   `@app.options()`
*   `@app.head()`
*   `@app.patch()`
*   `@app.trace()`

Tip

You are free to use each operation (HTTP method) as you wish.

**FastAPI** doesn't enforce any specific meaning.

The information here is presented as a guideline, not a requirement.

For example, when using GraphQL you normally perform all the actions using only `POST` operations.

### Step 4: define the **path operation function**[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#step-4-define-the-path-operation-function "Permanent link")

This is our "**path operation function**":

*   **path**: is `/`.
*   **operation**: is `get`.
*   **function**: is the function below the "decorator" (below `@app.get("/")`).

Python 3.8+

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

This is a Python function.

It will be called by **FastAPI** whenever it receives a request to the URL "`/`" using a `GET` operation.

In this case, it is an `async` function.

* * *

You could also define it as a normal function instead of `async def`:

Python 3.8+

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}
```

### Step 5: return the content[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#step-5-return-the-content "Permanent link")

Python 3.8+

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

You can return a `dict`, `list`, singular values as `str`, `int`, etc.

You can also return Pydantic models (you'll see more about that later).

There are many other objects and models that will be automatically converted to JSON (including ORMs, etc). Try using your favorite ones, it's highly probable that they are already supported.

Recap[¶](https://fastapi.tiangolo.com/tutorial/first-steps/#recap "Permanent link")
-----------------------------------------------------------------------------------

*   Import `FastAPI`.
*   Create an `app` instance.
*   Write a **path operation decorator** using decorators like `@app.get("/")`.
*   Define a **path operation function**; for example, `def root(): ...`.
*   Run the development server using the command `fastapi dev`.
