# Building a GET API Lab

## Learning Goals

- Build an API to handle GET requests.

***

## Key Vocab

- **Application Programming Interface (API)**: a software application that
  allows two or more software applications to communicate with one another.
  Can be standalone or incorporated into a larger product.
- **HTTP Request Method**: assets of HTTP requests that tell the server which
  actions the client is attempting to perform on the located resource.
- **`GET`**: the most common HTTP request method. Signifies that the client is
  attempting to view the located resource.
- **`POST`**: the second most common HTTP request method. Signifies that the
  client is attempting to submit a form to create a new resource.
- **`PATCH`**: an HTTP request method that signifies that the client is attempting
  to update a resource with new information.
- **`DELETE`**: an HTTP request method that signifies that the client is
  attempting to delete a resource.

***

## Instructions

This is a **test-driven lab**. Run `pipenv install` to create your virtual
environment and `pipenv shell` to enter the virtual environment. Then run
`pytest -x` to run your tests. Use these instructions and `pytest`'s error
messages to complete your work in the `server/` folder. Remember to set up your
environment in the `server/` folder as well:

```console
$ export FLASK_APP=app.py
$ export FLASK_RUN_PORT=5555
```

In this application, we'll be working on a JSON API to get a list of bakeries
and their baked goods. We have two models, bakeries and baked goods, that will
soon have a one-to-many relationship. The initial migrations are already set up.
Here's what the ERD for these tables looks like:

