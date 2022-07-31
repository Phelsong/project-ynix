from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from calc import single_skill
from queries import *

# -----------------------------------------------------------------------------
app = FastAPI()
# -----------------------------------------------------------------------------
origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://localhost:3000",
    "http://127.0.0.1"
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


@app.get("/api")
def health_check():
    return {"Server Status": "You've got Py"}
# -----------------------------------------------------------------------------


@app.get("/classes/{class_id}")
async def get_class(class_id):
    [data] = get_class_query(class_id)
    return data
# -----------------------------------------------------------------------------


@app.put("/basic_calc")
def basic_calc():
    return single_skill()
# ------------------------------------------------------------------------------


@app.get("/zones")
def get_zone_list():
    data = get_zone_list_query()
    return data
    
#------------------------------------------------------------------------------

@app.get("/zones/{zone_id}")
async def get_zone_info(zone_id):
    [data] = get_zone_query(zone_id)
    return data

#------------------------------------------------------------------------------

