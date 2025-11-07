from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from db import db

app = FastAPI(debug=True)

@app.get("/get-wydarzenie")
def get_wydarzenie():
    my_db = db()
    return my_db.get_wydarzenie()

@app.post("/save-wydarzenie")
async def save_wydarzenie(request: Request):
    wydarzenie_data = await request.json()
    #sample payload: {"name":"Test","email":"moj@email"}
    my_db = db()
    result = my_db.save_wydarzenie(wydarzenie_data)
    return JSONResponse(status_code=201, content=result)

@app.put("/edytuj-wydarzenie")
async def put_wydarzenie(request: Request):
    wydarzenie_edytuj = await request.json()
    my_db = db()
    result = my_db.put_wydarzenie(wydarzenie_edytuj)
    return JSONResponse(status_code=201, content=result)
