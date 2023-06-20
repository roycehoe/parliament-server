from constants import IS_DEV
from database import get_database
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from logs import get_configured_logging
from services import prepopulate
from services.parliament_data import get_all_parliament_dates, get_parliament_data

app = FastAPI(docs_url="/docs" if IS_DEV else None)

CORS_ALLOWED_ORIGINS = [  # location where your frontend is running
    "http://localhost:3000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

get_configured_logging()


@app.on_event("startup")
def prepopulate_parliament_data():
    if IS_DEV:
        return
    return prepopulate.prepopulate_parliament_data()


@app.get("/hello_world")
def hello_world():
    return "hello world"


@app.get("/{date}")
def parliament_data(date: str):
    return get_parliament_data(date)


@app.get("/dates/")
def parliament_dates():
    return get_all_parliament_dates()
