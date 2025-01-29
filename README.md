# fastapi-clean-architecture

## Description

_Example Application Interface using FastAPI framework in Python 3_

This example showcases Repository Pattern in Hexagonal Architecture _(also known as Clean Architecture)_. Here we have two Entities - Books and Authors, whose relationships have been exploited to create CRUD endpoint in REST under OpenAPI standard.

## Installation

- Install poetry for env management 

  ```sh
  $ pip install poetry
  ```

- To store virtual environments in the project root run 

  ```sh
  $ virtualenvs.in-project
  ```

- Install all the project dependency using poetry:

  ```sh
  $ poetry install
  ```

- Activate the virtualenv(poetry shell moved to a plugin: poetry-plugin-shell):

  ```sh
  $ /path/to/virtual/environment/bin/activate.bat
  ```

  OR

  ```sh
  $ .\venv\Scripts\activate
  ```

- Run the application from command prompt:

  ```sh
  $ poetry run uvicorn main:app --reload
  ```

- Open `localhost:8000/docs` for API Documentation


## Testing

For Testing, `unittest` module is used for Test Suite and Assertion, whereas `pytest` is being used for Test Runner and Coverage Reporter.

- Run the following command to initiate test:
  ```sh
  $ poetry run pytest
  ```
- To include Coverage Reporting as well:
  ```sh
  $ poetry run pytest --cov-report xml --cov .
  ```