![Bakeries ERD](https://curriculum-content.s3.amazonaws.com/phase-3/sinatra-with-active-record-get-lab/bakeries-baked_goods-erd.png)

You can run the app and explore your API in the browser by using Flask command:

```console
$ flask run
```

- Update the `Bakery` and `BakedGood` models to set up the correct associations
  based on the structure of the tables. Use the `relationship()` SQLAlchemy
  method and SQLAlchemy-serializer's `SerializerMixin` class.
- `flask db init` has already been run. Run `flask db upgrade head` to create
  your database with simple `bakeries` and `baked_goods` tables.
- You will need to direct your Flask app to a database at `app.db`, update your
  models, run a migration with
  `flask db revision --autogenerate -m'<your message>'` and update the database
  file with `flask db upgrade head`.
- You should fill your database with the script in `server/seed.py`. (Though you
  can certainly write your own if you'd prefer!)
- `GET /bakeries`: returns an array of JSON objects for all bakeries in the
  database.
- `GET /bakeries/<int:id>`: returns a single bakery as JSON with its baked goods
  nested in an array. Use the `id` from the URL to look up the correct bakery.
- `GET /baked_goods/by_price`: returns an array of baked goods as JSON, sorted
  by price in descending order. (**HINT**: how can you use SQLAlchemy to sort
  the baked goods in a particular order?)
- `GET /baked_goods/most_expensive`: returns the single most expensive baked
  good as JSON. (**HINT**: how can you use SQLAlchemy to sort the baked goods
  in a particular order _and_ limit the number of results?)

Once all of your tests are passing, commit and push your work using `git` to
submit.

### Examples

#### All Bakeries

```json
[
  {
    "baked_goods": [
      {
        "bakery_id": 1,
        "created_at": "2022-09-12 21:01:00",
        "id": 8,
        "name": "Veronica",
        "price": 7,
        "updated_at": null
      },
      {
        "bakery_id": 1,
        "created_at": "2022-09-12 21:01:00",
        "id": 15,
        "name": "Sean",
        "price": 9,
        "updated_at": null
      },
      {
        "bakery_id": 1,
        "created_at": "2022-09-12 21:01:00",
        "id": 25,
        "name": "Robin",
        "price": 3,
        "updated_at": null
      },
      {
        "bakery_id": 1,
        "created_at": "2022-09-12 21:01:00",
        "id": 27,
        "name": "Derek",
        "price": 7,
        "updated_at": null
      },
      {
        "bakery_id": 1,
        "created_at": "2022-09-12 21:01:00",
        "id": 105,
        "name": "Holly",
        "price": 10,
        "updated_at": null
      },
      {
        "bakery_id": 1,
        "created_at": "2022-09-12 21:01:00",
        "id": 173,
        "name": "Maureen",
        "price": 8,
        "updated_at": null
      },
      {
        "bakery_id": 1,
        "created_at": "2022-09-12 21:01:00",
        "id": 187,
        "name": "Jennifer",
        "price": 5,
        "updated_at": null
      }
    ],
    "created_at": "2022-09-12 21:01:00",
    "id": 1,
    "name": "Jones-Erickson",
    "updated_at": null
  },
  {
    "baked_goods": [
      {
        "bakery_id": 2,
        "created_at": "2022-09-12 21:01:00",
        "id": 76,
        "name": "Samantha",
        "price": 7,
        "updated_at": null
      },
      {
        "bakery_id": 2,
        "created_at": "2022-09-12 21:01:00",
        "id": 95,
        "name": "Jeffrey",
        "price": 5,
        "updated_at": null
      },
      {
        "bakery_id": 2,
        "created_at": "2022-09-12 21:01:00",
        "id": 125,
        "name": "Pamela",
        "price": 5,
        "updated_at": null
      },
      {
        "bakery_id": 2,
        "created_at": "2022-09-12 21:01:00",
        "id": 149,
        "name": "Brandy",
        "price": 7,
        "updated_at": null
      },
      {
        "bakery_id": 2,
        "created_at": "2022-09-12 21:01:00",
        "id": 175,
        "name": "Kendra",
        "price": 8,
        "updated_at": null
      }
    ],
    "created_at": "2022-09-12 21:01:00",
    "id": 2,
    "name": "Cook-Cunningham",
    "updated_at": null
  },
  // ...
]
```

#### Bakery by ID

```json
{
  "baked_goods": [
    {
      "bakery_id": 2,
      "created_at": "2022-09-12 21:01:00",
      "id": 76,
      "name": "Samantha",
      "price": 7,
      "updated_at": null
    },
    {
      "bakery_id": 2,
      "created_at": "2022-09-12 21:01:00",
      "id": 95,
      "name": "Jeffrey",
      "price": 5,
      "updated_at": null
    },
    {
      "bakery_id": 2,
      "created_at": "2022-09-12 21:01:00",
      "id": 125,
      "name": "Pamela",
      "price": 5,
      "updated_at": null
    },
    {
      "bakery_id": 2,
      "created_at": "2022-09-12 21:01:00",
      "id": 149,
      "name": "Brandy",
      "price": 7,
      "updated_at": null
    },
    {
      "bakery_id": 2,
      "created_at": "2022-09-12 21:01:00",
      "id": 175,
      "name": "Kendra",
      "price": 8,
      "updated_at": null
    }
  ],
  "created_at": "2022-09-12 21:01:00",
  "id": 2,
  "name": "Cook-Cunningham",
  "updated_at": null
}
```

#### Baked Goods By Price

```json
[
  {
    "bakery": {
      "created_at": "2022-09-12 21:15:43",
      "id": 3,
      "name": "Schneider Ltd",
      "updated_at": null
    },
    "bakery_id": 3,
    "created_at": "2022-09-12 21:15:43",
    "id": 11,
    "name": "Antonio",
    "price": 1,
    "updated_at": null
  },
  {
    "bakery": {
      "created_at": "2022-09-12 21:15:43",
      "id": 4,
      "name": "Ingram, Griffith and Morris",
      "updated_at": null
    },
    "bakery_id": 4,
    "created_at": "2022-09-12 21:15:43",
    "id": 15,
    "name": "Drew",
    "price": 1,
    "updated_at": null
  },
  // ...
]
```

#### Most Expensive Baked Good

```json
{
  "bakery": {
    "created_at": "2022-09-12 21:15:43",
    "id": 11,
    "name": "Hodge-Stuart",
    "updated_at": null
  },
  "bakery_id": 11,
  "created_at": "2022-09-12 21:15:43",
  "id": 91,
  "name": "Jessica",
  "price": 100,
  "updated_at": "2022-09-12 21:15:43"
}
```

***

## Resources

- [Flask - Pallets](https://flask.palletsprojects.com/en/2.2.x/)
- [GET - Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET)
- [flask.json.jsonify Example Code - Full Stack Python](https://www.fullstackpython.com/flask-json-jsonify-examples.html)
- [SQLAlchemy-serializer - PyPI](https://pypi.org/project/SQLAlchemy-serializer/)
