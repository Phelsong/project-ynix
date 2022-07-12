from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas
import psycopg2
# -----------------------------------------------------------------------------
app = FastAPI()
# -----------------------------------------------------------------------------
origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://localhost:3000",
    "http://127.0.0.1:"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

@app.get("/")
def read_root():
    return {"You've Got": "Py"}
# -----------------------------------------------------------------------------

