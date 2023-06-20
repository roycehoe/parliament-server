# Introduction

Responsible for obtaining and serving unadulterated hansard data

# Gettin Started

- Install [poetry](https://python-poetry.org/docs/1.3#installing-with-the-official-installer) on your machine
- Go into the backend directory
- Install all project dependencies with `poetry install`
- Activate the project virtual environment by running the command `poetry shell`
- Run the command `uvicorn main:app --reload` to start the backend server on your machine. The server should be running on localhost:8000
- Optional: To view the Swagger UI of this application, create a .env file in the backend directory and add the following line: `IS_DEV="True"`. You may visit the Swagger UI page at localhost:8000/docs
