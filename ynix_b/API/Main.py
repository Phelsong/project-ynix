from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ynix_b.API.calc import single_skill
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

@app.get("/api")
def health_check():
    return {"You've Got": "Py"}
# -----------------------------------------------------------------------------
@app.get("/classes/:class")
def get_class(class_name):
    return {"You've Got": class_name}
# -----------------------------------------------------------------------------
@app.put("/basic_calc")
def basic_calc():
    return single_skill()
#------------------------------------------------------------------------------
